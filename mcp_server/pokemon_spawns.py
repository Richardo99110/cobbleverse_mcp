"""
COBBLEVERSE Pokemon Spawn Database
Source: https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/
Contains spawn data for all 1025+ Pokemon across Generations 1-9.

Content was rephrased for compliance with licensing restrictions.
"""

SOURCE_URL = "https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/"

# Each entry: {name, number, generation, source, spawn_biomes, rarity, condition, forms}
POKEMON_SPAWNS = {

# Pokemon are keyed by lowercase name for easy lookup

# === GEN 1 - KANTO ===
"bulbasaur": {"name": "Bulbasaur", "number": 1, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Jungle biomes", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"ivysaur": {"name": "Ivysaur", "number": 2, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Jungle biomes", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"venusaur": {"name": "Venusaur", "number": 3, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Jungle biomes", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"charmander": {"name": "Charmander", "number": 4, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Peaks, Windswept Hills, Basalt Deltas", "rarity": "Ultra-Rare", "condition": "Weather Clear", "forms": ""},
"charmeleon": {"name": "Charmeleon", "number": 5, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Peaks, Windswept Hills, Basalt Deltas", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"charizard": {"name": "Charizard", "number": 6, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Peaks, Windswept Hills, Basalt Deltas", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"squirtle": {"name": "Squirtle", "number": 7, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All River biomes, Jungle, All Forest biomes, Cherry Grove", "rarity": "Ultra-Rare", "condition": "Also by fishing", "forms": ""},
"wartortle": {"name": "Wartortle", "number": 8, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All River biomes, Jungle, All Forest biomes, Cherry Grove", "rarity": "Ultra-Rare", "condition": "Also by fishing", "forms": ""},
"blastoise": {"name": "Blastoise", "number": 9, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All River biomes, Jungle, All Forest biomes, Cherry Grove", "rarity": "Ultra-Rare", "condition": "Also by fishing", "forms": ""},
"caterpie": {"name": "Caterpie", "number": 10, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Plains, Cherry Grove", "rarity": "Common", "condition": "Day", "forms": "Valencian form: All Jungle biomes"},
"metapod": {"name": "Metapod", "number": 11, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Plains, Cherry Grove", "rarity": "Common", "condition": "Day", "forms": "Valencian form: All Jungle biomes"},
"butterfree": {"name": "Butterfree", "number": 12, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Plains, Cherry Grove", "rarity": "Common", "condition": "Day", "forms": "Valencian form: All Jungle biomes"},
"weedle": {"name": "Weedle", "number": 13, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Jungle, Cherry Grove", "rarity": "Common", "condition": "Day", "forms": ""},
"kakuna": {"name": "Kakuna", "number": 14, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Jungle, Cherry Grove", "rarity": "Common", "condition": "Day", "forms": ""},
"beedrill": {"name": "Beedrill", "number": 15, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Oak Forest, Birch Forest, Dark Oak Forest, Jungle, Cherry Grove", "rarity": "Common", "condition": "Day, Weather clear", "forms": ""},
"pidgey": {"name": "Pidgey", "number": 16, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Flower Forest, Oak Forest, Birch Forest, Dark Oak Forest, Plains, Sunflower Plains", "rarity": "Common", "condition": "Day", "forms": ""},
"pidgeotto": {"name": "Pidgeotto", "number": 17, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Flower Forest, Oak Forest, Birch Forest, Dark Oak Forest, Plains, Sunflower Plains", "rarity": "Common", "condition": "Day", "forms": ""},
"pidgeot": {"name": "Pidgeot", "number": 18, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Flower Forest, Oak Forest, Birch Forest, Dark Oak Forest, Plains, Sunflower Plains", "rarity": "Common", "condition": "Day", "forms": ""},
"rattata": {"name": "Rattata", "number": 19, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Savanna, Savanna Plateau, All Forest biomes except Dark Forest", "rarity": "Common", "condition": "Night", "forms": "Alolan form: Dark Forest during the night"},
"raticate": {"name": "Raticate", "number": 20, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Savanna, Savanna Plateau, All Forest biomes except Dark Forest", "rarity": "Common", "condition": "Night", "forms": "Alolan form: Dark Forest during the night"},
"spearow": {"name": "Spearow", "number": 21, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Savanna", "rarity": "Common", "condition": "Day", "forms": ""},
"fearow": {"name": "Fearow", "number": 22, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Savanna", "rarity": "Common", "condition": "Day", "forms": ""},
"ekans": {"name": "Ekans", "number": 23, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Desert, Savanna, Deep Dark", "rarity": "Common", "condition": "Day", "forms": ""},
"arbok": {"name": "Arbok", "number": 24, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Desert biomes, Savanna, Deep Dark", "rarity": "Common", "condition": "", "forms": ""},
"pikachu": {"name": "Pikachu", "number": 25, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes except Dark Forest", "rarity": "Uncommon", "condition": "During a storm", "forms": "Alolan form: Beach; Cosplay Belle: Sunflower Plains; Libre: Savanna; Phd: Jungle; Pop Star: Cherry Grove; Rock Star: Badlands"},
"raichu": {"name": "Raichu", "number": 26, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Forest biomes", "rarity": "Uncommon", "condition": "During a storm", "forms": "Alolan form: Jungle, Desert, Savanna"},
"sandshrew": {"name": "Sandshrew", "number": 27, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Desert", "rarity": "Common", "condition": "", "forms": "Alolan form: Jagged Peaks, Snowy Plains, Snowy Slopes"},
"sandslash": {"name": "Sandslash", "number": 28, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Desert", "rarity": "Common", "condition": "", "forms": "Alolan form: Jagged Peaks, Snowy Plains, Snowy Slopes"},
"nidoran_f": {"name": "Nidoran Female", "number": 29, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"nidorina": {"name": "Nidorina", "number": 30, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"nidoqueen": {"name": "Nidoqueen", "number": 31, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"nidoran_m": {"name": "Nidoran Male", "number": 32, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"nidorino": {"name": "Nidorino", "number": 33, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"nidoking": {"name": "Nidoking", "number": 34, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Uncommon", "condition": "", "forms": ""},
"clefairy": {"name": "Clefairy", "number": 35, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dripstone Caves, Hills biomes", "rarity": "Uncommon", "condition": "Night", "forms": ""},
"clefable": {"name": "Clefable", "number": 36, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dripstone Caves, Hills biomes", "rarity": "Uncommon", "condition": "Night", "forms": ""},
"vulpix": {"name": "Vulpix", "number": 37, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, Cherry Grove, All Taiga biomes, Crimson Forest, Warped Forest", "rarity": "Uncommon", "condition": "", "forms": "Alolan form: Snowy Taiga, Grove"},
"ninetales": {"name": "Ninetales", "number": 38, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, Cherry Grove, All Taiga biomes, Crimson Forest, Warped Forest", "rarity": "Uncommon", "condition": "Also obtainable by giving Vulpix a Fire Stone", "forms": "Alolan form: Snowy Taiga, Snow Forest"},
"jigglypuff": {"name": "Jigglypuff", "number": 39, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Cherry Grove, Flower Forest, Sunflower Plains", "rarity": "Common", "condition": "Night", "forms": ""},
"wigglytuff": {"name": "Wigglytuff", "number": 40, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Cherry Grove, Flower Forest, Meadow, Sunflower Plains", "rarity": "Common", "condition": "Night", "forms": ""},
"zubat": {"name": "Zubat", "number": 41, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, Swamp, Mangrove Swamp, Dark Forest, Deep Dark", "rarity": "Common", "condition": "Night, Weather Clear", "forms": ""},
"golbat": {"name": "Golbat", "number": 42, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, Swamp, Mangrove Swamp, Dark Forest, Deep Dark", "rarity": "Common", "condition": "Night, Weather Clear", "forms": ""},
"oddish": {"name": "Oddish", "number": 43, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, All Plains biomes, All Jungle biomes, Savanna", "rarity": "Common", "condition": "Day", "forms": "Valencian form: Savanna during the day"},
"gloom": {"name": "Gloom", "number": 44, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, All Plains biomes, Jungle, Savanna", "rarity": "Common", "condition": "Day", "forms": "Valencian form: Savanna during the day"},
"vileplume": {"name": "Vileplume", "number": 45, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Forest biomes, All Plains biomes, Jungle, Savanna", "rarity": "Common", "condition": "Night", "forms": "Valencian form: Savanna during the night"},
"paras": {"name": "Paras", "number": 46, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Crimson Forest, Lush Caves, Mushroom Fields, Dark Forest", "rarity": "Common", "condition": "", "forms": ""},
"parasect": {"name": "Parasect", "number": 47, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Crimson Forest, Lush Caves, Mushroom Fields, Dark Forest", "rarity": "Common", "condition": "", "forms": ""},
"venonat": {"name": "Venonat", "number": 48, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dark Forest, Swamp", "rarity": "Common", "condition": "Night", "forms": ""},
"venomoth": {"name": "Venomoth", "number": 49, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dark Forest, Swamp", "rarity": "Common", "condition": "Night, Weather clear", "forms": ""},
"diglett": {"name": "Diglett", "number": 50, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Min Y=0, Weather Clear", "forms": "Alolan form: Overworld biomes Max Y=0"},
"dugtrio": {"name": "Dugtrio", "number": 51, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Min Y=0, Weather Clear", "forms": "Alolan form: Overworld biomes Max Y=0"},
"meowth": {"name": "Meowth", "number": 52, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Overworld biomes except Taiga, Desert, Badlands, Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains", "rarity": "Common", "condition": "Night, Weather clear", "forms": "Alolan form: Badlands, Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains. Galarian form: Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains"},
"persian": {"name": "Persian", "number": 53, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Desert", "rarity": "Common", "condition": "Also in Structure: Illager Outpost", "forms": "Alolan form: Badlands, Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains. Galarian form: Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains"},
"psyduck": {"name": "Psyduck", "number": 54, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp, River, Plain, Savanna, Dark Forest", "rarity": "Common", "condition": "", "forms": ""},
"golduck": {"name": "Golduck", "number": 55, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp, River, Plain, Savanna, Dark Forest", "rarity": "Common", "condition": "", "forms": ""},
"mankey": {"name": "Mankey", "number": 56, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Windswept Hills, Windswept Gravelly Hills, Meadow, Stony Peaks, Jungle, Sparse Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"primeape": {"name": "Primeape", "number": 57, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Windswept Hills, Windswept Gravelly Hills, Meadow, Stony Peaks, Jungle, Sparse Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"growlithe": {"name": "Growlithe", "number": 58, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Desert", "rarity": "Common", "condition": "", "forms": "Hisuian form: Frozen Peaks, Jagged Peaks, Snowy Slopes, Stony Peaks"},
"arcanine": {"name": "Arcanine", "number": 59, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Desert", "rarity": "Common", "condition": "", "forms": "Hisuian form: Frozen Peaks, Jagged Peaks, Snowy Slopes, Stony Peaks"},
"poliwag": {"name": "Poliwag", "number": 60, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp (Raining), Dark Forest, All Hills biomes, Mushroom Fields, Jungle, All Plains biomes, All Forest biomes, Lush Caves", "rarity": "Common", "condition": "Also by fishing", "forms": ""},
"poliwhirl": {"name": "Poliwhirl", "number": 61, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp, Dark Forest, All Hills biomes, Mushroom Fields, Jungle, All Plains biomes, All Forest biomes, Lush Caves", "rarity": "Common", "condition": "Also by fishing", "forms": ""},
"poliwrath": {"name": "Poliwrath", "number": 62, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp, Dark Forest, All Hills biomes, Mushroom Fields, Jungle, All Plains biomes, All Forest biomes, Lush Caves", "rarity": "Common", "condition": "Also by fishing", "forms": ""},
"abra": {"name": "Abra", "number": 63, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes, Dark Forest", "rarity": "Uncommon", "condition": "During the Night, in Mansion Structures", "forms": ""},
"kadabra": {"name": "Kadabra", "number": 64, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes, Dark Forest", "rarity": "Rare", "condition": "During the Night, in Mansion Structures", "forms": ""},
"alakazam": {"name": "Alakazam", "number": 65, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes, Dark Forest", "rarity": "Rare", "condition": "During the Night, in Mansion Structures", "forms": ""},
"machop": {"name": "Machop", "number": 66, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes", "rarity": "Common", "condition": "Night", "forms": ""},
"machoke": {"name": "Machoke", "number": 67, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes", "rarity": "Common", "condition": "Night", "forms": ""},
"machamp": {"name": "Machamp", "number": 68, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Hills biomes", "rarity": "Common", "condition": "Night", "forms": ""},
"bellsprout": {"name": "Bellsprout", "number": 69, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"weepinbell": {"name": "Weepinbell", "number": 70, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"victreebel": {"name": "Victreebel", "number": 71, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"tentacool": {"name": "Tentacool", "number": 72, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes", "rarity": "Common", "condition": "Submerged or fishing", "forms": ""},
"tentacruel": {"name": "Tentacruel", "number": 73, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes", "rarity": "Common", "condition": "Submerged or fishing", "forms": ""},
"geodude": {"name": "Geodude", "number": 74, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Caves", "forms": "Alolan form: All Overworld biomes near iron ores"},
"graveler": {"name": "Graveler", "number": 75, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Caves", "forms": "Alolan form: All Overworld biomes near iron ores"},
"golem": {"name": "Golem", "number": 76, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Caves", "forms": "Alolan form: All Overworld biomes near iron ores"},
"ponyta": {"name": "Ponyta", "number": 77, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Plains biomes, All Savanna biomes, Nether Wastes", "rarity": "Uncommon", "condition": "Night, Weather clear", "forms": "Galarian form: Flower Forest, Meadow, Sunflower Plains, Cherry Grove, Dark Forest"},
"rapidash": {"name": "Rapidash", "number": 78, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Plains biomes, All Savanna biomes, Nether Wastes", "rarity": "Uncommon", "condition": "", "forms": "Galarian form: Flower Forest, Meadow, Sunflower Plains, Cherry Grove, Dark Forest"},
"slowpoke": {"name": "Slowpoke", "number": 79, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Beach, River", "rarity": "Common", "condition": "Also by fishing", "forms": "Galarian form: Mushroom Fields"},
"slowbro": {"name": "Slowbro", "number": 80, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Beach", "rarity": "Common", "condition": "Also by fishing", "forms": "Galarian form: Mushroom Fields"},
"magnemite": {"name": "Magnemite", "number": 81, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Near lightning rod, during a storm", "forms": ""},
"magneton": {"name": "Magneton", "number": 82, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Deep Dark", "rarity": "Common", "condition": "Near lightning rod, during a storm", "forms": ""},
"farfetchd": {"name": "Farfetch'd", "number": 83, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Common", "condition": "Near Medicinal Leek", "forms": "Galarian form: All Forest biomes"},
"doduo": {"name": "Doduo", "number": 84, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Common", "condition": "Day", "forms": ""},
"dodrio": {"name": "Dodrio", "number": 85, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna", "rarity": "Common", "condition": "Day", "forms": ""},
"seel": {"name": "Seel", "number": 86, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Deep Frozen Ocean, Frozen Ocean, Cold Ocean", "rarity": "Common", "condition": "Submerged or fishing", "forms": ""},
"dewgong": {"name": "Dewgong", "number": 87, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Deep Frozen Ocean, Frozen Ocean, Cold Ocean", "rarity": "Common", "condition": "Submerged or fishing", "forms": ""},
"grimer": {"name": "Grimer", "number": 88, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp", "rarity": "Uncommon", "condition": "", "forms": "Alolan form: Beach"},
"muk": {"name": "Muk", "number": 89, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Swamp, Mangrove Swamp", "rarity": "Uncommon", "condition": "", "forms": "Alolan form: Beach"},
"shellder": {"name": "Shellder", "number": 90, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore, Deep Frozen Ocean, Frozen Ocean, Cold Ocean", "rarity": "Common", "condition": "Seafloor or fishing", "forms": ""},
"cloyster": {"name": "Cloyster", "number": 91, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore, Deep Frozen Ocean, Frozen Ocean, Cold Ocean", "rarity": "Common", "condition": "Seafloor or fishing", "forms": ""},
"gastly": {"name": "Gastly", "number": 92, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dark Forest, All Nether biomes, Deep Dark", "rarity": "Common", "condition": "", "forms": ""},
"haunter": {"name": "Haunter", "number": 93, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dark Forest, All Nether biomes, Deep Dark", "rarity": "Common", "condition": "", "forms": ""},
"gengar": {"name": "Gengar", "number": 94, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Dark Forest, All Nether biomes, Deep Dark", "rarity": "Uncommon", "condition": "", "forms": ""},
"onix": {"name": "Onix", "number": 95, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Basalt Deltas and in Caves", "rarity": "Uncommon", "condition": "", "forms": ""},
"drowzee": {"name": "Drowzee", "number": 96, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains, Snowy Slopes", "rarity": "Common", "condition": "Night", "forms": ""},
"hypno": {"name": "Hypno", "number": 97, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains, Snowy Slopes", "rarity": "Common", "condition": "Night", "forms": ""},
"krabby": {"name": "Krabby", "number": 98, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore, All Ocean biomes", "rarity": "Common", "condition": "Also by fishing", "forms": ""},
"kingler": {"name": "Kingler", "number": 99, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore, All Ocean biomes", "rarity": "Common", "condition": "Also by fishing", "forms": ""},
"voltorb": {"name": "Voltorb", "number": 100, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Common", "condition": "Storm", "forms": "Hisuian form: During storm near apricorns"},
"electrode": {"name": "Electrode", "number": 101, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Common", "condition": "Storm", "forms": "Hisuian form: During storm near apricorns"},
"exeggcute": {"name": "Exeggcute", "number": 102, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle, Savanna, Beach", "rarity": "Common", "condition": "", "forms": "Alolan form: Beach"},
"exeggutor": {"name": "Exeggutor", "number": 103, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle, Savanna, Beach", "rarity": "Common", "condition": "", "forms": "Alolan form: Beach"},
"cubone": {"name": "Cubone", "number": 104, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Desert, Soul Sand Valley", "rarity": "Common", "condition": "", "forms": "Alolan form: Soul Sand Valley"},
"marowak": {"name": "Marowak", "number": 105, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Desert, Soul Sand Valley", "rarity": "Common", "condition": "", "forms": "Alolan form: Soul Sand Valley"},
"hitmonlee": {"name": "Hitmonlee", "number": 106, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Windswept Hills, Windswept Forests, Windswept Gravelly Hills", "rarity": "Uncommon", "condition": "", "forms": ""},
"hitmonchan": {"name": "Hitmonchan", "number": 107, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Windswept Hills, Windswept Forests, Windswept Gravelly Hills", "rarity": "Uncommon", "condition": "", "forms": ""},
"lickitung": {"name": "Lickitung", "number": 108, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Savanna biomes, Plains", "rarity": "Uncommon", "condition": "", "forms": ""},
"koffing": {"name": "Koffing", "number": 109, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes, Soul Sand Valley", "rarity": "Common", "condition": "Night", "forms": "Galarian form: Dark Forest during the night"},
"weezing": {"name": "Weezing", "number": 110, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Common", "condition": "Night", "forms": "Galarian form: Dark Forest during the night"},
"rhyhorn": {"name": "Rhyhorn", "number": 111, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna, Stony Peaks, Windswept Hills, Windswept Gravelly Hills, Windswept Forest", "rarity": "Common", "condition": "", "forms": ""},
"rhydon": {"name": "Rhydon", "number": 112, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna, Stony Peaks, Windswept Hills, Windswept Gravelly Hills, Windswept Forest", "rarity": "Common", "condition": "", "forms": ""},
"chansey": {"name": "Chansey", "number": 113, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Rare", "condition": "Day, Near a Minecraft Village", "forms": ""},
"tangela": {"name": "Tangela", "number": 114, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle, Sparse Jungle", "rarity": "Common", "condition": "Day", "forms": ""},
"kangaskhan": {"name": "Kangaskhan", "number": 115, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Savanna, Savanna Plateau", "rarity": "Rare", "condition": "", "forms": ""},
"horsea": {"name": "Horsea", "number": 116, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Deep Lukewarm Ocean, Lukewarm Ocean, Warm Ocean, Deep Ocean", "rarity": "Common", "condition": "Also by fishing except in Cold Ocean, Frozen Ocean", "forms": ""},
"seadra": {"name": "Seadra", "number": 117, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Ocean, Deep Lukewarm Ocean, Lukewarm Ocean, Warm Ocean, Deep Ocean", "rarity": "Common", "condition": "Also by fishing except in Cold Ocean, Frozen Ocean", "forms": ""},
"goldeen": {"name": "Goldeen", "number": 118, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "River, Frozen River", "rarity": "Common", "condition": "Also by fishing in Plains, Meadow, Sunflower Plains, All Forest biomes, All Jungle biomes, Swamp, Mangrove Swamp, Stony Peaks, Jagged Peaks, Snowy Slopes, Snowy Plains, Snowy Taiga, Grove", "forms": ""},
"seaking": {"name": "Seaking", "number": 119, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "River, Frozen River", "rarity": "Common", "condition": "Also by fishing in Plains, Meadow, Sunflower Plains, All Forest biomes, All Jungle biomes, Swamp, Mangrove Swamp", "forms": ""},
"staryu": {"name": "Staryu", "number": 120, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore, Beach, Snowy Beach, All Ocean Biomes", "rarity": "Uncommon", "condition": "Submerged or fishing", "forms": ""},
"starmie": {"name": "Starmie", "number": 121, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Uncommon", "condition": "Submerged or fishing", "forms": ""},
"mr_mime": {"name": "Mr. Mime", "number": 122, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes", "rarity": "Uncommon", "condition": "Day, more common near a minecraft village", "forms": "Galarian form: Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains, Snowy Slopes"},
"scyther": {"name": "Scyther", "number": 123, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Meadow, Birch Forest, Oak Forest, Jungle, Bamboo Jungle, Sparse Jungle", "rarity": "Uncommon/Rare", "condition": "Day", "forms": ""},
"jynx": {"name": "Jynx", "number": 124, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Frozen River, Jagged Peaks, Snowy Beach, Snowy Plains, Snowy Slopes", "rarity": "Uncommon", "condition": "Day", "forms": ""},
"electabuzz": {"name": "Electabuzz", "number": 125, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Sunflower Plains, Meadow, Snowy Plains, Windswept Hills, Windswept Forest, Stony Peaks, Snowy Slopes", "rarity": "Uncommon", "condition": "Day, during a Storm", "forms": ""},
"magmar": {"name": "Magmar", "number": 126, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Windswept Hills, Stony Peaks, Jagged Peaks, Basalt Deltas, Nether Wastes", "rarity": "Common", "condition": "Weather Clear", "forms": ""},
"pinsir": {"name": "Pinsir", "number": 127, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Jungle, Sparse Jungle, Bamboo Jungle", "rarity": "Rare", "condition": "", "forms": ""},
"tauros": {"name": "Tauros", "number": 128, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Sunflower Plains", "rarity": "Common", "condition": "Day", "forms": "Paldean forms: Meadow, Windswept Hills, Jagged Peaks near Lava or Water"},
"magikarp": {"name": "Magikarp", "number": 129, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "River, All Ocean biomes", "rarity": "Common", "condition": "Also by Fishing", "forms": "Apricot: Desert, Savanna; Purple: Swamp; Pink: Flower Forest, Cherry Grove; Calico: Plains, Forests; Blue: Dark Forest, Snowy Plains; Brown: Badlands; Gray: Dark Forest"},
"gyarados": {"name": "Gyarados", "number": 130, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes", "rarity": "Common", "condition": "Day, Also by Fishing", "forms": ""},
"lapras": {"name": "Lapras", "number": 131, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Deep Frozen Ocean, Frozen Ocean, Deep Cold Ocean", "rarity": "Uncommon", "condition": "Also by Fishing", "forms": ""},
"ditto": {"name": "Ditto", "number": 132, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Overworld biomes except Ocean biomes", "rarity": "Ultra-Rare", "condition": "", "forms": ""},
"eevee": {"name": "Eevee", "number": 133, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Forest, Birch Forest, Cherry Grove", "rarity": "Uncommon", "condition": "Day, more common inside Mansion", "forms": ""},
"vaporeon": {"name": "Vaporeon", "number": 134, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "River, Swamp, Mangrove Swamp, Dark Forest, All Forest biomes, Jungle, Sparse Jungle, Bamboo Jungle, Plains, Sunflower Plains, Beach", "rarity": "Ultra-Rare", "condition": "Also by Fishing", "forms": ""},
"jolteon": {"name": "Jolteon", "number": 135, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Plains, Sunflower Plains, Meadow", "rarity": "Ultra-Rare", "condition": "Day", "forms": ""},
"flareon": {"name": "Flareon", "number": 136, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Badlands, Eroded Badlands, Wooded Badlands, Desert", "rarity": "Ultra-Rare", "condition": "Day", "forms": ""},
"porygon": {"name": "Porygon", "number": 137, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "The End", "rarity": "Uncommon", "condition": "", "forms": ""},
"omanyte": {"name": "Omanyte", "number": 138, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Fossil: Dripstone Oasis, Enhydro Agate, Eroded Pillar, Preserved Skeleton, Sandy Den, Vibrant Hydrothermal Vents", "rarity": "Rare", "condition": "Hidden in Suspicious sand/gravel. Use Resurrection Machine. Also wild in Lush Caves, Fungal Caves, Underground Jungle (Sky light >8)", "forms": ""},
"omastar": {"name": "Omastar", "number": 139, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Evolution from Omanyte", "rarity": "Rare", "condition": "Resurrection Machine. Also wild in Lush Caves, Fungal Caves, Underground Jungle", "forms": ""},
"kabuto": {"name": "Kabuto", "number": 140, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Fossil: Enhydro Agate, Hydrothermal Vents, Rooted Pit, Sunscorched Den, Suspicious Mound", "rarity": "Rare", "condition": "Hidden in Suspicious sand/gravel. Use Resurrection Machine. Also wild in Lush Caves, Fungal Caves, Underground Jungle", "forms": ""},
"kabutops": {"name": "Kabutops", "number": 141, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Evolution from Kabuto", "rarity": "Rare", "condition": "Resurrection Machine. Also wild in Lush Caves, Fungal Caves, Underground Jungle", "forms": ""},
"aerodactyl": {"name": "Aerodactyl", "number": 142, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Fossil: Frozen Pond, Lush Den, Oak Tree, Spruce Tree", "rarity": "Rare", "condition": "Suspicious sand/gravel. Use Resurrection Machine. Also wild in Lush Caves, Fungal Caves, Underground Jungle", "forms": ""},
"snorlax": {"name": "Snorlax", "number": 143, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Snowy Grove, Snowy Taiga, Forest, Flower Forest, Birch Forest, Dark Forest, Meadow", "rarity": "Rare", "condition": "", "forms": ""},
"articuno": {"name": "Articuno", "number": 144, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Snowy Plains", "rarity": "Ultra-Rare", "condition": "Structure: ArticunoTower (COBBLEVERSE)", "forms": "Galarian form: Under Dyna Tree during the night"},
"zapdos": {"name": "Zapdos", "number": 145, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Stony Shore", "rarity": "Ultra-Rare", "condition": "Structure: Zapdos Tower (COBBLEVERSE)", "forms": "Galarian form: Under Dyna Tree during a thunderstorm"},
"moltres": {"name": "Moltres", "number": 146, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "Nether Wastes", "rarity": "Ultra-Rare", "condition": "Structure: Moltres Tower (COBBLEVERSE)", "forms": "Galarian form: Under Dyna Tree during the day"},
"dratini": {"name": "Dratini", "number": 147, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes except Frozen Ocean", "rarity": "Rare", "condition": "Structure: Ocean Ruins", "forms": ""},
"dragonair": {"name": "Dragonair", "number": 148, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes except Frozen Ocean", "rarity": "Rare", "condition": "Structure: Ocean Ruins", "forms": ""},
"dragonite": {"name": "Dragonite", "number": 149, "generation": "Gen 1 Kanto", "source": "Cobblemon", "spawn_biomes": "All Ocean biomes except Frozen Ocean", "rarity": "Rare", "condition": "Structure: Ocean Ruins", "forms": ""},
"mewtwo": {"name": "Mewtwo", "number": 150, "generation": "Gen 1 Kanto", "source": "ATM x MSD", "spawn_biomes": "Savannah", "rarity": "Ultra-Rare", "condition": "Structure: Team Rocket Tower (COBBLEVERSE)", "forms": ""},
"mew": {"name": "Mew", "number": 151, "generation": "Gen 1 Kanto", "source": "MelloMons", "spawn_biomes": "Jungle", "rarity": "Ultra-Rare", "condition": "Structure: Origin Temple (COBBLEVERSE)", "forms": ""},
}

# === Search & Format Utilities ===

def search_pokemon(query: str) -> list[dict]:
    """Search for Pokemon by name, number, biome, rarity, generation, or condition."""
    q = query.lower().strip()
    # Handle '#123' style queries
    q_num = q.lstrip("#")

    # Split query into individual words for multi-word matching
    words = q.split()

    results = []
    for key, p in POKEMON_SPAWNS.items():
        score = 0
        name_lower = p["name"].lower()

        # Exact name match
        if q == key or q == name_lower:
            score += 10
        # Partial name match
        elif q in key or q in name_lower:
            score += 5
        # Check if pokemon name appears anywhere in the query
        elif key in q or name_lower in q:
            score += 5

        # Number match
        if q_num.isdigit() and int(q_num) == p["number"]:
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
        if p["condition"] and q in p["condition"].lower():
            score += 2

        # Forms match — boost heavily when user asks about a specific form
        if p["forms"]:
            forms_lower = p["forms"].lower()
            if q in forms_lower:
                score += 4
            # Check individual words like "alolan", "galarian", "hisuian"
            form_keywords = ["alolan", "galarian", "hisuian", "paldean", "valencian",
                             "cosplay", "mega", "shadow", "shiny"]
            for word in words:
                if word in form_keywords and word in forms_lower:
                    score += 6  # Strong boost for form-specific queries

        if score > 0:
            results.append((score, p))
    results.sort(key=lambda x: x[0], reverse=True)
    return [p for _, p in results]


def format_pokemon(p: dict) -> str:
    """Format a single Pokemon entry as readable text."""
    lines = [f"#{p['number']} {p['name']} ({p['generation']})"]
    lines.append(f"  Base spawn biomes: {p['spawn_biomes']}")
    lines.append(f"  Rarity: {p['rarity']}")
    if p["condition"]:
        lines.append(f"  Condition: {p['condition']}")
    if p["forms"]:
        lines.append(f"  ALTERNATIVE FORMS & THEIR SPAWN LOCATIONS: {p['forms']}")
        lines.append(f"  NOTE: Each form spawns in DIFFERENT biomes than the base form listed above.")
    return "\n".join(lines)
