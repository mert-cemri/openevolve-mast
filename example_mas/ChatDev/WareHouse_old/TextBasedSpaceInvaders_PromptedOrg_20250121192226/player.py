'''
Player class to represent the player's ship. Handles movement and shooting.
'''
import pygame
from bullet import Bullet
class Player:
    def __init__(self, screen):
        self.screen = screen
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect(midbottom=(400, 580))
        self.speed = 5
    def move(self, direction):
        self.rect.x += direction * self.speed
        self.rect.x = max(0, min(self.rect.x, self.screen.get_width() - self.rect.width))
    def shoot(self):
        return Bullet(self.screen, self.rect.centerx, self.rect.top)
    def draw(self):
        self.screen.blit(self.image, self.rect)