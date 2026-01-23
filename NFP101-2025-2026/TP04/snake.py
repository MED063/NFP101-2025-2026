#!/usr/bin/env python3
"""
Jeu du Snake - TP04 noté
Point d'entrée principal du jeu

Auteur: Mohamed
Module: NFP101 2025-2026
Date limite de rendu: 23/01/2026 à 23h59
"""

import sys
from game import Game


def main():
    """
    Fonction principale du jeu.
    Initialise et lance le jeu.
    """
    game = None

    try:
        game = Game(width=800, height=600)
        game.run()
        return 0

    except ImportError as e:
        print(f"\nERREUR: Module manquant - {e}")
        print("Installez pygame: pip install pygame")
        return 1

    except KeyboardInterrupt:
        print("\n\nJeu interrompu par l'utilisateur (Ctrl+C)")
        return 0

    except Exception as e:
        print(f"\nERREUR: {e}")
        return 1

    finally:
        if game is not None:
            try:
                import pygame
                pygame.quit()
            except Exception:
                pass


if __name__ == "__main__":
    exit_code = main()
    sys.exit(exit_code)
