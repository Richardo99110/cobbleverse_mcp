"""
HTTP bridge — exposes the MCP tools over a REST API and uses a local
Ollama LLM (llama3.2) to understand natural language queries.

Architecture:
  User question
      │
      ▼
  LLM (Ollama llama3.2)  ← decides which KB entries are relevant
      │
      ▼
  Knowledge Base retrieval  ← fetches the raw wiki content
      │
      ▼
  LLM (Ollama llama3.2)  ← writes a friendly, grounded answer
      │
      ▼
  Web chatbot

Run with:  python mcp_server/http_server.py
Serves on: http://localhost:8000
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

import json
import ollama

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse, StreamingResponse
from pydantic import BaseModel
import uvicorn

from knowledge_base import INSTALLATION, GAMEPLAY
from pokemon_spawns import POKEMON_SPAWNS, search_pokemon, format_pokemon, SOURCE_URL

# ── config ────────────────────────────────────────────────────────────────────

LLM_MODEL = "llama3.2"

SECTION_MAP = {
    "installation": INSTALLATION,
    "gameplay": GAMEPLAY,
}

# All KB entries flattened for the LLM to reason over
ALL_ENTRIES: list[dict] = []
for section, kb in SECTION_MAP.items():
    for key, entry in kb.items():
        ALL_ENTRIES.append({**entry, "key": key, "section": section})

# ── FastAPI app ───────────────────────────────────────────────────────────────

app = FastAPI(title="COBBLEVERSE Wiki API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

# ── LLM helpers ───────────────────────────────────────────────────────────────

def _build_entry_index() -> str:
    """Compact index of all KB entries shown to the LLM for selection."""
    lines = []
    for e in ALL_ENTRIES:
        lines.append(f'- key="{e["key"]}" section="{e["section"]}" title="{e["title"]}"')
    return "\n".join(lines)


ENTRY_INDEX = _build_entry_index()


def _is_pokemon_query(query: str) -> bool:
    """Detect if the user is asking about a specific Pokemon's spawn location."""
    q = query.lower()
    # Check if any Pokemon name appears in the query
    for key, p in POKEMON_SPAWNS.items():
        if key in q or p["name"].lower() in q:
            return True
    # Check for pokemon-finding intent words
    pokemon_signals = ["where to find", "where can i find", "how to catch", "how do i catch",
                       "where does", "spawn location", "where is", "how to get",
                       "pokemon spawn", "pokémon spawn", "pokedex", "pokédex",
                       "alolan", "galarian", "hisuian", "paldean"]
    return any(s in q for s in pokemon_signals)


POKEMON_PROMPT_TEMPLATE = """You are a helpful assistant for the COBBLEVERSE Minecraft modpack wiki.
Answer the user's question about Pokemon spawns using ONLY the data below.
Be friendly and concise. Use markdown formatting.

IMPORTANT RULES:
- "Base spawn biomes" is where the NORMAL/DEFAULT form of the Pokemon spawns in the wild.
- "ALTERNATIVE FORMS & THEIR SPAWN LOCATIONS" lists regional variants (Alolan, Galarian, Hisuian, Paldean, etc.) and their DIFFERENT spawn biomes.
- If the user asks about a specific form (e.g. "Alolan Pikachu"), answer with the spawn location listed for THAT FORM, NOT the base spawn location.
- Always clearly distinguish between the base form and alternative forms in your answer.
- FOSSIL POKEMON: Some Pokemon are marked as "FOSSIL POKEMON". These CANNOT be found in the wild normally. Instead, the player must:
  1. Find the fossil at the listed "Fossil dig sites" (as Suspicious Sand or Gravel blocks).
  2. Use a Resurrection Machine to revive the fossil into the Pokemon.
  3. Some fossil Pokemon may ALSO be found wild in certain caves (noted in "Additional info").
  When answering about fossil Pokemon, always explain the fossil revival process.

Source: {source_url}

Pokemon spawn data:
{context}

User question: {user_query}

Answer:"""


def _answer_pokemon_query(user_query: str) -> str | None:
    """If the query is about a specific Pokemon, search the spawn DB and answer with LLM."""
    results = search_pokemon(user_query)
    if not results:
        return None

    context_parts = []
    for p in results[:5]:
        context_parts.append(format_pokemon(p))
    context = "\n\n".join(context_parts)

    prompt = POKEMON_PROMPT_TEMPLATE.format(
        source_url=SOURCE_URL, context=context, user_query=user_query
    )

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3},
    )
    return response["message"]["content"].strip()


def _answer_pokemon_query_stream(user_query: str):
    """Streaming version for pokemon queries. Returns None if no results."""
    results = search_pokemon(user_query)
    if not results:
        return None

    context_parts = [format_pokemon(p) for p in results[:5]]
    context = "\n\n".join(context_parts)

    prompt = POKEMON_PROMPT_TEMPLATE.format(
        source_url=SOURCE_URL, context=context, user_query=user_query
    )

    # Return the stream iterator directly (not a generator function)
    return ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3},
        stream=True,
    )


def _select_entries_with_llm(user_query: str) -> list[dict]:
    """
    Ask the LLM which KB entry keys are relevant to the user's question.
    Returns a list of matching entry dicts.
    """
    prompt = f"""You are a routing assistant for the COBBLEVERSE Minecraft modpack wiki.

Given a user question, select the most relevant knowledge base entries from the list below.
Reply with ONLY a JSON array of key strings, e.g. ["install_modrinth", "server_apex"].
Select 1–3 keys. If nothing is relevant, return [].

Available entries:
{ENTRY_INDEX}

User question: {user_query}

Reply with JSON only:"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0},
    )
    raw = response["message"]["content"].strip()

    # Extract JSON array from the response (LLM may add extra text)
    start = raw.find("[")
    end = raw.rfind("]") + 1
    if start == -1 or end == 0:
        return []

    try:
        keys = json.loads(raw[start:end])
    except json.JSONDecodeError:
        return []

    entry_map = {e["key"]: e for e in ALL_ENTRIES}
    return [entry_map[k] for k in keys if k in entry_map]


def _answer_with_llm(user_query: str, entries: list[dict]) -> str:
    """
    Given the retrieved KB entries, ask the LLM to write a helpful answer.
    """
    context_parts = []
    for e in entries:
        context_parts.append(f"### {e['title']}\n{e['content']}\nSource: {e['url']}")
    context = "\n\n".join(context_parts)

    prompt = f"""You are a helpful assistant for the COBBLEVERSE Minecraft modpack wiki.
Answer the user's question using ONLY the information provided in the context below.
Be friendly, clear, and concise. Use markdown formatting where helpful (bullet points, bold text).
If the context doesn't fully answer the question, say so honestly.
Always mention the source URL at the end.

Context:
{context}

User question: {user_query}

Answer:"""

    response = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3},
    )
    return response["message"]["content"].strip()


def _answer_with_llm_stream(user_query: str, entries: list[dict]):
    """Streaming version of _answer_with_llm — yields text chunks."""
    context_parts = []
    for e in entries:
        context_parts.append(f"### {e['title']}\n{e['content']}\nSource: {e['url']}")
    context = "\n\n".join(context_parts)

    prompt = f"""You are a helpful assistant for the COBBLEVERSE Minecraft modpack wiki.
Answer the user's question using ONLY the information provided in the context below.
Be friendly, clear, and concise. Use markdown formatting where helpful (bullet points, bold text).
If the context doesn't fully answer the question, say so honestly.
Always mention the source URL at the end.

Context:
{context}

User question: {user_query}

Answer:"""

    stream = ollama.chat(
        model=LLM_MODEL,
        messages=[{"role": "user", "content": prompt}],
        options={"temperature": 0.3},
        stream=True,
    )
    for chunk in stream:
        delta = chunk["message"]["content"]
        if delta:
            yield delta


# ── keyword fallback search (used when LLM routing fails) ────────────────────

def _keyword_search(query: str) -> list[dict]:
    q = query.lower()
    results = []
    for e in ALL_ENTRIES:
        score = 0
        if any(kw in q or q in kw for kw in e["keywords"]):
            score += 2
        if q in e["title"].lower():
            score += 3
        if q in e["content"].lower():
            score += 1
        if score > 0:
            results.append((score, e))
    results.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in results]


# ── request model ─────────────────────────────────────────────────────────────

class QueryRequest(BaseModel):
    query: str


# ── chat endpoint ─────────────────────────────────────────────────────────────

@app.post("/chat")
def chat(req: QueryRequest):
    """
    Main chatbot endpoint.
    1. Check if this is a Pokemon-specific query first.
    2. Otherwise, LLM selects relevant KB entries and writes a grounded answer.
    """
    # Fast path: Pokemon spawn queries
    if _is_pokemon_query(req.query):
        answer = _answer_pokemon_query(req.query)
        if answer:
            return {
                "answer": answer,
                "section": "pokemon_spawns",
                "matched_entries": ["Pokemon Spawn Database"],
            }

    # Step 1: LLM-based routing
    entries = _select_entries_with_llm(req.query)

    # Fallback to keyword search if LLM returned nothing
    if not entries:
        entries = _keyword_search(req.query)[:2]

    if not entries:
        return {
            "answer": (
                "I couldn't find anything relevant in the wiki for that question. "
                "Try asking about installing COBBLEVERSE, setting up a server, "
                "gameplay features, or where to find a specific Pokemon."
            ),
            "section": "unknown",
            "matched_entries": [],
        }

    # Step 2: LLM-based answer generation
    answer = _answer_with_llm(req.query, entries)
    sections = list({e["section"] for e in entries})

    return {
        "answer": answer,
        "section": sections[0] if len(sections) == 1 else ", ".join(sections),
        "matched_entries": [e["title"] for e in entries],
    }


@app.post("/chat/stream")
def chat_stream(req: QueryRequest):
    """
    Streaming version of /chat — sends the LLM answer token by token
    as a Server-Sent Events stream.
    """
    # Fast path: Pokemon spawn queries (streamed)
    if _is_pokemon_query(req.query):
        stream = _answer_pokemon_query_stream(req.query)
        if stream is not None:
            def _pokemon_stream():
                for chunk in stream:
                    delta = chunk["message"]["content"]
                    if delta:
                        yield f"data: {json.dumps(delta)}\n\n"
                yield "data: [DONE]\n\n"
            return StreamingResponse(_pokemon_stream(), media_type="text/event-stream")

    # Step 1: LLM routing (non-streaming, fast)
    entries = _select_entries_with_llm(req.query)
    if not entries:
        entries = _keyword_search(req.query)[:2]

    if not entries:
        def _no_match():
            yield "data: I couldn't find anything relevant for that question.\n\n"
            yield "data: [DONE]\n\n"
        return StreamingResponse(_no_match(), media_type="text/event-stream")

    # Step 2: stream the LLM answer
    def _generate():
        for chunk in _answer_with_llm_stream(req.query, entries):
            # SSE format
            yield f"data: {json.dumps(chunk)}\n\n"
        yield "data: [DONE]\n\n"

    return StreamingResponse(_generate(), media_type="text/event-stream")


# ── MCP tool endpoints (for direct tool access) ───────────────────────────────

@app.get("/tools")
def list_tools():
    return {
        "tools": [
            {"name": "search_installation", "description": "Search the INSTALLATION knowledge base"},
            {"name": "get_installation_topics", "description": "List all INSTALLATION topics"},
        ]
    }


@app.post("/tools/search_installation")
def search_installation(req: QueryRequest):
    results = _keyword_search(req.query)
    if not results:
        results = list(INSTALLATION.values())
    answer = "\n\n---\n\n".join(
        f"**{e['title']}**\n\n{e['content']}\n\nSource: {e['url']}" for e in results[:3]
    )
    return {"result": answer, "section": "installation"}


@app.get("/tools/get_installation_topics")
def get_installation_topics():
    return {"topics": [{"key": k, "title": v["title"]} for k, v in INSTALLATION.items()]}


@app.post("/tools/search_pokemon")
def api_search_pokemon(req: QueryRequest):
    """Search the Pokemon spawn database directly."""
    results = search_pokemon(req.query)
    if not results:
        return {"results": [], "count": 0, "query": req.query}
    formatted = [format_pokemon(p) for p in results[:10]]
    return {"results": formatted, "count": len(results), "query": req.query}


# ── serve web client ──────────────────────────────────────────────────────────

WEB_DIR = os.path.join(os.path.dirname(__file__), "..", "web_client")

if os.path.isdir(WEB_DIR):
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

    @app.get("/")
    def serve_index():
        return FileResponse(os.path.join(WEB_DIR, "index.html"))


if __name__ == "__main__":
    print(f"COBBLEVERSE Wiki MCP Server (LLM: {LLM_MODEL}) → http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

