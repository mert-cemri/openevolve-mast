'''
Monster class representing enemy entities.
'''
import pygame
import random
class Monster:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.hp = random.randint(10, 30)
    def render(self, screen, tile_size):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)