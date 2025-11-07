'''
Pipe class representing the pipes in the game.
'''
import pygame
import random
class Pipe:
    def __init__(self):
        self.image = pygame.Surface((52, 320))
        self.image.fill((0, 255, 0))  # Green pipes
        self.gap = 150
        self.x = 400
        # Ensure the top height is within a reasonable range
        min_top_height = 50
        max_top_height = 450 - self.gap
        self.top_height = random.randint(min_top_height, max_top_height)
        self.bottom_height = 600 - self.top_height - self.gap
        self.top_rect = self.image.get_rect(midbottom=(self.x, self.top_height))
        self.bottom_rect = self.image.get_rect(midtop=(self.x, self.top_height + self.gap))
    def update(self):
        self.top_rect.x -= 5
        self.bottom_rect.x -= 5
    def draw(self, screen):
        screen.blit(self.image, self.top_rect)
        screen.blit(self.image, self.bottom_rect)
    def is_off_screen(self):
        return self.top_rect.right < 0