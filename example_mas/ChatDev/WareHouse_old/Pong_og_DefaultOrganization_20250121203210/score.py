'''
Score class to keep track of the players' scores.
'''
import pygame
class Score:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, 74)
    def increase_score(self, player):
        if player == 1:
            self.player1_score += 1
        elif player == 2:
            self.player2_score += 1
    def draw(self, screen):
        score_text = self.font.render(f"{self.player1_score} - {self.player2_score}", True, (255, 255, 255))
        screen.blit(score_text, (350, 10))