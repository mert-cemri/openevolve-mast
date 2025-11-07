'''
Paddle class for the Pong game.
'''
import pygame
WHITE = (255, 255, 255)
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 120
PADDLE_SPEED = 5
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, PADDLE_WIDTH, PADDLE_HEIGHT)
    def move(self, up=True):
        if up:
            self.rect.y -= PADDLE_SPEED
        else:
            self.rect.y += PADDLE_SPEED
        # Ensure paddle stays on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > pygame.display.get_surface().get_height():
            self.rect.bottom = pygame.display.get_surface().get_height()
    def draw(self, screen):
        pygame.draw.rect(screen, WHITE, self.rect)