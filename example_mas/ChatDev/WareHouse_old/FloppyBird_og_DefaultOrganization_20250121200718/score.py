'''
Score tracking and display.
'''
import pygame
# Constants
FONT_SIZE = 32
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, FONT_SIZE)
    def increment(self):
        self.value += 1
    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.value}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))