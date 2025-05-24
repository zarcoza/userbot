import json
import os

BLACKLIST_FILE = "database/blacklist.json"

def load_blacklist():
    """Muat daftar nama grup yang diblacklist dari file JSON."""
    if not os.path.exists(BLACKLIST_FILE):
        return []
    with open(BLACKLIST_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_blacklist(data):
    """Simpan daftar nama grup yang diblacklist ke file JSON."""
    with open(BLACKLIST_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2)

async def get_all_groups(client):
    """
    Ambil semua grup (termasuk supergroup) yang diikuti oleh userbot,
    kecuali yang diblacklist berdasarkan nama grup (title).
    """
    groups = []
    blacklist = load_blacklist()

    async for dialog in client.iter_dialogs():
        if dialog.is_group or (dialog.is_channel and getattr(dialog.entity, "megagroup", False)):
            if dialog.title in blacklist:
                continue
            groups.append(dialog)

    return groups

async def get_group_by_name(client, name):
    """Ambil objek dialog grup berdasarkan nama grup (title)."""
    async for dialog in client.iter_dialogs():
        if (dialog.is_group or (dialog.is_channel and getattr(dialog.entity, "megagroup", False))) and dialog.title.lower() == name.lower():
            return dialog
    return None