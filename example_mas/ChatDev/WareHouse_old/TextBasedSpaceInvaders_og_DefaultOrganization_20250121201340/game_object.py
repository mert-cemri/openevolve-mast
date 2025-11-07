'''
Base class for all game objects (Player, Alien, Bullet).
'''
import pygame
class GameObject:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(x, y, width, height)
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)