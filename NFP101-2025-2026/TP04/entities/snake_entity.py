"""
Module snake_entity - Classe représentant le serpent
"""

import pygame
from .moving_entity import MovingEntity


class Snake(MovingEntity):
    """Classe représentant le serpent du jeu."""

    def __init__(self, x, y):
        """Initialise le serpent à une position donnée."""
        super().__init__()
        self._body = [(int(x), int(y))]
        self._grow_pending = 0

    def get_head_pos(self):
        """Retourne la position de la tête du serpent."""
        return self._body[0]

    def get_body(self):
        """Retourne une copie du corps du serpent (encapsulation)."""
        return self._body.copy()

    def grow(self, n):
        """Fait grandir le serpent de n segments."""
        self._grow_pending += n

    def set_direction(self, dx, dy):
        """
        Met à jour la direction de déplacement.
        Empêche le demi-tour instantané.
        """
        # Empêcher le demi-tour instantané
        if (self._dx > 0 and dx < 0) or (self._dx < 0 and dx > 0):
            return
        if (self._dy > 0 and dy < 0) or (self._dy < 0 and dy > 0):
            return

        super().set_direction(dx, dy)

    def update(self, game):
        """
        Met à jour la position du serpent.
        Gère le déplacement, la croissance et les collisions.
        """
        if game.game_over:
            return

        # Calculer la nouvelle position de la tête
        head_x, head_y = self._body[0]
        new_head = (head_x + self._dx, head_y + self._dy)

        # Vérifier les collisions avec les murs
        if (new_head[0] < 0 or new_head[0] >= game.width or
            new_head[1] < 0 or new_head[1] >= game.height):
            game.game_over = True
            return

        # Vérifier les collisions avec le corps
        if new_head in self._body[1:]:
            game.game_over = True
            return

        # Ajouter la nouvelle tête
        self._body.insert(0, new_head)

        # Gérer la croissance
        if self._grow_pending > 0:
            self._grow_pending -= 1
        else:
            self._body.pop()

    def draw(self, screen):
        """Dessine le serpent sur l'écran."""
        for i, (x, y) in enumerate(self._body):
            # Tête en vert clair, corps en vert foncé
            color = (0, 200, 0) if i == 0 else (0, 150, 0)

            pygame.draw.rect(screen, color, (x, y, self.CELL_SIZE, self.CELL_SIZE))
            pygame.draw.rect(screen, (0, 0, 0), (x, y, self.CELL_SIZE, self.CELL_SIZE), 1)
