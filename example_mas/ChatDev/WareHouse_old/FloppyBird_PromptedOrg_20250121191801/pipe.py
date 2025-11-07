'''
Pipe module to represent the pipes in the game.
'''
import pygame
import random
from constants import PIPE_COLOR, PIPE_WIDTH, PIPE_GAP, SCREEN_HEIGHT, SCREEN_WIDTH
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.height = random.randint(100, SCREEN_HEIGHT - PIPE_GAP - 100)
        self.passed = False
    def update(self):
        self.x -= 5
    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.height))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.height + PIPE_GAP, PIPE_WIDTH, SCREEN_HEIGHT))
    def is_colliding(self, bird):
        if bird.x + 10 > self.x and bird.x - 10 < self.x + PIPE_WIDTH:
            if bird.y - 10 < self.height or bird.y + 10 > self.height + PIPE_GAP:
                return True
        return False