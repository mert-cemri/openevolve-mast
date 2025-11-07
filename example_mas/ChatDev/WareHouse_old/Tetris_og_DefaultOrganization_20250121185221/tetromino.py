'''
Tetromino class for managing the tetromino pieces.
'''
import random
import pygame
class Tetromino:
    SHAPES = [
        [[1, 1, 1, 1]],
        [[1, 1], [1, 1]],
        [[0, 1, 0], [1, 1, 1]],
        [[1, 0, 0], [1, 1, 1]],
        [[0, 0, 1], [1, 1, 1]],
        [[1, 1, 0], [0, 1, 1]],
        [[0, 1, 1], [1, 1, 0]]
    ]
    def __init__(self):
        self.shape = random.choice(self.SHAPES)
        self.x = 3
        self.y = 0
    def get_blocks(self):
        blocks = []
        for y, row in enumerate(self.shape):
            for x, cell in enumerate(row):
                if cell:
                    blocks.append((self.x + x, self.y + y))
        return blocks
    def rotate(self, board):
        original_shape = self.shape
        self.shape = [list(row) for row in zip(*self.shape[::-1])]
        if not board.is_valid_position(self):
            # Implementing a more comprehensive wall kick system
            for dx, dy in [(-1, 0), (1, 0), (-2, 0), (2, 0), (0, 1), (0, -1)]:
                self.x += dx
                self.y += dy
                if board.is_valid_position(self):
                    return
                self.x -= dx
                self.y -= dy
            # Revert rotation if no valid position is found
            self.shape = original_shape
    def move(self, dx, dy, board):
        self.x += dx
        self.y += dy
        if not board.is_valid_position(self):
            self.x -= dx
            self.y -= dy
            return False
        return True
    def draw(self, screen):
        for x, y in self.get_blocks():
            pygame.draw.rect(screen, (255, 255, 255), (x * 30, y * 30, 30, 30))