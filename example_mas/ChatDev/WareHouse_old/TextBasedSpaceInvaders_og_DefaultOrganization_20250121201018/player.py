'''
Player class representing the player's ship.
'''
import pygame
from shot import Shot
class Player:
    def __init__(self):
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(center=(400, 550))
    def move_left(self):
        if self.rect.left > 0:
            self.rect.x -= 5
    def move_right(self):
        if self.rect.right < 800:
            self.rect.x += 5
    def shoot(self):
        return Shot(self.rect.centerx, self.rect.top)
    def draw(self, screen):
        screen.blit(self.image, self.rect)