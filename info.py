# heartie_userbot/commands/info.py

from telethon import events
from config import OWNER_ID, HEARTIE_VERSION
from storage import load_license
from datetime import datetime
import random

# Banner lucu & pink aesthetic
BANNER = """
<b>Welcome to</b> <i>Heartie Userbot</i> ♡
<code>Versi {version}</code>

<b>Userbot rasa cewek manis siap nemenin kamu~</b>
""".strip()

def get_heartie_status():
    license_info = load_license()
    expired = license_info.get("expired_at", None)
    if expired:
        expired_at = datetime.fromisoformat(expired)
        sisa = (expired_at - datetime.now()).days
        if sisa >= 0:
            return f"Aktivasi berlaku sampai <b>{expired_at.strftime('%d %B %Y')}</b> ({sisa} hari lagi)"
        else:
            return "<b>Masa aktif kamu sudah habis.</b> Segera perpanjang ya~"
    return "Belum ada data masa aktif. Mungkin kamu belum aktivasi~"

def register_info_handler(client):
    @client.on(events.NewMessage(pattern=r'^/start$'))
    async def start_handler(event):
        if event.sender_id != OWNER_ID:
            return  # Hanya untuk owner
        await event.respond(BANNER.format(version=HEARTIE_VERSION), parse_mode="html")

    @client.on(events.NewMessage(pattern=r'^/status$'))
    async def status_handler(event):
        if event.sender_id != OWNER_ID:
            return
        msg = get_heartie_status()
        await event.respond(f"♡ <b>Status Heartie</b>\n\n{msg}", parse_mode="html")

    @client.on(events.NewMessage(pattern=r'^/help$'))
    async def help_handler(event):
        if event.sender_id != OWNER_ID:
            return
        await event.respond(
            "♡ <b>Panduan Perintah Heartie</b>\n\n"
            "/start — Tampilkan banner lucu\n"
            "/status — Cek masa aktif userbot\n"
            "/help — Lihat semua perintah\n"
            "/feedback teks — Kirim saran/pesan manis buat developer\n"
            "/about — Info tentang Heartie", parse_mode="html"
        )

    @client.on(events.NewMessage(pattern=r'^/about$'))
    async def about_handler(event):
        if event.sender_id != OWNER_ID:
            return
        await event.respond(
            "<b>Heartie Userbot</b> versi {} ♡\n\n"
            "Dibuat khusus untuk bantu kamu kirim pesan ke banyak grup\n"
            "dengan gaya manis dan fleksibel~".format(HEARTIE_VERSION),
            parse_mode="html"
        )

    @client.on(events.NewMessage(pattern=r'^/feedback (.+)'))
    async def feedback_handler(event):
        if event.sender_id != OWNER_ID:
            return
        feedback = event.pattern_match.group(1)
        # Nanti bisa disimpan ke file atau dikirim ke admin bot
        await event.respond("♡ Terima kasih untuk feedback-nya~\n\n<i>{}</i>".format(feedback), parse_mode="html")