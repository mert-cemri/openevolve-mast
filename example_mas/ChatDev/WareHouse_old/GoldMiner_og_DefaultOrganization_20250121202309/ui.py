'''
UI class that handles the display of game information.
'''
import pygame
class UI:
    def __init__(self, screen):
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
    def draw_score(self, score):
        score_text = self.font.render(f"Score: {score}", True, (255, 255, 255))
        self.screen.blit(score_text, (10, 10))
    def draw_timer(self, time_remaining):
        timer_text = self.font.render(f"Time: {int(time_remaining)}", True, (255, 255, 255))
        self.screen.blit(timer_text, (700, 10))