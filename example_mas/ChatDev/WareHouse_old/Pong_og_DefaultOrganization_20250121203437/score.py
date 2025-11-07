'''
Score class to keep track of the players' scores.
'''
import pygame
class Score:
    def __init__(self):
        self.font = pygame.font.Font(None, 74)
        self.score1 = 0
        self.score2 = 0
    def update(self, player):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1
    def draw(self, screen):
        score_text = self.font.render(f"{self.score1}  {self.score2}", True, (255, 255, 255))
        screen.blit(score_text, (350, 10))