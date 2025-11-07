'''
Scoreboard class for displaying scores.
'''
import pygame
# Constants
FONT_SIZE = 36
FONT_COLOR = (255, 255, 255)
SCREEN_WIDTH = 800
class Scoreboard:
    def __init__(self):
        self.font = pygame.font.Font(None, FONT_SIZE)
        self.score1 = 0
        self.score2 = 0
    def update_score(self, player):
        if player == 1:
            self.score1 += 1
        else:
            self.score2 += 1
    def draw(self, screen):
        score_text = f"{self.score1} - {self.score2}"
        text = self.font.render(score_text, True, FONT_COLOR)
        text_rect = text.get_rect(center=(SCREEN_WIDTH // 2, 50))
        screen.blit(text, text_rect)