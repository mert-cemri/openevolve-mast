'''
Ball class to represent the ball, handle movement, collision detection, and scoring.
'''
import pygame
import random
class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 15, 15)
        self.speed_x = random.choice([-5, 5])
        self.speed_y = random.choice([-5, 5])
        # Ensure the ball doesn't move strictly horizontally
        while self.speed_y == 0:
            self.speed_y = random.choice([-5, 5])
    def move(self, paddle1, paddle2, score):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            self.speed_y *= -1
        if self.rect.colliderect(paddle1.rect) or self.rect.colliderect(paddle2.rect):
            self.speed_x *= -1
        if self.rect.left <= 0:
            score.player2 += 1
            self.reset()
        if self.rect.right >= 800:
            score.player1 += 1
            self.reset()
    def reset(self):
        self.rect.x, self.rect.y = 400, 300
        # Introduce variability in speed
        self.speed_x = random.choice([-5, 5]) * random.uniform(1.0, 1.2)
        self.speed_y = random.choice([-5, 5]) * random.uniform(1.0, 1.2)
        # Ensure the ball doesn't move strictly horizontally
        while self.speed_y == 0:
            self.speed_y = random.choice([-5, 5]) * random.uniform(1.0, 1.2)
    def render(self, screen):
        pygame.draw.ellipse(screen, (255, 255, 255), self.rect)