import pygame
from pygame.sprite import Sprite


class Ship(Sprite):
    """Una clase para administrar la nave."""

    def __init__(self, ai_game):
        """Inicializa la nave y establece su posición inicial."""
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings
        self.screen_rect = ai_game.screen.get_rect()

        # Carga la imagen de la nave y obtiene su rectángulo.
        self.image = pygame.image.load('images/ship.bmp')
        self.rect = self.image.get_rect()

        # Inicia cada nueva nave en la parte inferior centro de la pantalla.
        self.rect.midbottom = self.screen_rect.midbottom

        # Almacena un float para la posición horizontal exacta de la nave.
        self.x = float(self.rect.x)

        # Movement flags; comienza con una nave que no se está moviendo..
        self.moving_right = False
        self.moving_left = False

    def center_ship(self):
        """Centra la nave en la pantalla."""
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)

    def update(self):
        """Actualiza la posición de la nave en base a las movement flags"""
        # Actualiza el valor x de la nave, no el rectángulo.
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
            
        # Actualiza el objeto rectángulo desde self.x.
        self.rect.x = self.x

    def blitme(self):
        """Dibuja la nave en su posición actual."""
        self.screen.blit(self.image, self.rect)