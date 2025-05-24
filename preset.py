# commands/preset.py
from telethon import events
from config import client
from storage import load_presets, save_presets

@client.on(events.NewMessage(pattern=r"^/simpan_preset (\w+)\s+(.+)", outgoing=True))
async def simpan_preset(event):
    nama, pesan = event.pattern_match.group(1), event.pattern_match.group(2)
    presets = load_presets()
    presets[nama] = pesan
    save_presets(presets)
    await event.reply(f"💾 Preset `{nama}` telah disimpan dengan pesan:\n\n{pesan}", parse_mode="md")

@client.on(events.NewMessage(pattern=r"^/list_preset$", outgoing=True))
async def list_preset(event):
    presets = load_presets()
    if not presets:
        await event.reply("📭 Belum ada preset yang disimpan~")
        return
    teks = "💖 **Daftar Preset Pesan:**\n\n"
    for nama in presets:
        teks += f"• `{nama}`\n"
    await event.reply(teks, parse_mode="md")

@client.on(events.NewMessage(pattern=r"^/edit_preset (\w+)\s+(.+)", outgoing=True))
async def edit_preset(event):
    nama, pesan_baru = event.pattern_match.group(1), event.pattern_match.group(2)
    presets = load_presets()
    if nama not in presets:
        await event.reply(f"❌ Preset `{nama}` tidak ditemukan.")
        return
    presets[nama] = pesan_baru
    save_presets(presets)
    await event.reply(f"🔄 Preset `{nama}` telah diperbarui!", parse_mode="md")

@client.on(events.NewMessage(pattern=r"^/hapus_preset (\w+)", outgoing=True))
async def hapus_preset(event):
    nama = event.pattern_match.group(1)
    presets = load_presets()
    if nama in presets:
        del presets[nama]
        save_presets(presets)
        await event.reply(f"🗑️ Preset `{nama}` berhasil dihapus.")
    else:
        await event.reply(f"❌ Preset `{nama}` tidak ditemukan.")