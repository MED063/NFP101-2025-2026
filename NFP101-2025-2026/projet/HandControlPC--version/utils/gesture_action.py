from abc import ABC, abstractmethod
import cv2

# ############### CODE IA (Claude) ################
class GestureAction(ABC):
    """Classe de base abstraite pour toutes les actions gestuelles."""

    def __init__(self, name: str):
        self.name = name
        self.active = False

    @abstractmethod
    def process(self, img, hands_data: list):
        """
        Traite un frame et retourne (img, continuer_mode).
        Chaque sous-classe implémente sa propre logique.
        """
        pass

    def activate(self):
        self.active = True

    def deactivate(self):
        self.active = False

    def render_hud(self, img, text: str, pos=(40, 150), color=(0, 255, 255)):
        """Affiche un texte HUD commun à tous les modes."""
        cv2.putText(img, f"[{self.name}] {text}", pos,
                    cv2.FONT_HERSHEY_SIMPLEX, 0.8, color, 2)
        return img
# ########################################
