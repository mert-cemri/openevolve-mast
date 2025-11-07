'''
GameObject class for representing objects in the game.
'''
import pygame
class GameObject:
    def __init__(self, type, value, weight, position):
        self.type = type
        self.value = value
        self.weight = weight
        self.position = position
    def draw(self, screen):
        color = (255, 215, 0) if self.type == "gold" else (169, 169, 169)
        pygame.draw.circle(screen, color, self.position, 15)