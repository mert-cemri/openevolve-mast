'''
Bird module to represent the bird character.
'''
import pygame
from constants import BIRD_COLOR, BIRD_START_X, BIRD_START_Y, GRAVITY, FLAP_STRENGTH
class Bird:
    def __init__(self):
        self.x = BIRD_START_X
        self.y = BIRD_START_Y
        self.velocity = 0
    def flap(self):
        self.velocity = -FLAP_STRENGTH
    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity
    def draw(self, screen):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), 10)