'''
Represents an alien enemy in the game.
'''
import pygame
from game_object import GameObject
class Alien(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 40, 30)
        self.speed = 1
        self.direction = 1  # 1 for right, -1 for left
    def move(self):
        self.x += self.speed * self.direction
        if self.x <= 0 or self.x >= 760:  # Assuming screen width is 800
            self.direction *= -1
            self.y += 30  # Move down when hitting the edge
        self.rect.x = self.x
        self.rect.y = self.y