'''
This module contains the Player class, which represents the player's ship.
'''
import pygame
from shot import Shot
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(midbottom=(400, 580))
    def move(self, direction):
        self.rect.x += direction * 10
        self.rect.x = max(0, min(self.rect.x, self.screen.get_width() - self.rect.width))
    def fire(self):
        return Shot(self.screen, self.rect.centerx, self.rect.top)
    def draw(self):
        self.screen.blit(self.image, self.rect)