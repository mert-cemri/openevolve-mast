'''
Represents a single checkers piece.
'''
import pygame
class Piece:
    def __init__(self, color):
        self.color = color
        self.king = False
    def is_king(self):
        return self.king
    def make_king(self):
        self.king = True
    def draw(self, screen, x, y):
        radius = 40
        pygame.draw.circle(screen, (255, 0, 0) if self.color == 'Red' else (0, 0, 0), (x + 50, y + 50), radius)
        if self.king:
            pygame.draw.circle(screen, (255, 215, 0), (x + 50, y + 50), radius - 10)