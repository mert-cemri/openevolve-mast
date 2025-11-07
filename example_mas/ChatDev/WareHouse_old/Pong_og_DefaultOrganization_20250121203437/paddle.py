'''
Paddle class to represent player paddles.
'''
import pygame
class Paddle:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = 10
    def move(self, up):
        if up:
            self.rect.y -= self.speed
        else:
            self.rect.y += self.speed
        # Keep paddle on screen
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > 600:
            self.rect.bottom = 600
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)