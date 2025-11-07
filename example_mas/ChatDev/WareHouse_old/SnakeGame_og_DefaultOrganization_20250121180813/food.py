'''
Food class to manage food behavior.
'''
import pygame
import random
class Food:
    def __init__(self):
        self.position = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)
        self.color = (255, 0, 0)
    def randomize_position(self):
        self.position = (random.randint(0, 29) * 20, random.randint(0, 19) * 20)
    def draw(self, surface, grid_size):
        rect = pygame.Rect(self.position[0], self.position[1], grid_size, grid_size)
        pygame.draw.rect(surface, self.color, rect)