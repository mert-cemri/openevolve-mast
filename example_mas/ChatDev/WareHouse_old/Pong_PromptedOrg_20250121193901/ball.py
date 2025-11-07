'''
Ball class to represent the ball, manage its movement, collision detection, and scoring.
'''
import pygame
import random
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])
    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
    def bounce(self):
        self.speed_x *= -1
    def reset(self):
        self.rect.x = 400
        self.rect.y = 300
        self.speed_x = random.choice([-1, 1]) * random.randint(4, 6)
        self.speed_y = random.choice([-1, 1]) * random.randint(4, 6)
    def render(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)