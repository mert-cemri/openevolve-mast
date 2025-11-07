'''
Alien class to manage the aliens.
'''
import pygame
class Alien(pygame.sprite.Sprite):
    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings
        # Load a default image if 'alien.bmp' is not found
        try:
            self.image = pygame.image.load('alien.bmp')
        except FileNotFoundError:
            self.image = pygame.Surface((40, 30))  # Create a simple rectangle as a placeholder
            self.image.fill((0, 255, 0))  # Fill it with green color
        self.rect = self.image.get_rect()
        self.x = float(self.rect.x)
    def update(self):
        self.x += (self.settings.alien_speed * self.settings.fleet_direction)
        self.rect.x = self.x