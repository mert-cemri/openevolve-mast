'''
Represents player's ship.
'''
import pygame
class Ship:
    def __init__(self, game):
        self.screen = game.screen
        self.settings = game.settings
        self.image = pygame.Surface((50, 30))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.midbottom = self.screen.get_rect().midbottom
        self.x = float(self.rect.x)
        self.moving_left = False
        self.moving_right = False
    def update(self):
        if self.moving_right and self.rect.right < self.screen.get_rect().right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        self.rect.x = self.x
    def draw(self):
        self.screen.blit(self.image, self.rect)