'''
Represents a bullet fired by the player.
'''
import pygame
from game_object import GameObject
class Bullet(GameObject):
    def __init__(self, x, y):
        super().__init__(x, y, 5, 10)
        self.speed = -10
    def move(self):
        self.y += self.speed
        self.rect.y = self.y  # Update the rect position
    def check_collision(self, alien):
        return self.rect.colliderect(alien.rect)