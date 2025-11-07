'''
Paddle class to represent the paddles controlled by the players.
'''
import pygame
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
    def move(self, up=True):
        if up:
            self.rect.y -= 5
        else:
            self.rect.y += 5
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)