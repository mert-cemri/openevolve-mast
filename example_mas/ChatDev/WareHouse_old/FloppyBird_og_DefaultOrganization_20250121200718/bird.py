'''
Bird character logic.
'''
import pygame
# Constants
BIRD_WIDTH = 34
BIRD_HEIGHT = 24
GRAVITY = 0.5
FLAP_STRENGTH = -10
class Bird:
    def __init__(self):
        self.image = pygame.Surface((BIRD_WIDTH, BIRD_HEIGHT))
        self.image.fill((255, 255, 0))  # Yellow bird
        self.rect = self.image.get_rect(center=(50, 300))
        self.velocity = 0
    def flap(self):
        self.velocity = FLAP_STRENGTH
    def update(self):
        self.velocity += GRAVITY
        self.rect.y += self.velocity
        # End the game if the bird goes out of bounds
        if self.rect.top <= 0 or self.rect.bottom >= 600:
            raise Exception("Game Over: Bird collided with the ground or went out of bounds.")
    def draw(self, screen):
        screen.blit(self.image, self.rect)