"""
COBBLEVERSE MCP Server
Exposes the INSTALLATION knowledge base via MCP tools.
Run with: python mcp_server/server.py
"""

from mcp.server.fastmcp import FastMCP
from knowledge_base import INSTALLATION

mcp = FastMCP("cobbleverse-wiki")


def _search(kb: dict, query: str) -> list[dict]:
    """Return entries whose keywords or title match the query."""
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


# ── INSTALLATION TOOLS ────────────────────────────────────────────────────────

@mcp.tool()
def search_installation(query: str) -> str:
    """
    Search the INSTALLATION knowledge base for answers about installing
    COBBLEVERSE (Modrinth, CurseForge, Apex Hosting, Nitrado, LumyMon).

    Args:
        query: The user's question or keywords, e.g. 'install modrinth'
    """
    results = _search(INSTALLATION, query)
    if not results:
        # Return all entries as a fallback
        results = list(INSTALLATION.values())

    parts = []
    for entry in results[:3]:
        parts.append(f"## {entry['title']}\n{entry['content']}\nSource: {entry['url']}")
    return "\n\n---\n\n".join(parts)


@mcp.tool()
def get_installation_topics() -> str:
    """
    List all available INSTALLATION topics in the knowledge base.
    """
    lines = ["Available INSTALLATION topics:\n"]
    for key, entry in INSTALLATION.items():
        lines.append(f"- {entry['title']}")
    return "\n".join(lines)


@mcp.tool()
def get_installation_entry(topic_key: str) -> str:
    """
    Retrieve a specific INSTALLATION entry by its key.

    Args:
        topic_key: One of: install_modrinth, install_curseforge, server_apex,
                   server_apex_update, server_nitrado, lumymon
    """
    entry = INSTALLATION.get(topic_key)
    if not entry:
        available = ", ".join(INSTALLATION.keys())
        return f"Topic '{topic_key}' not found. Available keys: {available}"
    return f"## {entry['title']}\n\n{entry['content']}\n\nSource: {entry['url']}"


if __name__ == "__main__":
    mcp.run(transport="stdio")

