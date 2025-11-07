'''
Paddle class for player control.
'''
import pygame
# Constants
PADDLE_WIDTH, PADDLE_HEIGHT = 10, 120
PADDLE_COLOR = (255, 255, 255)
SCREEN_HEIGHT = 600
PADDLE_SPEED = 5
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def move_up(self):
        if self.rect.top > 0:
            self.rect.y -= PADDLE_SPEED
    def move_down(self):
        if self.rect.bottom < SCREEN_HEIGHT:
            self.rect.y += PADDLE_SPEED
    def draw(self, screen):
        pygame.draw.rect(screen, PADDLE_COLOR, self.rect)