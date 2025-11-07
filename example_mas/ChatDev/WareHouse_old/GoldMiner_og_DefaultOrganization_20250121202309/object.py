'''
Object class representing items that can be grabbed by the claw.
'''
import pygame
class Object:
    def __init__(self, screen, x, y, value=10, weight=1):
        self.screen = screen
        self.x = x
        self.y = y
        self.value = value
        self.weight = weight
    def draw(self):
        pygame.draw.circle(self.screen, (255, 215, 0), (self.x, self.y), 10)