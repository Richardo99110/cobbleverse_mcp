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
