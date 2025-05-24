from telethon import events
from utils import load_blacklist, save_blacklist, get_group_by_name
from userbot import client

@client.on(events.NewMessage(pattern=r'/blacklist_add (.+)'))
async def blacklist_add(event):
    name = event.pattern_match.group(1).strip()
    group = await get_group_by_name(client, name)
    
    if not group:
        await event.reply("❌ Grup dengan nama itu tidak ditemukan!")
        return

    blacklist = load_blacklist()
    if group.title not in blacklist:
        blacklist.append(group.title)
        save_blacklist(blacklist)
        await event.reply(f"🚫 Grup {group.title} telah ditambahkan ke blacklist!")
    else:
        await event.reply("⚠️ Grup itu sudah diblacklist.")

@client.on(events.NewMessage(pattern=r'/blacklist_remove (.+)'))
async def blacklist_remove(event):
    name = event.pattern_match.group(1).strip()
    blacklist = load_blacklist()

    if name in blacklist:
        blacklist.remove(name)
        save_blacklist(blacklist)
        await event.reply(f"✅ Grup {name} telah dihapus dari blacklist!")
    else:
        await event.reply("⚠️ Grup itu tidak ada dalam blacklist.")

@client.on(events.NewMessage(pattern=r'/list_blacklist'))
async def list_blacklist(event):
    blacklist = load_blacklist()
    if not blacklist:
        await event.reply("🌸 Belum ada grup yang diblacklist.")
        return

    text = "🚫 Daftar Grup Blacklist:\n\n"
    for name in blacklist:
        text += f"- {name}\n"

    await event.reply(text)