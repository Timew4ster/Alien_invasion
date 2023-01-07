import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
    """Una clase para administrar las balas disparadas desde el barco."""

    def __init__(self, ai_game):
        """Crea un objeto bala en la posición actual del barco."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.color = self.settings.bullet_color

        # Crea una bala en (0, 0) y luego establece la posición correcta.
        self.rect = pygame.Rect(0, 0, self.settings.bullet_width,
            self.settings.bullet_height)
        self.rect.midtop = ai_game.ship.rect.midtop

        # Almacena la posición de la bala como un float.
        self.y = float(self.rect.y)

    def update(self):
        """Mueve la bala hacia arriba en la pantalla."""
        # Actualiza la posición exacta de la bala.
        self.y -= self.settings.bullet_speed
        # Actualiza la posición del rectángulo.
        self.rect.y = self.y

    def draw_bullet(self):
        """Dibuja la bala en la pantalla."""
        pygame.draw.rect(self.screen, self.color, self.rect)