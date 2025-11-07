'''
The Player class represents the player's ship, handling movement and firing shots.
'''
import pygame
from shot import Shot
class Player:
    def __init__(self):
        self.x = 400
        self.y = 550
        self.speed = 5
        self.width = 50  # Assuming the player's width is 50
    def move_left(self):
        if self.x - self.speed >= 0:  # Ensure the player doesn't move off the left edge
            self.x -= self.speed
    def move_right(self):
        if self.x + self.speed + self.width <= 800:  # Ensure the player doesn't move off the right edge
            self.x += self.speed
    def fire(self):
        return Shot(self.x, self.y)