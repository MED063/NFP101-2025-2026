import subprocess
import numpy as np
import cv2
import math

from utils.gesture_action import GestureAction

# ############### CODE IA (Claude) ################
class VolumeController(GestureAction):
    """Contrôle le volume système via le pincement pouce-index."""

    def __init__(self, min_vol: int = 0, max_vol: int = 100,
                 dist_min: int = 50, dist_max: int = 300):
        super().__init__("Volume")
        self.min_vol = min_vol
        self.max_vol = max_vol
        self.dist_min = dist_min
        self.dist_max = dist_max
        self._current_vol = self._get_volume()

    def _get_volume(self) -> int:
        try:
            result = subprocess.run(
                ["osascript", "-e", "output volume of (get volume settings)"],
                capture_output=True, text=True
            )
            return int(result.stdout.strip())
        except Exception:
            return 50

    def _set_volume(self, vol_percent: int):
        try:
            subprocess.run(
                ["osascript", "-e", f"set volume output volume {int(vol_percent)}"],
                capture_output=True
            )
        except Exception as e:
            print(f"Erreur set volume: {e}")

    def process(self, img, hands_data: list):
        """Ajuste le volume selon la distance pouce-index. Retourne (img, continuer)."""
        if not hands_data or len(hands_data[0]["lmList"]) < 21:
            return img, True
        hand = hands_data[0]
        thumb, index = hand["lmList"][4], hand["lmList"][8]
        return self.adjust(img, thumb, index), True

    def adjust(self, img, thumb: dict, index: dict):
        try:
            x1, y1 = thumb["x"], thumb["y"]
            x2, y2 = index["x"], index["y"]
            length = math.hypot(x2 - x1, y2 - y1)

            vol_percent = int(np.interp(length, [self.dist_min, self.dist_max],
                                        [self.min_vol, self.max_vol]))
            self._set_volume(vol_percent)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            img = self.render_hud(img, f"VOL: {vol_percent}%", pos=(x2 + 20, y2))
        except Exception as e:
            print(f"Erreur volume: {e}")
        return img
# ########################################
