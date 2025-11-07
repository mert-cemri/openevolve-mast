'''
Tracks and displays player's score and remaining lives.
'''
import pygame
class Scoreboard:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.score = 0
        self.lives = self.settings.lives_limit
        self.font = pygame.font.SysFont(None, 36)
    def increase_score(self, points):
        self.score += points
    def decrease_life(self):
        self.lives -= 1
    def is_game_over(self):
        return self.lives <= 0
    def draw(self):
        score_img = self.font.render(f"Score: {self.score}", True, (255, 255, 255))
        lives_img = self.font.render(f"Lives: {self.lives}", True, (255, 255, 255))
        self.screen.blit(score_img, (20, 20))
        self.screen.blit(lives_img, (20, 60))