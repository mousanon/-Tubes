class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # screen settings
        self.screen_width = 960
        self.screen_height = 720
        self.bg_color = (230, 230, 230)
        
        # ship settings
        self.ship_speed