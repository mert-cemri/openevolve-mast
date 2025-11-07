'''
Treasure class representing chests that restore player's HP.
'''
import pygame
import random
class Treasure:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.heal_amount = random.randint(20, 30)
    def render(self, screen, tile_size):
        rect = pygame.Rect(self.x * tile_size, self.y * tile_size, tile_size, tile_size)
        pygame.draw.rect(screen, (255, 215, 0), rect)