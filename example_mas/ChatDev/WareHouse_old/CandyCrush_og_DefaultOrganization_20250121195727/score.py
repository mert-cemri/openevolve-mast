'''
Score tracking for the match-3 game.
'''
import pygame
class Score:
    def __init__(self):
        self.score = 0
        self.font = pygame.font.SysFont(None, 36)
    def update_score(self, cleared_matches):
        self.score += len(cleared_matches) * 10
    def draw(self, screen):
        score_text = self.font.render(f"Score: {self.score}", True, (0, 0, 0))
        screen.blit(score_text, (10, 10))