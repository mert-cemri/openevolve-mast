'''
This module contains utility functions for the 2048 game, including random tile generation and checking available moves.
'''
import random
def generate_random_tile():
    return 2 if random.random() < 0.9 else 4
def can_move(grid):
    for r in range(4):
        for c in range(4):
            if grid[r][c] is None:
                return True
            if c < 3 and (grid[r][c].value == grid[r][c + 1].value or grid[r][c + 1] is None):
                return True
            if r < 3 and (grid[r][c].value == grid[r + 1][c].value or grid[r + 1][c] is None):
                return True
            if c > 0 and (grid[r][c].value == grid[r][c - 1].value or grid[r][c - 1] is None):
                return True
            if r > 0 and (grid[r][c].value == grid[r - 1][c].value or grid[r - 1][c] is None):
                return True
    return False