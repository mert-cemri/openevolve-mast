'''
Settings class to store all settings for the Space Invaders game.
'''
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (230, 230, 230)
        self.ship_speed = 1.5
        self.shot_speed = 1.0
        self.alien_speed = 0.5
        self.alien_drop_speed = 10
        self.fleet_direction = 1  # 1 represents right; -1 represents left