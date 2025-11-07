'''
Alien class to represent an alien. Handles movement and drawing.
'''
import pygame
class Alien:
    def __init__(self, screen, x, y):
        self.screen = screen
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.speed = 1
        self.direction = 1  # 1 for right, -1 for left
        self.descent_timer = 0  # Timer for descent
    def move(self):
        self.rect.x += self.speed * self.direction
        if self.rect.right >= self.screen.get_width() or self.rect.left <= 0:
            self.direction *= -1
            self.rect.y += 10  # Move down when hitting the edge
        # Increment descent timer and move down periodically
        self.descent_timer += 1
        if self.descent_timer >= 60:  # Adjust the value for desired descent speed
            self.rect.y += 5  # Move down every second (assuming 60 FPS)
            self.descent_timer = 0
    def draw(self):
        self.screen.blit(self.image, self.rect)