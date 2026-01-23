"""
Module entity - Classe de base pour toutes les entités du jeu
"""


class Entity:
    """
    Classe de base pour toutes les entités du jeu.
    Définit l'interface commune avec update() et draw().
    """

    def update(self, game):
        """
        Met à jour l'état de l'entité.

        Args:
            game: Instance de la classe Game

        Raises:
            NotImplementedError: Si la méthode n'est pas implémentée par la sous-classe
        """
        pass

    def draw(self, screen):
        """
        Dessine l'entité sur l'écran.

        Args:
            screen: Surface Pygame sur laquelle dessiner

        Raises:
            NotImplementedError: Si la méthode n'est pas implémentée par la sous-classe
        """
        pass
