"""
Tests unitaires : ScreenshotTaker (sans déclenchement réel de capture).
Exécuter : pytest tests/
"""
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

import tempfile
import pytest
from unittest.mock import patch, MagicMock


def test_screenshot_creates_folder():
    with tempfile.TemporaryDirectory() as tmp:
        folder = os.path.join(tmp, "my_shots")
        with patch("mss.mss") as mock_mss:
            mock_ctx = MagicMock()
            mock_mss.return_value.__enter__ = lambda s: mock_ctx
            mock_mss.return_value.__exit__ = MagicMock(return_value=False)
            mock_ctx.shot = MagicMock()

            from utils.screenshot import ScreenshotTaker
            taker = ScreenshotTaker(folder=folder)
            assert os.path.isdir(folder)


def test_screenshot_is_gesture_action():
    with patch("mss.mss"):
        from utils.gesture_action import GestureAction
        from utils.screenshot import ScreenshotTaker
        with tempfile.TemporaryDirectory() as tmp:
            with patch("mss.mss") as mock_mss:
                mock_ctx = MagicMock()
                mock_mss.return_value.__enter__ = lambda s: mock_ctx
                mock_mss.return_value.__exit__ = MagicMock(return_value=False)
                taker = ScreenshotTaker(folder=tmp)
                assert isinstance(taker, GestureAction)
                assert taker.name == "Screenshot"


def test_volume_is_gesture_action():
    from utils.gesture_action import GestureAction
    from utils.volume_control import VolumeController
    with patch("subprocess.run") as mock_run:
        mock_run.return_value = MagicMock(stdout="50\n")
        vc = VolumeController()
        assert isinstance(vc, GestureAction)
        assert vc.name == "Volume"
