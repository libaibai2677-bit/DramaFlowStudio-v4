# DramaFlow Studio v4 - Config System

import json
import os
from typing import Any, Dict

CONFIG_PATH = "config/app_config.json"

DEFAULT_CONFIG: Dict[str, Any] = {
    "app_name": "DramaFlow Studio v4",
    "version": "1.0.0",

    "image_search": {
        "enable_cache": True,
        "cache_dir": "cache/images",
        "max_results": 30
    },

    "providers": {
        "pexels": {"enabled": True},
        "pixabay": {"enabled": True},
        "unsplash": {"enabled": True},
        "bing": {"enabled": False},
        "google": {"enabled": False}
    }
}


def load_config() -> Dict[str, Any]:
    """Load configuration from file or create default."""

    os.makedirs("config", exist_ok=True)

    if not os.path.exists(CONFIG_PATH):
        save_config(DEFAULT_CONFIG)
        return DEFAULT_CONFIG

    try:
        with open(CONFIG_PATH, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        return DEFAULT_CONFIG


def save_config(config: Dict[str, Any]) -> None:
    """Save configuration to file."""

    os.makedirs("config", exist_ok=True)

    with open(CONFIG_PATH, "w", encoding="utf-8") as f:
        json.dump(config, f, indent=4, ensure_ascii=False)
