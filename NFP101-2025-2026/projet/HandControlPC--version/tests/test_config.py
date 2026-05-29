"""
Tests unitaires - chargement de la configuration.
Exécuter : pytest tests/
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import json
import tempfile
import pytest

from utils.config_loader import load_config


def test_load_config_default_when_missing():
    cfg = load_config("nonexistent_file.json")
    assert "camera" in cfg
    assert "detection" in cfg
    assert "volume" in cfg
    assert "screenshot" in cfg
    assert "zoom" in cfg


def test_load_config_values_default():
    cfg = load_config("nonexistent_file.json")
    assert cfg["camera"]["width"] == 1280
    assert cfg["camera"]["height"] == 720
    assert cfg["volume"]["min"] == 0
    assert cfg["volume"]["max"] == 100


def test_load_config_from_file():
    custom = {"camera": {"width": 640, "height": 480}}
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        json.dump(custom, f)
        tmp_path = f.name
    try:
        cfg = load_config(tmp_path)
        assert cfg["camera"]["width"] == 640
        assert cfg["camera"]["height"] == 480
        # Les autres sections restent par défaut
        assert "detection" in cfg
    finally:
        os.unlink(tmp_path)


def test_load_config_invalid_json_fallback():
    with tempfile.NamedTemporaryFile(mode="w", suffix=".json", delete=False) as f:
        f.write("{ invalid json }")
        tmp_path = f.name
    try:
        cfg = load_config(tmp_path)
        assert cfg["camera"]["width"] == 1280  # retour aux valeurs par défaut
    finally:
        os.unlink(tmp_path)


def test_load_real_config():
    config_path = os.path.join(os.path.dirname(__file__), "..", "config.json")
    if os.path.exists(config_path):
        cfg = load_config(config_path)
        assert cfg["camera"]["width"] > 0
        assert cfg["camera"]["height"] > 0
        assert 0 <= cfg["volume"]["min"] < cfg["volume"]["max"]


def test_screenshot_folder_key_present():
    cfg = load_config("nonexistent_file.json")
    assert "folder" in cfg["screenshot"]


def test_zoom_bounds_valid():
    cfg = load_config("nonexistent_file.json")
    assert cfg["zoom"]["min_scale"] < cfg["zoom"]["max_scale"]
