# config.py
from telethon import TelegramClient
import os

API_ID = int(os.getenv("API_ID", "
27165484"))  # ganti sesuai API ID kamu
API_HASH = os.getenv("API_HASH", "b5f28de58166f16d6fedc4e0fd29a859")
SESSION_NAME = os.getenv("SESSION_NAME", "heartie_session")

# Inisialisasi client
client = TelegramClient(SESSION_NAME, API_ID, API_HASH)

# File penyimpanan
PRESET_FILE = "data/presets.json"
BLACKLIST_FILE = "data/blacklist.json"
SCHEDULE_FILE = "data/schedule.json"
