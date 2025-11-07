'''
Board class to manage the Tetris game board and line clearing.
'''
import pygame
from constants import BOARD_WIDTH, BOARD_HEIGHT, BLOCK_SIZE
class Board:
    def __init__(self):
        self.grid = [[0] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]
    def clear_lines(self):
        lines_to_clear = []
        for y in range(BOARD_HEIGHT):
            if all(self.grid[y]):
                lines_to_clear.append(y)
        for y in lines_to_clear:
            del self.grid[y]
            self.grid.insert(0, [0] * BOARD_WIDTH)
        return len(lines_to_clear)
    def is_game_over(self):
        # Game is over if any block is in the top row
        return any(self.grid[0])
    def draw(self, screen):
        for y in range(BOARD_HEIGHT):
            for x in range(BOARD_WIDTH):
                if self.grid[y][x]:
                    pygame.draw.rect(screen, (255, 255, 255), (x * BLOCK_SIZE, y * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE))