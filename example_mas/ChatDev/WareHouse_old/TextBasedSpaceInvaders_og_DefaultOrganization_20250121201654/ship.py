'''
Ship class to manage the player's ship.
'''
import pygame
from shot import Shot
class Ship:
    def __init__(self, game):
        self.game = game  # Store the game reference
        self.screen = game.screen
        self.settings = game.settings
        self.screen_rect = game.screen.get_rect()
        # Load a default image if 'ship.bmp' is not found
        try:
            self.image = pygame.image.load('ship.bmp')
        except FileNotFoundError:
            self.image = pygame.Surface((50, 30))  # Create a simple rectangle as a placeholder
            self.image.fill((255, 0, 0))  # Fill it with red color
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen_rect.midbottom
        self.x = float(self.rect.x)
        self.moving_right = False
        self.moving_left = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def blitme(self):
        self.screen.blit(self.image, self.rect)
    def fire_shot(self):
        new_shot = Shot(self)
        self.game.shots.add(new_shot)