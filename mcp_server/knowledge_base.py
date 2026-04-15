"""
COBBLEVERSE Wiki Knowledge Base - INSTALLATION section
"""

INSTALLATION = {
    "install_modrinth": {
        "title": "How To Install COBBLEVERSE From Modrinth",
        "url": "https://www.lumyverse.com/cobbleverse/how-to-install-cobbleverse-on-modrinth/",
        "content": (
            "To install COBBLEVERSE from Modrinth:\n"
            "1. Download the Modrinth App from https://modrinth.com/app (available for Windows, macOS, Linux).\n"
            "   Note: COBBLEVERSE is specifically configured for Windows. macOS/Linux may work but are not fully supported.\n"
            "2. Install and open the Modrinth App.\n"
            "3. Sign in with your Microsoft account (the same one used for Minecraft: Java Edition).\n"
            "4. Search for 'Cobbleverse' in the search bar and select the 'Modpack' filter.\n"
            "5. Click on COBBLEVERSE and hit Install. Modrinth handles everything automatically.\n"
            "IMPORTANT: Before launching for the first time, allocate at least 4 GB (4096 MB) of RAM.\n"
            "Click the gear icon in the top-right corner to open Settings and adjust memory allocation."
        ),
        "keywords": ["install", "modrinth", "download", "launcher", "setup", "ram", "memory"]
    },
    "install_curseforge": {
        "title": "How To Install COBBLEVERSE From CurseForge",
        "url": "https://www.lumyverse.com/cobbleverse/how-to-install-cobbleverse-on-curseforge/",
        "content": (
            "To install COBBLEVERSE from CurseForge:\n"
            "1. Download the CurseForge app from https://www.curseforge.com/download/app.\n"
            "2. During installation, you will be asked to install Overwolf. It is recommended as it handles "
            "automatic updates and simplifies modpack management.\n"
            "3. Open CurseForge, search for 'Cobbleverse' in the search bar.\n"
            "4. Click Install to download and set up the modpack automatically.\n"
            "That's it — the rest is automatic and the modpack will be ready to play."
        ),
        "keywords": ["install", "curseforge", "download", "launcher", "overwolf", "setup"]
    },
    "server_apex": {
        "title": "How To Set Up A Server for Apex Hosting",
        "url": "https://www.lumyverse.com/cobbleverse/how-set-up-a-server-for-apex-hosting-cobbleverse/",
        "content": (
            "To set up a COBBLEVERSE server on Apex Hosting:\n"
            "STEP 1: Choose Your Server\n"
            "- Visit https://apexhost.gg/LUMYVERSE to access the selection page.\n"
            "- Choose a server plan that fits your needs (adjust RAM and player slots accordingly).\n"
            "- COBBLEVERSE requires at least 4 GB of RAM.\n"
            "- After clicking 'Order Now', go to the Configuration page and select your server location and version:\n"
            "  * COBBLEVERSE Pokémon Adventure [Modrinth]\n"
            "  * COBBLEVERSE Pokémon Adventure [CurseForge]\n"
            "- After setup, you will receive an email with login details for the Apex Hosting Panel.\n"
            "STEP 2: Start your server and enjoy COBBLEVERSE."
        ),
        "keywords": ["server", "apex", "hosting", "apex hosting", "multiplayer", "setup", "ram"]
    },
    "server_apex_update": {
        "title": "How To Update Apex Server",
        "url": "https://www.lumyverse.com/cobbleverse/how-to-update-apex-server/",
        "content": (
            "To update your COBBLEVERSE Apex server:\n"
            "IMPORTANT: Always backup your world first!\n"
            "Fastest method — Reset Server Files:\n"
            "- Use 'Reset Server Files' in the Apex panel. Do NOT select 'All Server Files' or your world will be deleted.\n"
            "  This option is only available if the update is available on Apex.\n"
            "Manual method via FTP:\n"
            "1. Access your server through the Apex Panel and click 'FTP File Access'.\n"
            "2. Open these three folders: Config, Mods, Datapacks.\n"
            "3. Delete all current COBBLEVERSE content in each folder.\n"
            "4. Replace with the updated files from the corresponding folders in your launcher.\n"
            "- Only replace content already on the server — do not add client-only files.\n"
            "- Do not delete any custom content you have added, unless the server fails to launch."
        ),
        "keywords": ["update", "apex", "server", "ftp", "upgrade", "reset", "files"]
    },
    "server_nitrado": {
        "title": "How To Set Up A Server for Nitrado",
        "url": "https://www.lumyverse.com/cobbleverse/how-set-up-a-server-for-nitrado-cobbleverse/",
        "content": (
            "To set up a COBBLEVERSE server on Nitrado:\n"
            "STEP 1: Choose your Version\n"
            "- CurseForge version: https://nitra.do/COBBLEVERSE\n"
            "- Modrinth version: https://nitra.do/COBBLEVERSE-Modrinth\n"
            "  These links pre-install COBBLEVERSE for you automatically.\n"
            "- Choose a server plan based on your needs (RAM and player slots).\n"
            "- COBBLEVERSE requires at least 4 GB of RAM.\n"
            "- Once setup is done, your server starts automatically and you can access the Nitrado dashboard.\n"
            "STEP 2: Start your server and enjoy COBBLEVERSE."
        ),
        "keywords": ["server", "nitrado", "hosting", "multiplayer", "setup", "ram"]
    },
    "lumymon": {
        "title": "LumyMon",
        "url": "https://www.lumyverse.com/cobbleverse/lumymon/",
        "content": (
            "LumyMon is a utility and content expansion mod that enhances the Cobblemon experience in COBBLEVERSE.\n\n"
            "Navigation & Exploration:\n"
            "- Regional Cartography Tables: Craft precise maps using these workstations.\n"
            "- Gym & League Mapping: Forge items representing Gym Leaders and Champions to generate maps to their locations.\n"
            "- Regional Poké Radars: Combine Locator Chips with Cartography Tables to track Legendary Pokémon positions.\n"
            "- Regi Ores & Resources: Discover unique ores to awaken the Titans; use Apricorn Boxes for storage.\n\n"
            "The Altar System:\n"
            "- Altars and Shrines: Custom 3D blocks for Legendaries from Generations 1–4, plus Eternatus, Regieleki, Regidrago.\n"
            "- Summoning Mechanics: Use specific items on altars to trigger encounters with custom particle and sound effects.\n"
            "- Unique Dimensions: Custom dimensions for Arceus and Darkrai with unique mechanics.\n"
            "- Every summoned Pokémon has randomized IVs and levels — chance for Shiny or Perfect IV encounters.\n\n"
            "Quality of Life:\n"
            "- Remote PC Access: Access your Pokémon Boxes from anywhere (Default key: P).\n"
            "- Better Riding: Hotkey to instantly dismount from your Pokémon (Default key: V).\n"
            "- Elemental Mounts: Fire immunity while riding Fire-types; infinite water breathing while riding Water-types.\n"
            "- Vanilla Replacements: Some vanilla mobs replaced by Pokémon (e.g., Gastly replaces Happy Ghastlings).\n\n"
            "Download:\n"
            "- Modrinth: https://modrinth.com/mod/lumymon\n"
            "- CurseForge: https://www.curseforge.com/minecraft/mc-mods/lumymon\n\n"
            "LumyMon works standalone but is the core of the COBBLEVERSE modpack."
        ),
        "keywords": ["lumymon", "mod", "expansion", "altar", "shrine", "radar", "cartography", "remote pc", "riding", "download"]
    },
}


# ── GAMEPLAY ──────────────────────────────────────────────────────────────────

GAMEPLAY = {
    "why_play": {
        "title": "Why Should I Play COBBLEVERSE",
        "url": "https://www.lumyverse.com/cobbleverse/why-should-i-play-cobbleverse/",
        "content": (
            "Your journey in COBBLEVERSE begins by choosing a starter Pokémon. "
            "COBBLEVERSE features exclusive starters from the Pallet Region and the Lumya Region, "
            "not found in the base Cobblemon mod.\n\n"
            "Starter Kit includes:\n"
            "- Your personal Trainer Card\n"
            "- A national Pokédex\n"
            "- A map to the first Gym in the Kanto region\n"
            "- 10 Poké Balls\n"
            "- A large backpack with plenty of space\n"
            "- 10 Oran Berries\n"
            "- A custom guidebook\n\n"
            "Key features:\n"
            "- Hostile mobs and hunger are disabled by default — focus on Pokémon battles. "
            "You can re-enable mobs and hunger if you prefer classic survival.\n"
            "- All Mythical, Ultra Beasts, and Legendary Pokémon are available, many in secret locations.\n"
            "- Shiny Rayquaza awaits in the End.\n"
            "- Ride over 200 Pokémon species, including flying mounts.\n"
            "- All 48 official Mega Evolutions are available. Press Y to Mega Evolve outside of battle "
            "with the correct Mega Stone and Mega Bracelet. Pokémon stay Mega Evolved while exploring.\n"
            "- Custom villages with Pokémon Centers and PokéMarkets.\n"
            "- The ultimate goal: complete the Pokémon League by defeating all Gym Leaders across regions, "
            "earning Badges, and becoming the Pokémon Master."
        ),
        "keywords": ["why play", "starter", "features", "overview", "start", "begin", "new",
                     "mega evolution", "riding", "pokémon center", "league", "badges", "what is"]
    },
    "exclusive_structures": {
        "title": "Exclusive Structures in COBBLEVERSE",
        "url": "https://www.lumyverse.com/cobbleverse/exclusive-structures-in-cobbleverse/",
        "content": (
            "COBBLEVERSE features many exclusive custom structures not found in vanilla Minecraft or base Cobblemon. "
            "These include Gyms for each region (Kanto, Johto, Hoenn, Sinnoh), Elite Four Towers, "
            "Legendary Pokémon temples and shrines, Team Rocket Tower, Burned Tower, Bell Tower, "
            "Sky Pillar, Spear Pillar, and many more.\n\n"
            "Each structure is tied to the progression system — you unlock new structures by defeating "
            "Gym Leaders and Champions of each region. Structures spawn in specific biomes and can be "
            "located using Cartography Tables and Poké Radars from the LumyMon mod.\n\n"
            "For detailed structure locations, use the /locate command with cheats enabled, "
            "e.g. /locate structure cobbleverse:bell_tower"
        ),
        "keywords": ["structures", "exclusive", "buildings", "gyms", "temples", "towers",
                     "custom", "locations", "biomes"]
    },
    "other_structures": {
        "title": "Other Structures (Legendary Monuments & More)",
        "url": "https://www.lumyverse.com/cobbleverse/other-structures/",
        "content": (
            "COBBLEVERSE includes many addon structures created by community collaborators:\n\n"
            "Legendary Monuments (COBBLEVERSE Version):\n"
            "- Lake Verity (Cherry Grove): Trial of Mesprit. Completing it gives the Mesprit Plume to spawn Mesprit and get a Red Chain component.\n"
            "- Lake Acuity (Glacial Chasm): Home of Uxie. Pass its trial to get the Uxie Claw for spawning Uxie and a Red Chain piece.\n"
            "- Lake Valor (Arid Highlands): Dwelling of Azelf. Overcome its trial to receive the Azelf Fang for spawning Azelf and the final Red Chain fragment.\n\n"
            "Other notable structures:\n"
            "- Outskirt Stand: An isolated merchant in the Desert Oasis that sells Zygarde Cells.\n"
            "- Turnback Cave: A misty cave that connects to the Distortion World. Team Galactic leader Selina was the only human to reach it.\n"
            "- Distortion World: A parallel dimension where time doesn't flow and space is unstable. "
            "Domain of Giratina. Only the Red Chain can imprison Giratina. "
            "To exit: find the natural return portal or craft an artificial portal using Raw Origin.\n"
            "- Four Treasures of Ruin (Ting-Lu, Chien-Pao, Wo-Chien, Chi-Yu): Sealed legendary entities. "
            "Remove 8 legendary stakes of a specific color around their sanctuary to awaken them.\n"
            "- Stark Mountain: A volcano in the Nether Wastes guarding the Magma Stone. Removing it awakens Heatran.\n"
            "- Eternatus Cocoon: A structure in The End. Requires 500 Galar Particles (overworld ore) to break the seal."
        ),
        "keywords": ["structures", "legendary monuments", "lake verity", "lake acuity", "lake valor",
                     "distortion world", "giratina", "turnback cave", "stark mountain", "heatran",
                     "eternatus", "zygarde", "outskirt stand", "ruin", "ting-lu", "chien-pao"]
    },
    "making_money": {
        "title": "Making Money in COBBLEVERSE",
        "url": "https://www.lumyverse.com/cobbleverse/making-money-in-cobbleverse/",
        "content": (
            "COBBLEVERSE features an economic system using two currencies:\n\n"
            "1. PokéDollars: Earned by defeating wild Pokémon and trainers (including Gym Leaders). "
            "Stronger trainers give more PokéDollars.\n"
            "2. Relic Coins: Avoid spending these — you need 100 to get a Gholdengo!\n\n"
            "Spending PokéDollars — CobbleMerchants:\n"
            "- Basic CobbleMerchant: Place a display case next to an unemployed villager. "
            "Wide range of items (Poké Balls, mob drops, healing supplies) but expensive.\n"
            "- Poké Mart CobbleMerchant (blue-roof villages): Smaller selection, slightly lower prices.\n"
            "- Shopping Center CobbleMerchant (larger villages): Huge variety (TMs, Rare Candies, etc.) "
            "at the lowest prices. Explore all floors!\n\n"
            "Earning PokéDollars:\n"
            "- Defeat wild Pokémon and trainers.\n"
            "- Sell items (emeralds, Relic Coins, Vitamins) to any CobbleMerchant via the 'Bank' option."
        ),
        "keywords": ["money", "pokédollars", "pokedollars", "economy", "currency", "earn",
                     "cobblemerchant", "merchant", "shop", "buy", "sell", "relic coin",
                     "gholdengo", "poké mart", "shopping"]
    },
    "pokemon_spawns": {
        "title": "All Pokémon Spawns in COBBLEVERSE",
        "url": "https://www.lumyverse.com/cobbleverse/all-pokemon-spawn-in-cobbleverse/",
        "content": (
            "COBBLEVERSE includes Pokémon from all 9 generations (Gen 1 Kanto through Gen 9 Paldea), "
            "totaling over 1025 Pokémon with custom spawn conditions.\n\n"
            "Key spawn info:\n"
            "- Biomes mentioned refer to vanilla Minecraft biomes. Use the PokéNav to find where Pokémon spawn.\n"
            "- The /checkspawn command may not work properly — use PokéNav instead.\n"
            "- For Pokémon added by Cobblemon, see https://wiki.cobblemon.com/ for more info.\n\n"
            "Legendary & Mythical spawn conditions:\n"
            "- Many require completing specific Trainer battle series first.\n"
            "- Example: Ho-Oh, Lugia, and the three Legendary Beasts only appear after defeating Kanto Champion Blue.\n"
            "- Legendaries are typically Ultra-Rare and tied to specific structures.\n\n"
            "Rarity tiers: Common, Uncommon, Rare, Ultra-Rare.\n\n"
            "Special conditions include: time of day (Day/Night/Dusk), weather (Clear/Rain/Storm/Thunderstorm), "
            "Y-level ranges, moon phases, nearby blocks, biome-specific spawns, and fishing.\n\n"
            "Regional forms (Alolan, Galarian, Hisuian, Paldean) spawn in different biomes than their base forms.\n\n"
            "Examples:\n"
            "- Bulbasaur: All Jungle biomes (Ultra-Rare)\n"
            "- Pikachu: All Forest biomes except Dark Forest (Uncommon, during a storm)\n"
            "- Eevee: Plains, Forest, Birch Forest, Cherry Grove (Uncommon, Day)\n"
            "- Mewtwo: Savannah (Ultra-Rare, Structure: Team Rocket Tower)\n"
            "- Rayquaza: Deep Ocean (Ultra-Rare, Structure: Sky Pillar)\n"
            "- Arceus: Origin Dimension (Ultra-Rare, Structure: Sinnoh Temple)\n\n"
            "For the full spawn table with all 1025+ Pokémon, visit the source URL."
        ),
        "keywords": ["spawn", "pokémon", "pokemon", "find", "catch", "where", "biome",
                     "location", "rare", "ultra-rare", "legendary", "mythical", "shiny",
                     "generation", "gen", "kanto", "johto", "hoenn", "sinnoh", "unova",
                     "kalos", "alola", "galar", "paldea", "fishing", "night", "day",
                     "weather", "storm", "alolan", "galarian", "hisuian"]
    },
}