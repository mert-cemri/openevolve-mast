'''
Stores settings for Space Invaders game.
'''
class Settings:
    def __init__(self):
        self.screen_width = 800
        self.screen_height = 600
        self.bg_color = (0, 0, 0)
        self.ship_speed = 5
        self.bullet_speed = 6
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (255, 255, 255)
        self.bullets_allowed = 3
        self.alien_speed_x = 1.0  # Horizontal speed of aliens
        self.fleet_direction = 1  # 1 represents right; -1 represents left
        self.fleet_drop_speed = 10  # Vertical drop distance when fleet hits edge
        self.lives_limit = 3