'''
Represents the player's ship in the game.
'''
import pygame
from bullet import Bullet
from game_object import GameObject
class Player(GameObject):
    def __init__(self):
        super().__init__(400, 550, 50, 30)
        self.speed = 5
    def move(self, direction):
        self.x += direction * self.speed
        self.x = max(0, min(self.x, 750))
        self.rect.x = self.x  # Update the rect position
    def shoot(self):
        return Bullet(self.x + self.width // 2, self.y)