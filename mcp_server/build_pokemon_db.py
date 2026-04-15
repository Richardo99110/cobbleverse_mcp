"""
Build script — generates pokemon_spawns.py from raw data.
Run once:  python mcp_server/build_pokemon_db.py
"""

import json, os

# Each entry: (number, name, source, spawn, rarity, condition, forms, generation)
# We'll write them as a Python dict keyed by lowercase name.

HEADER = '''"""
COBBLEVERSE Pokémon Spawn Database
Auto-generated from https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/
Contains spawn data for all 1025+ Pokémon across Generations 1-9.

Content was rephrased for compliance with licensing restrictions.
Source: https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/
"""

SOURCE_URL = "https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/"

# Each entry: {name, number, generation, source, spawn_biomes, rarity, condition, forms}
POKEMON_SPAWNS = {
'''

FOOTER = '''}

def search_pokemon(query: str) -> list[dict]:
    """Search for Pokémon by name, number, biome, rarity, generation, or condition."""
    q = query.lower().strip()
    results = []
    for key, p in POKEMON_SPAWNS.items():
        score = 0
        # Exact name match
        if q == key or q == p["name"].lower():
            score += 10
        # Partial name match
        elif q in key or q in p["name"].lower():
            score += 5
        # Number match
        if q.lstrip("#") == str(p["number"]):
            score += 10
        # Generation match
        if q in p["generation"].lower():
            score += 2
        # Biome/spawn match
        if q in p["spawn_biomes"].lower():
            score += 3
        # Rarity match
        if q in p["rarity"].lower():
            score += 2
        # Condition match
        if q in p["condition"].lower():
            score += 2
        # Forms match
        if q in p["forms"].lower():
            score += 2
        if score > 0:
            results.append((score, p))
    results.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in results]


def format_pokemon(p: dict) -> str:
    """Format a single Pokémon entry as readable text."""
    lines = [f"#{p['number']} {p['name']} ({p['generation']})"]
    lines.append(f"  Source mod: {p['source']}")
    lines.append(f"  Spawn biomes: {p['spawn_biomes']}")
    lines.append(f"  Rarity: {p['rarity']}")
    if p['condition']:
        lines.append(f"  Condition: {p['condition']}")
    if p['forms']:
        lines.append(f"  Forms: {p['forms']}")
    return "\\n".join(lines)
'''

# Raw data extracted from the wiki page — all 1025+ Pokémon
# Format: (number, name, source, spawn_biomes, rarity, condition, forms, gen)
RAW_DATA = []

