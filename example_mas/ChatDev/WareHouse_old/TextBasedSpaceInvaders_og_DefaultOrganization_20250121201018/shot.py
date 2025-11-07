'''
Shot class representing a shot fired by the player.
'''
import pygame
class Shot:
    def __init__(self, x, y):
        self.image = pygame.Surface((5, 10))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect(center=(x, y))
    def move(self):
        self.rect.y -= 10
    def draw(self, screen):
        screen.blit(self.image, self.rect)