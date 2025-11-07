'''
Pipe class representing the pipes in the game.
'''
import pygame
import random
class Pipe:
    def __init__(self):
        self.x = 400
        self.gap = 150
        self.width = 70
        self.top_height = random.randint(50, 350)
        self.bottom_height = 600 - self.top_height - self.gap
        self.color = (0, 255, 0)  # Green pipes
        self.passed = False  # New attribute to track if the bird has passed
    def update(self):
        self.x -= 5
    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.top_height))
        pygame.draw.rect(screen, self.color, (self.x, 600 - self.bottom_height, self.width, self.bottom_height))
    def collides_with(self, bird):
        if bird.rect.colliderect((self.x, 0, self.width, self.top_height)) or \
           bird.rect.colliderect((self.x, 600 - self.bottom_height, self.width, self.bottom_height)):
            return True
        return False
    def off_screen(self):
        return self.x < -self.width