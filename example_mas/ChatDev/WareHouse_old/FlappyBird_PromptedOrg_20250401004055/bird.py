'''
Bird class to handle bird physics, movement, and rendering.
'''
import pygame
class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -10
        self.image = pygame.Surface((34, 24))
        self.image.fill((255, 255, 0))  # Yellow bird
    def flap(self):
        self.velocity = self.flap_strength
    def update(self):
        self.velocity += self.gravity
        self.y += self.velocity
    def draw(self, screen):
        screen.blit(self.image, (self.x, self.y))
    def get_rect(self):
        return pygame.Rect(self.x, self.y, 34, 24)