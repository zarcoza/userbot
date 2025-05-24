import json
import os

JOB_FILE = "storage/job_storage.json"
PRESET_FILE = "storage/preset_storage.json"

def load_jobs():
    if not os.path.exists(JOB_FILE):
        return {}
    with open(JOB_FILE, "r") as f:
        return json.load(f)

def save_jobs(jobs):
    with open(JOB_FILE, "w") as f:
        json.dump(jobs, f, indent=2)

def load_presets():
    if not os.path.exists(PRESET_FILE):
        return {}
    with open(PRESET_FILE, "r") as f:
        return json.load(f)

def save_presets(presets):
    with open(PRESET_FILE, "w") as f:
        json.dump(presets, f, indent=2)