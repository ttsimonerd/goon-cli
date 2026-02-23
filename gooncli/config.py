import json
from pathlib import Path

CONFIG_DIR = Path.home() / ".gooncli"
CONFIG_FILE = CONFIG_DIR / "config.json"

DEFAULT_CONFIG = {
    "speed": 0.05,
    "mobile_version": False,
}

def load_config():
    cfg = DEFAULT_CONFIG.copy()

    if not CONFIG_FILE.exists():
        return cfg

    try:
        with open(CONFIG_FILE, "r") as f:
            user_cfg = json.load(f)
    except:
        return cfg

    for key, value in DEFAULT_CONFIG.items():
        cfg[key] = user_cfg.get(key, value)

    return cfg

def save_config(cfg):
    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(CONFIG_FILE, "w") as f:
        json.dump(cfg, f, indent=4)

def reset_config():
    save_config(DEFAULT_CONFIG.copy())
