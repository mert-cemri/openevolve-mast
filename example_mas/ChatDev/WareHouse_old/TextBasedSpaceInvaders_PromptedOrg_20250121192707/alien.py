'''
This module contains the Alien class, which represents an alien.
'''
import pygame
class Alien:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1
    def move(self):
        self.rect.x += self.direction * 5
        if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 5  # Reduced the downward movement increment for balanced gameplay
        if self.rect.bottom >= self.screen.get_height():
            # End the game if any alien reaches the bottom
            return True
        return False
    def draw(self):
        self.screen.blit(self.image, self.rect)