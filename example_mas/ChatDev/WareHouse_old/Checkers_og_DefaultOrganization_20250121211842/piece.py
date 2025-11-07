'''
Piece class to represent individual checkers pieces.
'''
import pygame
class Piece:
    def __init__(self, color, is_king=False):
        self.color = color
        self.is_king = is_king
    def draw(self, screen, position):
        radius = 40
        if self.color == 'red':
            color = (255, 0, 0)
        else:
            color = (0, 0, 0)
        pygame.draw.circle(screen, color, position, radius)
        if self.is_king:
            pygame.draw.circle(screen, (255, 215, 0), position, radius // 2)