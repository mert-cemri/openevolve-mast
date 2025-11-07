'''
Bird class to represent the bird character in the game.
'''
import pygame
from constants import *
class Bird:
    def __init__(self):
        self.x = BIRD_START_X
        self.y = BIRD_START_Y
        self.velocity = 0
    def flap(self):
        self.velocity = -FLAP_STRENGTH
    def update(self, game):
        self.velocity += GRAVITY
        self.y += self.velocity
        if self.y > SCREEN_HEIGHT - GROUND_HEIGHT:
            game.game_over()  # Call game over before setting the position
            self.y = SCREEN_HEIGHT - GROUND_HEIGHT
    def draw(self, screen):
        pygame.draw.circle(screen, BIRD_COLOR, (self.x, int(self.y)), BIRD_RADIUS)