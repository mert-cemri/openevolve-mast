'''
Represents the pipes, handles their movement and collision detection.
'''
import pygame
import random
class Pipe:
    def __init__(self):
        self.image = pygame.Surface((52, 320))
        self.image.fill((0, 255, 0))  # Green pipe
        self.rect_top = self.image.get_rect(midbottom=(400, random.randint(150, 450)))
        self.rect_bottom = self.image.get_rect(midtop=(400, self.rect_top.bottom + 100))
        self.speed = 5
        self.scored = False  # Initialize scored attribute
    def update(self):
        self.rect_top.x -= self.speed
        self.rect_bottom.x -= self.speed
    def draw(self, screen):
        screen.blit(self.image, self.rect_top)
        screen.blit(self.image, self.rect_bottom)
    def off_screen(self):
        return self.rect_top.right < 0
    def collides_with(self, bird):
        return self.rect_top.colliderect(bird.get_rect()) or self.rect_bottom.colliderect(bird.get_rect())