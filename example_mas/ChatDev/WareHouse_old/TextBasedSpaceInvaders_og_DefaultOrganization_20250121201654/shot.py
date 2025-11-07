'''
Shot class to manage shots fired from the ship.
'''
import pygame
from pygame.sprite import Sprite
class Shot(Sprite):
    def __init__(self, ship):
        super().__init__()
        self.screen = ship.screen
        self.settings = ship.settings
        self.color = (60, 60, 60)
        self.rect = pygame.Rect(0, 0, 3, 15)
        self.rect.midtop = ship.rect.midtop
        self.y = float(self.rect.y)
    def update(self):
        self.y -= self.settings.shot_speed
        self.rect.y = self.y
    def draw_shot(self):
        pygame.draw.rect(self.screen, self.color, self.rect)