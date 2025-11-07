'''
Pipe obstacle logic.
'''
import pygame
import random
# Constants
PIPE_WIDTH = 52
PIPE_HEIGHT = 320
PIPE_GAP = 150
PIPE_SPEED = 3
class Pipe:
    def __init__(self, gap_size):
        self.image = pygame.Surface((PIPE_WIDTH, PIPE_HEIGHT))
        self.image.fill((0, 255, 0))  # Green pipe
        self.top_rect = self.image.get_rect(midbottom=(400, random.randint(100, 300)))
        self.bottom_rect = self.image.get_rect(midtop=(400, self.top_rect.bottom + gap_size))
    def update(self):
        self.top_rect.x -= PIPE_SPEED
        self.bottom_rect.x -= PIPE_SPEED
    def off_screen(self):
        return self.top_rect.right < 0
    def collides_with(self, bird):
        return self.top_rect.colliderect(bird.rect) or self.bottom_rect.colliderect(bird.rect)
    def draw(self, screen):
        screen.blit(self.image, self.top_rect)
        screen.blit(self.image, self.bottom_rect)