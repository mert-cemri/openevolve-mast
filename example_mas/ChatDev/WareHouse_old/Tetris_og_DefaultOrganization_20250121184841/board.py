'''
Board class to represent the Tetris board and handle operations like clearing lines.
'''
import pygame
from constants import *
class Board:
    def __init__(self):
        self.grid = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
        self.score = 0
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0] * BOARD_WIDTH)
            self.score += 100  # Increase score for each cleared line
    def is_game_over(self):
        return any(self.grid[0])  # Game over if any block is in the top row
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, WHITE, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))
    def add_tetromino(self, tetromino):
        for y, row in enumerate(tetromino.shape):
            for x, cell in enumerate(row):
                if cell:
                    self.grid[tetromino.position[0] + y][tetromino.position[1] + x] = 1