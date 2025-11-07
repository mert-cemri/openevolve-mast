'''
Represents the bird, handles its movement and collision detection.
'''
import pygame
class Bird:
    def __init__(self):
        self.image = pygame.Surface((34, 24))
        self.image.fill((255, 255, 0))  # Yellow bird
        self.rect = self.image.get_rect(center=(50, 300))
        self.velocity = 0
        self.gravity = 0.5
        self.flap_strength = -10
    def flap(self):
        self.velocity = self.flap_strength
    def update(self):
        self.velocity += self.gravity
        self.rect.y += self.velocity
        if self.rect.y >= 576:  # Adjust for bird height
            self.rect.y = 576
            self.velocity = 0
            return True  # Indicate collision with the ground
        return False
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    def get_rect(self):
        return self.rect