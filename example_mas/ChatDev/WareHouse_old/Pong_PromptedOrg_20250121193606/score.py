'''
Score class for the Pong game.
'''
import pygame
WHITE = (255, 255, 255)
FONT_SIZE = 36
class Score:
    def __init__(self):
        self.player1_score = 0
        self.player2_score = 0
        self.font = pygame.font.Font(None, FONT_SIZE)
    def increment_player1(self):
        self.player1_score += 1
    def increment_player2(self):
        self.player2_score += 1
    def draw(self, screen, screen_width):
        score_text = f"{self.player1_score} : {self.player2_score}"
        text = self.font.render(score_text, True, WHITE)
        screen.blit(text, (screen_width // 2 - text.get_width() // 2, 20))