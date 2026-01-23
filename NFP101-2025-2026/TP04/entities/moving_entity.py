"""
Module moving_entity - Classe pour les entités en mouvement
"""

from .entity import Entity


class MovingEntity(Entity):
    """Classe pour les entités en mouvement."""

    CELL_SIZE = 20
    DEFAULT_SPEED = 10

    def __init__(self):
        """Initialise une entité mobile avec une direction par défaut."""
        self._dx = self.CELL_SIZE
        self._dy = 0

    @classmethod
    def set_cell_size(cls, value):
        """Définit la taille de la cellule pour toutes les entités mobiles."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"CELL_SIZE invalide: {value}")
        cls.CELL_SIZE = int(value)

    @classmethod
    def set_default_speed(cls, value):
        """Définit la vitesse par défaut pour toutes les entités mobiles."""
        if not isinstance(value, (int, float)) or value <= 0:
            raise ValueError(f"DEFAULT_SPEED invalide: {value}")
        cls.DEFAULT_SPEED = int(value)

    def set_direction(self, dx, dy):
        """Met à jour la direction de déplacement."""
        self._dx = dx
        self._dy = dy
