'''
Object class to represent game objects like gold and rocks.
'''
import pygame
class Object:
    def __init__(self, type, value, position):
        self.type = type
        self.value = value
        self.position = position
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 215, 0) if type == "gold" else (169, 169, 169))
    def draw(self, screen):
        screen.blit(self.image, self.position)