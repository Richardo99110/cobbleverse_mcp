"""
HTTP bridge — exposes the MCP tools over a simple REST API so the
web chatbot can call them without needing a native MCP client.

Run with:  python mcp_server/http_server.py
Serves on: http://localhost:8000
"""

import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pydantic import BaseModel
import uvicorn

from knowledge_base import INSTALLATION

app = FastAPI(title="COBBLEVERSE Wiki API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# ── helpers ───────────────────────────────────────────────────────────────────

def _search(kb: dict, query: str) -> list[dict]:
    q = query.lower()
    results = []
    for entry in kb.values():
        score = 0
        if any(kw in q or q in kw for kw in entry["keywords"]):
            score += 2
        if q in entry["title"].lower():
            score += 3
        if q in entry["content"].lower():
            score += 1
        if score > 0:
            results.append((score, entry))
    results.sort(key=lambda x: x[0], reverse=True)
    return [e for _, e in results]


def _format_entry(entry: dict) -> str:
    return f"**{entry['title']}**\n\n{entry['content']}\n\n*Source: {entry['url']}*"


# ── MCP-style tool endpoints ──────────────────────────────────────────────────

class QueryRequest(BaseModel):
    query: str


@app.get("/tools")
def list_tools():
    """List all available MCP tools."""
    return {
        "tools": [
            {
                "name": "search_installation",
                "description": "Search the INSTALLATION knowledge base",
                "section": "installation",
            },
            {
                "name": "get_installation_topics",
                "description": "List all INSTALLATION topics",
                "section": "installation",
            },
        ]
    }


@app.post("/tools/search_installation")
def search_installation(req: QueryRequest):
    """Search INSTALLATION knowledge base."""
    results = _search(INSTALLATION, req.query)
    if not results:
        results = list(INSTALLATION.values())
    answer = "\n\n---\n\n".join(_format_entry(e) for e in results[:3])
    return {"result": answer, "section": "installation", "matches": len(results)}


@app.get("/tools/get_installation_topics")
def get_installation_topics():
    """Return all INSTALLATION topic titles."""
    topics = [{"key": k, "title": v["title"]} for k, v in INSTALLATION.items()]
    return {"topics": topics, "section": "installation"}


@app.get("/tools/get_installation_entry/{topic_key}")
def get_installation_entry(topic_key: str):
    """Return a specific INSTALLATION entry."""
    entry = INSTALLATION.get(topic_key)
    if not entry:
        return {"error": f"Key '{topic_key}' not found", "available": list(INSTALLATION.keys())}
    return {"result": _format_entry(entry), "section": "installation"}


# ── chat endpoint (used by the web chatbot) ───────────────────────────────────

SECTION_MAP = {
    "installation": INSTALLATION,
}

SECTION_KEYWORDS = {
    "installation": ["install", "modrinth", "curseforge", "apex", "nitrado", "lumymon",
                     "server", "download", "launcher", "setup", "ram", "memory", "update"],
}


def _detect_section(query: str) -> str:
    q = query.lower()
    scores = {}
    for section, keywords in SECTION_KEYWORDS.items():
        scores[section] = sum(1 for kw in keywords if kw in q)
    best = max(scores, key=scores.get)
    return best if scores[best] > 0 else "installation"


@app.post("/chat")
def chat(req: QueryRequest):
    """
    Main chatbot endpoint. Detects the relevant section and searches it.
    Returns a markdown-formatted answer.
    """
    section = _detect_section(req.query)
    kb = SECTION_MAP.get(section, INSTALLATION)
    results = _search(kb, req.query)

    if not results:
        return {
            "answer": (
                "I couldn't find a specific answer for that. "
                "Try asking about installing COBBLEVERSE from Modrinth or CurseForge, "
                "setting up a server on Apex or Nitrado, or about LumyMon."
            ),
            "section": section,
        }

    answer = "\n\n---\n\n".join(_format_entry(e) for e in results[:2])
    return {"answer": answer, "section": section}


# ── serve web client ──────────────────────────────────────────────────────────

WEB_DIR = os.path.join(os.path.dirname(__file__), "..", "web_client")

if os.path.isdir(WEB_DIR):
    app.mount("/static", StaticFiles(directory=WEB_DIR), name="static")

    @app.get("/")
    def serve_index():
        return FileResponse(os.path.join(WEB_DIR, "index.html"))


if __name__ == "__main__":
    print("COBBLEVERSE Wiki MCP Server running at http://localhost:8000")
    uvicorn.run(app, host="0.0.0.0", port=8000)

