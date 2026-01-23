"""
Module entities - Contient toutes les entités du jeu Snake
"""

from .entity import Entity
from .moving_entity import MovingEntity
from .snake_entity import Snake
from .food import Food

__all__ = ['Entity', 'MovingEntity', 'Snake', 'Food']
