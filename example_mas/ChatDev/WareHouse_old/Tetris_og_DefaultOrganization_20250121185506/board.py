'''
Represents the game board and handles line clearing and tetromino placement.
'''
import pygame
from constants import *
class Board:
    def __init__(self):
        self.grid = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    def clear_lines(self):
        lines_to_clear = [i for i, row in enumerate(self.grid) if all(row)]
        for i in lines_to_clear:
            del self.grid[i]
            self.grid.insert(0, [0] * BOARD_WIDTH)
    def is_valid_position(self, tetromino):
        for x, y in tetromino.get_blocks():
            if x < 0 or x >= BOARD_WIDTH or y >= BOARD_HEIGHT or self.grid[y][x]:
                return False
        return True
    def add_tetromino(self, tetromino):
        for x, y in tetromino.get_blocks():
            self.grid[y][x] = tetromino.color
    def draw(self, screen):
        for y, row in enumerate(self.grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(screen, cell, (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))