# storage.py
import json
import os
from config import PRESET_FILE

def load_presets():
    if not os.path.exists(PRESET_FILE):
        return {}
    with open(PRESET_FILE, "r") as f:
        return json.load(f)

def save_presets(presets):
    with open(PRESET_FILE, "w") as f:
        json.dump(presets, f, indent=2)