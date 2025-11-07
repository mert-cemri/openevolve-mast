'''
Paddle class to represent player paddles.
'''
import pygame
class Paddle:
    def __init__(self, position):
        self.x, self.y = position
        self.width = 10
        self.height = 120
        self.color = (255, 255, 255)
    def move(self, direction):
        self.y += direction
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.width, self.height))