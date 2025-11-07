'''
Tetromino class to represent the tetrominoes, including their shapes and rotations.
'''
import pygame
import random
from constants import *
class Tetromino:
    def __init__(self):
        self.shape = random.choice(TETROMINO_SHAPES)
        self.position = [0, BOARD_WIDTH // 2 - len(self.shape[0]) // 2]
    def rotate(self, board):
        new_shape = list(zip(*self.shape[::-1]))
        if not self.collides(new_shape, self.position, board):
            self.shape = new_shape
    def move(self, dx, dy, board):
        new_position = [self.position[0] + dy, self.position[1] + dx]
        if not self.collides(self.shape, new_position, board):
            self.position = new_position
            return True  # Tetromino has not landed
        elif dy:  # Only check for landing when moving down
            board.add_tetromino(self)
            board.clear_lines()
            return False  # Indicates the tetromino has landed
        return True
    def collides(self, shape, position, board):
        for y, row in enumerate(shape):
            for x, cell in enumerate(row):
                if cell:
                    if (y + position[0] >= BOARD_HEIGHT or
                        x + position[1] < 0 or
                        x + position[1] >= BOARD_WIDTH or
                        board.grid[y + position[0]][x + position[1]]):
                        return True
        return False
    def draw(self, screen):
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, WHITE, ((self.position[1] + x) * BLOCK_SIZE, (self.position[0] + y) * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))