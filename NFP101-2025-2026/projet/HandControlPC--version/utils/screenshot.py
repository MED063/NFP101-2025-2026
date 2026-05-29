import os
import time
import mss

from utils.gesture_action import GestureAction

class ScreenshotTaker(GestureAction):
    """Prend une capture d'écran déclenchée par geste."""

    def __init__(self, folder: str = "screenshots"):
        super().__init__("Screenshot")
        self.folder = folder
        os.makedirs(self.folder, exist_ok=True)
        print(f"Dossier '{self.folder}' prêt.")
        self.test_capture()

    def test_capture(self):
        try:
            test_file = os.path.join(self.folder, "test_capture.png")
            with mss.mss() as sct:
                sct.shot(output=test_file)
            if os.path.exists(test_file):
                os.remove(test_file)
                print("Test de capture réussi!")
            else:
                print("Erreur lors du test de capture")
        except Exception as e:
            print(f"ERREUR PERMISSIONS: {e}")

    def process(self, img, hands_data: list):
        """Interface polymorphe — déclenche une capture. Retourne (img, continuer)."""
        success = self.capture()
        return img, success

    def capture(self) -> bool:
        try:
            timestamp = time.strftime("%Y%m%d_%H%M%S")
            filename = os.path.join(self.folder, f"capture_{timestamp}.png")
            with mss.mss() as sct:
                sct.shot(output=filename)
            if os.path.exists(filename):
                print(f"Capture sauvegardée: {filename}")
                return True
            return False
        except Exception as e:
            print(f"ERREUR CAPTURE: {e}")
            return False


if __name__ == "__main__":
    taker = ScreenshotTaker()
    taker.capture()
