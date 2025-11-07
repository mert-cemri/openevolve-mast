'''
Paddle class to represent player paddles and handle movement and rendering.
'''
import pygame
class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 100)
        self.speed = 5
    def move(self, keys, up_key, down_key):
        if keys[up_key]:
            self.rect.y -= self.speed
        if keys[down_key]:
            self.rect.y += self.speed
        self.rect.y = max(0, min(self.rect.y, 500))
    def render(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)