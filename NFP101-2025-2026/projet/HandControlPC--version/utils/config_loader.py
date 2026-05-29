import json
import os
import copy

_DEFAULT_CONFIG = {
    "camera": {"width": 1280, "height": 720, "index": 0},
    "detection": {
        "min_detection_confidence": 0.7,
        "min_tracking_confidence": 0.5,
        "screenshot_confidence": 0.35,
        "gesture_history_length": 15,
        "cooldown_frames": 15
    },
    "volume": {"min": 0, "max": 100, "distance_min": 50, "distance_max": 300},
    "screenshot": {"folder": "screenshots", "cooldown": 30, "stable_threshold": 0.6},
    "zoom": {"min_scale": 0.5, "max_scale": 3.0}
}

def load_config(path: str = "config.json") -> dict:
    """Charge la configuration depuis un fichier JSON, avec fallback sur les valeurs par défaut."""
    if not os.path.exists(path):
        print(f"[Config] Fichier '{path}' introuvable, utilisation des valeurs par défaut.")
        return _DEFAULT_CONFIG.copy()
    try:
        with open(path, "r", encoding="utf-8") as f:
            user_cfg = json.load(f)
        merged = copy.deepcopy(_DEFAULT_CONFIG)
        for section, values in user_cfg.items():
            if section in merged and isinstance(values, dict):
                merged[section].update(values)
            else:
                merged[section] = values
        return merged
    except json.JSONDecodeError as e:
        print(f"[Config] Erreur de parsing JSON : {e}. Utilisation des valeurs par défaut.")
        return copy.deepcopy(_DEFAULT_CONFIG)
