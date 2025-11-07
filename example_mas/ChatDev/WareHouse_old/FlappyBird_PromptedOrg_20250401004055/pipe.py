'''
Pipe class to handle pipe obstacles, movement, collision detection, and rendering.
'''
import pygame
class Pipe:
    def __init__(self, x, gap_y, gap_size, speed):
        self.x = x
        self.gap_y = gap_y
        self.gap_size = gap_size
        self.speed = speed
        self.width = 60
        self.color = (34, 139, 34)  # Green pipes
        self.passed = False
    def update(self):
        self.x -= self.speed
    def draw(self, screen):
        # Top pipe
        pygame.draw.rect(screen, self.color, (self.x, 0, self.width, self.gap_y - self.gap_size // 2))
        # Bottom pipe
        pygame.draw.rect(screen, self.color, (self.x, self.gap_y + self.gap_size // 2, self.width, 600 - self.gap_y - self.gap_size // 2))
    def collide(self, bird_rect):
        top_pipe_rect = pygame.Rect(self.x, 0, self.width, self.gap_y - self.gap_size // 2)
        bottom_pipe_rect = pygame.Rect(self.x, self.gap_y + self.gap_size // 2, self.width, 600 - self.gap_y - self.gap_size // 2)
        return bird_rect.colliderect(top_pipe_rect) or bird_rect.colliderect(bottom_pipe_rect)
    def off_screen(self):
        return self.x + self.width < 0