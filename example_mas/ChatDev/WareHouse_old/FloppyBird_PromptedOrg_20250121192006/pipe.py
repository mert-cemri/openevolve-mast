'''
Pipe class to represent the pipes in the game.
'''
import pygame
import random
from constants import *
class Pipe:
    def __init__(self):
        self.x = SCREEN_WIDTH
        self.gap_y = random.randint(PIPE_GAP_MIN, PIPE_GAP_MAX)
        self.passed = False
    def update(self):
        self.x -= PIPE_SPEED
    def is_off_screen(self):
        return self.x < -PIPE_WIDTH
    def collides_with(self, bird):
        if bird.x + BIRD_RADIUS > self.x and bird.x - BIRD_RADIUS < self.x + PIPE_WIDTH:
            if bird.y - BIRD_RADIUS < self.gap_y or bird.y + BIRD_RADIUS > self.gap_y + PIPE_GAP_SIZE:
                return True
        return False
    def passed_by(self, bird):
        if not self.passed and self.x + PIPE_WIDTH < bird.x:
            self.passed = True
            return True
        return False
    def draw(self, screen):
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, 0, PIPE_WIDTH, self.gap_y))
        pygame.draw.rect(screen, PIPE_COLOR, (self.x, self.gap_y + PIPE_GAP_SIZE, PIPE_WIDTH, SCREEN_HEIGHT))