'''
Bullet class to represent a bullet fired by the player. Handles movement and drawing.
'''
import pygame
class Bullet:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(midbottom=(x, y))
        self.speed = -10
    def move(self):
        self.rect.y += self.speed
    def draw(self):
        self.screen.blit(self.image, self.rect)