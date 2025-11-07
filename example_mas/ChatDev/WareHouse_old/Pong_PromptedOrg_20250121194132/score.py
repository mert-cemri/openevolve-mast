'''
Score class to manage and render the score for each player.
'''
import pygame
class Score:
    def __init__(self):
        self.player1 = 0
        self.player2 = 0
        self.font = pygame.font.Font(None, 74)
    def render(self, screen):
        score_text = self.font.render(f"{self.player1}  {self.player2}", True, (255, 255, 255))
        screen.blit(score_text, (350, 10))