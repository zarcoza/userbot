# main.py
import asyncio
from config import client
from telethon import events

from commands import forward, schedule, preset, blacklist, info

BANNER = """
╭━━━━━━━━━━━━━━━━━━━━━╮
┃ 💖 𝗛𝗲𝗮𝗿𝘁𝗶𝗲 𝗨𝘀𝗲𝗿𝗯𝗼𝘁 💖
┃ Powered by your sweet account!
╰━━━━━━━━━━━━━━━━━━━━━╯
"""

@client.on(events.NewMessage(pattern="/start"))
async def start(event):
    await event.reply("🌸 Hai, aku Heartie, userbot pink-mu yang manis!\n\nGunakan /help untuk lihat semua fiturku ya! 💖")

@client.on(events.NewMessage(pattern="/help"))
async def help_cmd(event):
    from commands.info import get_help_text
    await event.respond(get_help_text())

async def main():
    print(BANNER)
    await client.start()
    print("💖 Heartie siap membantu kamu!")
    await client.run_until_disconnected()

if __name__ == "__main__":
    asyncio.run(main())
