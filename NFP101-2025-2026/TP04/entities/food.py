"""
Module food - Classe représentant la nourriture
"""

import pygame
import random
from .entity import Entity
from .moving_entity import MovingEntity


class Food(Entity):
    """Classe représentant la nourriture du jeu."""

    def __init__(self, width=800, height=600):
        """Initialise la nourriture à une position aléatoire alignée sur la grille."""
        self._width = int(width)
        self._height = int(height)
        self._x = 0
        self._y = 0
        self.respawn()

    def pos(self):
        """Retourne la position de la nourriture."""
        return (self._x, self._y)

    def respawn(self, snake_body=None):
        """
        Repositionne la nourriture à une position aléatoire alignée sur la grille.
        Évite de spawner sur le serpent si snake_body est fourni (bonus).
        """
        # ############### CODE IA ################
        # Calculer le nombre de cellules disponibles
        cells_x = self._width // MovingEntity.CELL_SIZE
        cells_y = self._height // MovingEntity.CELL_SIZE

        # Si pas de corps de serpent, spawn aléatoire simple
        if snake_body is None:
            cell_x = random.randint(0, cells_x - 1)
            cell_y = random.randint(0, cells_y - 1)
            self._x = cell_x * MovingEntity.CELL_SIZE
            self._y = cell_y * MovingEntity.CELL_SIZE
            return

        # Éviter de spawner sur le serpent (bonus)
        for _ in range(100):  # Max 100 tentatives
            cell_x = random.randint(0, cells_x - 1)
            cell_y = random.randint(0, cells_y - 1)
            new_x = cell_x * MovingEntity.CELL_SIZE
            new_y = cell_y * MovingEntity.CELL_SIZE

            if (new_x, new_y) not in snake_body:
                self._x = new_x
                self._y = new_y
                return

        # Si toutes les tentatives échouent, utiliser la dernière position
        self._x = new_x
        self._y = new_y
        # ########################################

    def update(self, game):
        """Met à jour la nourriture (ne fait rien)."""
        pass

    def draw(self, screen):
        """Dessine la nourriture sur l'écran."""
        pygame.draw.rect(screen, (255, 0, 0),
                        (self._x, self._y, MovingEntity.CELL_SIZE, MovingEntity.CELL_SIZE))
        pygame.draw.rect(screen, (0, 0, 0),
                        (self._x, self._y, MovingEntity.CELL_SIZE, MovingEntity.CELL_SIZE), 1)
