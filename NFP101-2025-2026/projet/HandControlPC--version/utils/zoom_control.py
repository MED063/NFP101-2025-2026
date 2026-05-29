import cv2
import numpy as np
import math

from utils.gesture_action import GestureAction

# ############### CODE IA (Claude) ################
class ZoomManager(GestureAction):
    """Gère le zoom du flux vidéo via l'écartement de deux mains."""

    def __init__(self, min_scale: float = 0.5, max_scale: float = 3.0):
        super().__init__("Zoom")
        self.min_scale = min_scale
        self.max_scale = max_scale
        self.start_distance = None
        self.scale = 1.0
        self.base_image = None
        self.offset_x = 0
        self.offset_y = 0

    def capture_base_image(self, img):
        self.base_image = img.copy()
        self.offset_x = 0
        self.offset_y = 0
        self.scale = 1.0

    def process(self, img, hands_data: list):
        """Applique le zoom. Retourne (img, continuer_si_deux_mains)."""
        if len(hands_data) != 2:
            self.reset()
            return img, False
        return self.adjust(img, hands_data), True

    def adjust(self, img, hands_data: list):
        if self.base_image is None:
            self.capture_base_image(img)
        try:
            hand1 = hands_data[0]["lmList"][8]
            hand2 = hands_data[1]["lmList"][8]
            x1, y1 = hand1["x"], hand1["y"]
            x2, y2 = hand2["x"], hand2["y"]

            current_distance = math.hypot(x2 - x1, y2 - y1)
            if self.start_distance is None:
                self.start_distance = current_distance

            self.scale = np.clip(current_distance / self.start_distance,
                                 self.min_scale, self.max_scale)

            center_x = int((x1 + x2) / 2)
            center_y = int((y1 + y2) / 2)

            h, w = self.base_image.shape[:2]
            M = cv2.getRotationMatrix2D((center_x, center_y), 0, self.scale)
            M[0, 2] += self.offset_x
            M[1, 2] += self.offset_y
            zoomed_img = cv2.warpAffine(self.base_image, M, (w, h))

            zoomed_img = self.render_hud(zoomed_img, f"x{self.scale:.1f}", pos=(50, 100))
            cv2.rectangle(zoomed_img, (center_x - 10, center_y - 10),
                          (center_x + 10, center_y + 10), (0, 255, 0), 2)
            return zoomed_img

        except Exception as e:
            print(f"Erreur zoom: {e}")
            return self.base_image if self.base_image is not None else img

    def reset(self):
        self.start_distance = None
        self.scale = 1.0
        self.base_image = None
        self.offset_x = 0
        self.offset_y = 0
# ########################################
