class Settings:
    """Una clase para almacenar todas las configuraciones para Alien Invasion."""

    def __init__(self):
        """Inicializa las configuraciones estáticas del juego."""
        # Configuraciones de pantalla
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Configuraciones del barco
        self.ship_limit = 3

        # Configuraciones de la bala
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 3

        # Configuraciones del alienígena
        self.fleet_drop_speed = 10

        # La velocidad a la que el juego se acelera
        self.speedup_scale = 1.1
        # La velocidad a la que aumentan los valores de puntos del alienígena
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Inicializa configuraciones que cambian a lo largo del juego."""
        self.ship_speed = 1.5
        self.bullet_speed = 2.5
        self.alien_speed = 1.0

        # fleet_direction de 1 representa a la derecha; -1 representa a la izquierda.
        self.fleet_direction = 1

        # Scoring settings
        self.alien_points = 50

    def increase_speed(self):
        """Aumenta la configuración de velocidad y los valores de puntos del alienígena."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)