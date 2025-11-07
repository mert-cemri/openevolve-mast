'''
Score class to manage and display the player's score.
'''
import pygame
class Score:
    def __init__(self):
        self.value = 0
        self.font = pygame.font.Font(None, 36)
    def update(self):
        self.value += 1
    def display(self):
        score_surface = self.font.render(f'Score: {self.value}', True, (255, 255, 255))
        pygame.display.get_surface().blit(score_surface, (10, 10))