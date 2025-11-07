'''
Alien class representing an alien enemy.
'''
import pygame
class Alien:
    def __init__(self, x, y):
        self.image = pygame.Surface((40, 30))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect(topleft=(x, y))
        self.direction = 1
        self.horizontal_moves = 0  # Counter for horizontal movements
    def move(self):
        self.rect.x += self.direction * 2
        self.horizontal_moves += 1
        if self.rect.right >= 800 or self.rect.left <= 0:
            self.direction *= -1
            self.horizontal_moves = 0  # Reset counter when changing direction
        # Move down after a certain number of horizontal moves
        if self.horizontal_moves >= 10:
            self.rect.y += 20
            self.horizontal_moves = 0  # Reset counter after moving down
    def check_collision(self, shot):
        return self.rect.colliderect(shot.rect)
    def draw(self, screen):
        screen.blit(self.image, self.rect)