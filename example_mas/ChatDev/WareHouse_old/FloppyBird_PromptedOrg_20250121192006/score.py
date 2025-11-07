'''
Score class to manage the player's score.
'''
import pygame
from constants import *
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont(None, SCORE_FONT_SIZE)
    def increment(self):
        self.value += 1
    def reset(self):
        self.value = 0
    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.value}', True, SCORE_COLOR)
        screen.blit(score_surface, SCORE_POSITION)