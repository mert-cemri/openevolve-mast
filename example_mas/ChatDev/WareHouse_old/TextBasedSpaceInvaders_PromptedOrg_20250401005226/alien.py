'''
Represents alien enemy.
'''
import pygame
from pygame.sprite import Sprite
class Alien(Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
    def update(self):
        """Move the alien horizontally based on fleet direction."""
        self.x += self.settings.alien_speed_x * self.settings.fleet_direction
        self.rect.x = self.x