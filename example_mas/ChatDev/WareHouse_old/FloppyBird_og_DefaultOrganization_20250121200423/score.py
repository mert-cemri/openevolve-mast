'''
Score class for managing and displaying the score.
'''
import pygame
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
    def increase(self):
        self.value += 1
    def draw(self, screen):
        score_surface = self.font.render(f'Score: {self.value}', True, (255, 255, 255))
        screen.blit(score_surface, (10, 10))