class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 966     # mengubah lebar layar dari 1200 menjadi 966
        self.screen_height = 750    # mengubah tinggi layar dari 800 menjadi 750
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_limit = 3

        # Bullet settings
        self.bullet_width = 6       # mengubah lebar bullet menjadi 6
        self.bullet_height = 30     # mengubah tinggi bullet menjadi 30
        self.bullet_color = (250, 0, 0)    # mengubah warna peluru dari abu-abu (60, 60 ,60) menjadi merah
        self.bullets_allowed = 3

        # Alien settings
        self.fleet_drop_speed = 7   # mengubah kecepatan fleet menuju bottom dari 10 menjadi 7

        # How quickly the game speeds up
        self.speedup_scale = 1.1
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        self.ship_speed = 2.0      # mengubah kecepatan ship dari 1.5 menjadi 2.0
        self.bullet_speed = 2.5    # mengubah kecepatan bullet dari 3.0 menjadi 2.5
        self.alien_speed = 1.5     # mengubah kecepatan alien dari 1.0 menjadi 1.5

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = -1   # mengubah arah alien dari kiri ke kanan menjadi kanan ke kiri

        # Scoring
        self.alien_points = 50

    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
