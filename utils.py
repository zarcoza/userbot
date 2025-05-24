import json
import os

BLACKLIST_FILE = "database/blacklist.json"

def load_blacklist():
    if not os.path.exists(BLACKLIST_FILE):
        return []
    with open(BLACKLIST_FILE, "r") as f:
        return json.load(f)

def save_blacklist(data):
    with open(BLACKLIST_FILE, "w") as f:
        json.dump(data, f, indent=2)

async def get_all_groups(client):
    """Mengambil semua grup (termasuk supergroup), kecuali yang diblacklist."""
    groups = []
    blacklist = load_blacklist()

    async for dialog in client.iter_dialogs():
        if dialog.is_group or dialog.is_channel and dialog.entity.megagroup:
            if dialog.id in blacklist:
                continue  # Lewati grup yang diblacklist
            groups.append(dialog)

    return groups