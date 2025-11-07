'''
Defines the Food class, which represents the food items in the game.
'''
import pygame
from utils import random_position
class Food:
    def __init__(self):
        self.position = random_position()
    def spawn(self, snake_body):
        while True:
            new_position = random_position()
            if new_position not in snake_body:
                self.position = new_position
                break
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 0, 0), (*self.position, 10, 10))