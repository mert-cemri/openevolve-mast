'''
Ball class to represent the game ball.
'''
import pygame
import random
class Ball:
    def __init__(self, window_width, window_height):
        self.size = 15
        self.window_width = window_width
        self.window_height = window_height
        self.color = (255, 255, 255)
        self.reset_position()
    def move(self):
        self.x += self.x_vel
        self.y += self.y_vel
    def reset_position(self):
        self.x = self.window_width // 2
        self.y = self.window_height // 2
        self.x_vel = random.choice([-4, 4])
        self.y_vel = random.choice([-4, 4])
    def draw(self, window):
        pygame.draw.rect(window, self.color, (self.x, self.y, self.size, self.size))