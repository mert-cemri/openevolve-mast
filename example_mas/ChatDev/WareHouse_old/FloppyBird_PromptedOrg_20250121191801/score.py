'''
Score module to handle the scoring system.
'''
import pygame
from constants import SCORE_COLOR, SCREEN_WIDTH
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.SysFont(None, 36)
    def increase(self):
        self.value += 1
    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.value}', True, SCORE_COLOR)
        screen.blit(score_surface, (SCREEN_WIDTH - 150, 10))