"""
Module game - Classe principale du jeu Snake
"""

import pygame
from entities import Snake, Food, MovingEntity


class Game:
    """Classe principale du jeu Snake."""

    def __init__(self, width=800, height=600):
        try:
            # Validation minimale des dimensions
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise TypeError("Les dimensions doivent être des nombres")
            if width <= 0 or height <= 0:
                raise ValueError("Les dimensions doivent être positives")

            pygame.init()

            # Fenêtre et ressources principales
            self.width = int(width)
            self.height = int(height)
            self.screen = pygame.display.set_mode((self.width, self.height))
            pygame.display.set_caption("Snake Game - TP04")
            self.clock = pygame.time.Clock()

            # Etat du jeu
            self.running = True
            self.game_state = "menu"
            self.game_over = False
            self.paused = False
            self.score = 0

            # Polices (réutilisées dans les écrans)
            self._font = pygame.font.Font(None, 36)
            self._big_font = pygame.font.Font(None, 72)
            self._title_font = pygame.font.Font(None, 84)

            # Création des entités
            self._initialize_entities()
        except pygame.error as e:
            raise RuntimeError(f"Erreur Pygame lors de l'initialisation: {e}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'initialisation du jeu: {e}")

    def _initialize_entities(self):
        try:
            # Position de départ alignée sur la grille
            start_x = (self.width // 2 // MovingEntity.CELL_SIZE) * MovingEntity.CELL_SIZE
            start_y = (self.height // 2 // MovingEntity.CELL_SIZE) * MovingEntity.CELL_SIZE
            self.snake = Snake(start_x, start_y)
            self.food = Food(self.width, self.height)

            # Liste pour le polymorphisme update/draw
            self.entities = [self.food, self.snake]
            self.food.respawn(self.snake.get_body())
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'initialisation des entités: {e}")

    def reset_game(self):
        try:
            # Réinitialiser l'état et recréer les entités
            self.game_over = False
            self.score = 0
            self.game_state = "running"
            self._initialize_entities()
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la réinitialisation: {e}")

    def handle_events(self):
        try:
            for event in pygame.event.get():
                # Fermeture de la fenêtre
                if event.type == pygame.QUIT:
                    self.running = False
                    return
                # Gestion clavier
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        self.running = False
                        return
                    if self.game_state == "menu":
                        if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                            self.reset_game()
                    elif self.game_state == "running":
                        if event.key == pygame.K_p:
                            self.paused = True
                            self.game_state = "paused"
                        else:
                            self._handle_direction(event.key)
                    elif self.game_state == "paused":
                        if event.key == pygame.K_p:
                            self.paused = False
                            self.game_state = "running"
                    elif self.game_state == "game_over":
                        if event.key in (pygame.K_SPACE, pygame.K_RETURN):
                            self.reset_game()
                        elif event.key == pygame.K_m:
                            self.game_state = "menu"
        except pygame.error as e:
            raise RuntimeError(f"Erreur Pygame lors des événements: {e}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la gestion des événements: {e}")

    def _handle_direction(self, key):
        try:
            # Table de correspondance touches -> vecteur
            directions = {
                pygame.K_UP: (0, -MovingEntity.CELL_SIZE),
                pygame.K_DOWN: (0, MovingEntity.CELL_SIZE),
                pygame.K_LEFT: (-MovingEntity.CELL_SIZE, 0),
                pygame.K_RIGHT: (MovingEntity.CELL_SIZE, 0),
            }
            if key in directions and not self.game_over:
                dx, dy = directions[key]
                self.snake.set_direction(dx, dy)
        except Exception as e:
            raise RuntimeError(f"Erreur lors du changement de direction: {e}")

    def update(self):
        try:
            # Pas de mise à jour en menu, pause ou game over
            if self.game_state != "running":
                return

            # Mise à jour des entités
            for e in self.entities:
                e.update(self)

            # Passage à l'état game over si besoin
            if self.game_over:
                self.game_state = "game_over"
                return

            # Collision serpent/nourriture
            if self.snake.get_head_pos() == self.food.pos():
                self.snake.grow(1)
                self.score += 10
                self.food.respawn(self.snake.get_body())
        except Exception as e:
            raise RuntimeError(f"Erreur lors de la mise à jour du jeu: {e}")

    def draw(self):
        try:
            # Fond noir
            self.screen.fill((0, 0, 0))

            if self.game_state == "menu":
                self._draw_menu()
            elif self.game_state == "paused":
                self._draw_game_elements()
                self._draw_pause()
            else:
                self._draw_game_elements()
                self._draw_pause_info()
                if self.game_state == "game_over":
                    self._draw_game_over()

            pygame.display.flip()
        except pygame.error as e:
            raise RuntimeError(f"Erreur Pygame lors du dessin: {e}")
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin: {e}")

    def _draw_game_elements(self):
        try:
            # Dessiner les entités
            for e in self.entities:
                e.draw(self.screen)

            # Score en haut à gauche
            score_text = self._font.render(f"Score: {self.score}", True, (255, 255, 255))
            self.screen.blit(score_text, (10, 10))
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin des éléments: {e}")

    def _draw_pause_info(self):
        try:
            info_font = pygame.font.Font(None, 20)
            info_text = info_font.render("P: Pause", True, (150, 150, 150))
            self.screen.blit(info_text, (self.width - 80, 10))
        except Exception as e:
            raise RuntimeError(f"Erreur lors de l'affichage de l'info pause: {e}")

    def _draw_menu(self):
        try:
            title_font = pygame.font.Font(None, 84)
            title_text = title_font.render("SNAKE GAME", True, (0, 255, 0))
            title_rect = title_text.get_rect(center=(self.width // 2, self.height // 3))
            self.screen.blit(title_text, title_rect)

            start_font = pygame.font.Font(None, 32)
            start_text = start_font.render("Appuyez sur ESPACE pour commencer", True, (255, 255, 255))
            start_rect = start_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(start_text, start_rect)

            controls_font = pygame.font.Font(None, 24)
            controls = [
                "Fleches: Diriger le serpent",
                "P: Pause",
                "ESC: Quitter",
            ]
            y_offset = self.height // 2 + 80
            for control in controls:
                control_text = controls_font.render(control, True, (200, 200, 200))
                control_rect = control_text.get_rect(center=(self.width // 2, y_offset))
                self.screen.blit(control_text, control_rect)
                y_offset += 30

        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin du menu: {e}")

    def _draw_pause(self):
        try:
            overlay = pygame.Surface((self.width, self.height))
            overlay.set_alpha(128)
            overlay.fill((0, 0, 0))
            self.screen.blit(overlay, (0, 0))

            pause_text = self._big_font.render("PAUSE", True, (255, 255, 0))
            pause_rect = pause_text.get_rect(center=(self.width // 2, self.height // 2))
            self.screen.blit(pause_text, pause_rect)

            info_text = self._font.render("Appuyez sur P pour continuer", True, (255, 255, 255))
            info_rect = info_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            self.screen.blit(info_text, info_rect)
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin de la pause: {e}")

    def _draw_game_over(self):
        try:
            game_over_text = self._big_font.render("GAME OVER", True, (255, 0, 0))
            text_rect = game_over_text.get_rect(center=(self.width // 2, self.height // 2 - 30))
            self.screen.blit(game_over_text, text_rect)

            score_text = self._font.render(f"Score final: {self.score}", True, (255, 255, 255))
            score_rect = score_text.get_rect(center=(self.width // 2, self.height // 2 + 10))
            self.screen.blit(score_text, score_rect)

            restart_text = self._font.render("ESPACE: rejouer | M: menu | ESC: quitter", True, (200, 200, 200))
            restart_rect = restart_text.get_rect(center=(self.width // 2, self.height // 2 + 50))
            self.screen.blit(restart_text, restart_rect)
        except Exception as e:
            raise RuntimeError(f"Erreur lors du dessin du game over: {e}")

    def run(self):
        try:
            while self.running:
                # Limiter la vitesse du jeu
                self.clock.tick(MovingEntity.DEFAULT_SPEED)
                self.handle_events()
                self.update()
                self.draw()
        except KeyboardInterrupt:
            print("\nJeu interrompu par l'utilisateur")
        except Exception as e:
            raise RuntimeError(f"Erreur dans la boucle de jeu: {e}")
        finally:
            pygame.quit()
