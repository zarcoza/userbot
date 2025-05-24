# heartie_userbot/commands/__init__.py

from .forward import register_forward_handler
from .schedule import register_schedule_handler
from .preset import register_preset_handler
from .blacklist import register_blacklist_handler
from .info import register_info_handler

def register_all_handlers(client):
    register_forward_handler(client)
    register_schedule_handler(client)
    register_preset_handler(client)
    register_blacklist_handler(client)
    register_info_handler(client)