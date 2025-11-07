'''
Paddle class to represent player paddles.
'''
import pygame
class Paddle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 10
        self.height = 120
        self.speed = 5
    def move_up(self):
        if self.y - self.speed >= 0:
            self.y -= self.speed
    def move_down(self):
        if self.y + self.height + self.speed <= 600:
            self.y += self.speed
    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), (self.x, self.y, self.width, self.height))