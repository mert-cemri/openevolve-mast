'''
Tetromino class to manage the tetromino shapes and movements.
'''
import pygame
import random
from constants import BLOCK_SIZE, BOARD_WIDTH, BOARD_HEIGHT
class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]],  # I-tetromino
        [[1, 1], [1, 1]],  # O-tetromino
        [[0, 1, 0], [1, 1, 1]],  # T-tetromino
        [[1, 1, 0], [0, 1, 1]],  # S-tetromino
        [[0, 1, 1], [1, 1, 0]],  # Z-tetromino
        [[1, 0, 0], [1, 1, 1]],  # J-tetromino
        [[0, 0, 1], [1, 1, 1]]   # L-tetromino
    ]
    def __init__(self):
        self.shape = random.choice(self.SHAPES)
        self.x = BOARD_WIDTH // 2 - len(self.shape[0]) // 2
        self.y = 0
    def rotate(self, board):
        # Logic to rotate the tetromino
        new_shape = list(zip(*self.shape[::-1]))
        if self.can_move(0, 0, new_shape, board):
            self.shape = new_shape
    def move(self, direction, board, down=False):
        dx = direction
        dy = 1 if down else 0
        if self.can_move(dx, dy, self.shape, board):
            self.x += dx
            self.y += dy
            return True
        return False
    def can_move(self, dx, dy, shape, board):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    new_x = self.x + x + dx
                    new_y = self.y + y + dy
                    if new_x < 0 or new_x >= BOARD_WIDTH or new_y >= BOARD_HEIGHT:
                        return False
                    if new_y >= 0 and board.grid[new_y][new_x]:
                        return False
        return True
    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, (255, 255, 255), ((self.x + x) * BLOCK_SIZE, (self.y + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))