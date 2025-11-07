'''
Board class for managing the Tetris game board.
'''
import pygame
class Board:
    def __init__(self):
        self.width = 10
        self.height = 20
        self.grid = [[0] * self.width for _ in range(self.height)]
    def is_line_complete(self, y):
        return all(self.grid[y])
    def clear_lines(self):
        lines_cleared = 0
        for y in range(self.height):
            if self.is_line_complete(y):
                del self.grid[y]
                self.grid.insert(0, [0] * self.width)
                lines_cleared += 1
        return lines_cleared
    def add_tetromino(self, tetromino):
        for x, y in tetromino.get_blocks():
            self.grid[y][x] = 1
    def is_valid_position(self, tetromino):
        for x, y in tetromino.get_blocks():
            if x < 0 or x >= self.width or y >= self.height or self.grid[y][x]:
                return False
        return True
    def draw(self, screen):
        for y in range(self.height):
            for x in range(self.width):
                if self.grid[y][x]:
                    pygame.draw.rect(screen, (255, 255, 255), (x * 30, y * 30, 30, 30))