import os
import json

settings = None
mappings = None


def load_settings():
    global settings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'settings.json')) as f:
        settings = json.load(f)

def load_mappings():
    global mappings
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'mappings.json')) as m:
        mappings = json.load(m)

load_settings()
load_mappings()