'''
This module contains the Shot class, which represents a shot fired by the player.
'''
import pygame
class Shot:
    def __init__(self, screen, x, y):
        '''
        Initializes the Shot object with its position and appearance.
        '''
        self.screen = screen
        self.image = pygame.Surface((5, 15))
        self.image.fill((255, 255, 0))
        self.rect = self.image.get_rect(midbottom=(x, y))
    def move(self):
        '''
        Moves the shot upwards on the screen.
        '''
        self.rect.y -= 10
    def draw(self):
        '''
        Draws the shot on the screen.
        '''
        self.screen.blit(self.image, self.rect)