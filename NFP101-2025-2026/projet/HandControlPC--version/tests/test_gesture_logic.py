"""
Tests unitaires - logique gestuelle (sans webcam ni matériel).
Exécuter : pytest tests/
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import pytest
import numpy as np


# ---------------------------------------------------------------------------
# Tests : recognize_sign (test_sign_recognition)
# ---------------------------------------------------------------------------
from test_sign_recognition import recognize_sign, SIGNS


def test_recognize_sign_A():
    assert recognize_sign([1, 0, 0, 0, 0]) == "A"


def test_recognize_sign_B():
    assert recognize_sign([0, 1, 1, 1, 1]) == "B"


def test_recognize_sign_L():
    assert recognize_sign([1, 1, 0, 0, 0]) == "L"


def test_recognize_sign_O():
    assert recognize_sign([0, 1, 1, 1, 0]) == "O"


def test_recognize_sign_N():
    assert recognize_sign([1, 1, 1, 0, 0]) == "N"


def test_recognize_sign_J():
    assert recognize_sign([1, 0, 0, 0, 1]) == "J"


def test_recognize_sign_U():
    assert recognize_sign([0, 1, 1, 0, 0]) == "U"


def test_recognize_sign_R():
    assert recognize_sign([0, 1, 0, 0, 0]) == "R"


def test_recognize_sign_unknown():
    assert recognize_sign([0, 0, 0, 0, 0]) is None
    assert recognize_sign([1, 1, 1, 1, 1]) is None


def test_all_signs_are_recognized():
    for name, pattern in SIGNS.items():
        assert recognize_sign(pattern) == name


def test_bonjour_sequence_letters_all_present():
    from test_sign_recognition import BONJOUR_SEQUENCE
    for letter in BONJOUR_SEQUENCE:
        assert letter in SIGNS, f"La lettre '{letter}' de BONJOUR n'est pas dans SIGNS"


def test_bonjour_sequence_is_correct():
    from test_sign_recognition import BONJOUR_SEQUENCE
    assert BONJOUR_SEQUENCE == ["B", "O", "N", "J", "O", "U", "R"]


# ---------------------------------------------------------------------------
# Tests : VolumeController (calcul interp, sans appel système)
# ---------------------------------------------------------------------------
import math

def test_volume_interpolation():
    """Vérifie que la distance se traduit correctement en pourcentage de volume."""
    min_d, max_d = 50, 300
    min_v, max_v = 0, 100

    length_min = 50
    vol_min = int(np.interp(length_min, [min_d, max_d], [min_v, max_v]))
    assert vol_min == 0

    length_max = 300
    vol_max = int(np.interp(length_max, [min_d, max_d], [min_v, max_v]))
    assert vol_max == 100

    length_mid = 175
    vol_mid = int(np.interp(length_mid, [min_d, max_d], [min_v, max_v]))
    assert 45 <= vol_mid <= 55


def test_volume_distance_calculation():
    """Vérifie le calcul de distance entre deux points."""
    p1 = {"x": 0, "y": 0}
    p2 = {"x": 3, "y": 4}
    dist = math.hypot(p2["x"] - p1["x"], p2["y"] - p1["y"])
    assert dist == pytest.approx(5.0)


# ---------------------------------------------------------------------------
# Tests : ZoomManager (logique de scale, sans image réelle)
# ---------------------------------------------------------------------------
from utils.zoom_control import ZoomManager


def test_zoom_reset():
    z = ZoomManager()
    z.scale = 2.5
    z.start_distance = 200.0
    z.reset()
    assert z.scale == 1.0
    assert z.start_distance is None
    assert z.base_image is None


def test_zoom_scale_clamp():
    """Vérifie que le scale est bien borné entre min et max."""
    z = ZoomManager(min_scale=0.5, max_scale=3.0)
    scale = np.clip(10.0, z.min_scale, z.max_scale)
    assert scale == 3.0
    scale = np.clip(0.01, z.min_scale, z.max_scale)
    assert scale == 0.5


def test_zoom_is_gesture_action():
    from utils.gesture_action import GestureAction
    z = ZoomManager()
    assert isinstance(z, GestureAction)
    assert z.name == "Zoom"


# ---------------------------------------------------------------------------
# Tests : fingers_up (logique pure)
# ---------------------------------------------------------------------------

def make_hand(tip_positions: dict) -> dict:
    """Crée des données de main factices pour tester fingers_up."""
    lmList = [{"id": i, "x": 100, "y": 100} for i in range(21)]
    # Index tip=8, pip=6 ; Majeur tip=12, pip=10
    # On simule doigt levé : tip.y < pip.y
    # On simule doigt baissé : tip.y > pip.y
    for tip_id, pip_id, up in tip_positions:
        if up:
            lmList[tip_id]["y"] = 50   # tip au-dessus
            lmList[pip_id]["y"] = 100  # pip en-dessous
        else:
            lmList[tip_id]["y"] = 150  # tip en-dessous
            lmList[pip_id]["y"] = 100  # pip au-dessus
    return {"lmList": lmList}


def test_fingers_up_returns_list_of_5():
    from utils.hand_tracking import HandDetector
    detector = HandDetector()
    hand = make_hand([(8, 6, True), (12, 10, False), (16, 14, False), (20, 18, False)])
    result = detector.fingers_up(hand, confidence=0.0)
    assert isinstance(result, list)
    assert len(result) == 5


def test_empty_hand_returns_zeros():
    from utils.hand_tracking import HandDetector
    detector = HandDetector()
    result = detector.fingers_up({"lmList": []})
    assert result == [0, 0, 0, 0, 0]
