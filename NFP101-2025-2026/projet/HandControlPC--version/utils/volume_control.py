import subprocess
import numpy as np
import cv2
import math


class VolumeController:
    def __init__(self):
        self.min_vol = 0
        self.max_vol = 100
        self._current_vol = self._get_volume()

    def _get_volume(self):
        try:
            result = subprocess.run(
                ["osascript", "-e", "output volume of (get volume settings)"],
                capture_output=True, text=True
            )
            return int(result.stdout.strip())
        except Exception:
            return 50

    def _set_volume(self, vol_percent):
        try:
            subprocess.run(
                ["osascript", "-e", f"set volume output volume {int(vol_percent)}"],
                capture_output=True
            )
        except Exception as e:
            print(f"Erreur set volume: {e}")

    def adjust(self, img, thumb, index):
        try:
            x1, y1 = thumb["x"], thumb["y"]
            x2, y2 = index["x"], index["y"]
            length = math.hypot(x2 - x1, y2 - y1)

            vol_percent = int(np.interp(length, [50, 300], [self.min_vol, self.max_vol]))
            self._set_volume(vol_percent)

            cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 3)
            cv2.putText(img, f'VOL: {vol_percent}%', (x2 + 20, y2),
                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        except Exception as e:
            print(f"Erreur volume: {str(e)}")

        return img
