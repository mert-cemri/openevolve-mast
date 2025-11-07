'''
Represents tetrominoes and handles their movement and rotation.
'''
import pygame
import random
from constants import *
class Tetromino:
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color
        self.x = BOARD_WIDTH // 2 - len(shape[0]) // 2
        self.y = 0
    def rotate(self, board):
        new_shape = [list(row) for row in zip(*self.shape[::-1])]
        new_blocks = self._get_blocks(new_shape, self.x, self.y)
        if board.is_valid_position(Tetromino(new_shape, self.color)):
            self.shape = new_shape
    def move(self, dx, dy, board):
        new_tetromino = Tetromino(self.shape, self.color)
        new_tetromino.x = self.x + dx
        new_tetromino.y = self.y + dy
        if board.is_valid_position(new_tetromino):
            self.x += dx
            self.y += dy
            return True
        return False
    def get_blocks(self):
        return self._get_blocks(self.shape, self.x, self.y)
    def _get_blocks(self, shape, x, y):
        return [(x + j, y + i) for i, row in enumerate(shape) for j, cell in enumerate(row) if cell]
    def draw(self, screen):
        for x, y in self.get_blocks():
            pygame.draw.rect(screen, self.color, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
class TetrominoFactory:
    def __init__(self):
        self.shape_color_pairs = [
            ([[1, 1, 1, 1]], CYAN),  # I
            ([[1, 1, 1], [0, 1, 0]], PURPLE),  # T
            ([[1, 1, 0], [0, 1, 1]], RED),  # Z
            ([[0, 1, 1], [1, 1, 0]], GREEN),  # S
            ([[1, 1], [1, 1]], YELLOW),  # O
            ([[1, 1, 1], [1, 0, 0]], ORANGE),  # L
            ([[1, 1, 1], [0, 0, 1]], BLUE),  # J
        ]
    def create_tetromino(self):
        shape, color = random.choice(self.shape_color_pairs)
        return Tetromino(shape, color)