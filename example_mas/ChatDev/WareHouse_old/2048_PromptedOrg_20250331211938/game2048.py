'''
Implements the core logic for the 2048 game, including grid initialization, tile movements, merging logic, and game state checks.
'''
import random
import copy
class Game2048:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.highest_tile = 0
        self.place_random_tile()
        self.place_random_tile()
    def place_random_tile(self):
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] == 0]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = 4 if random.random() < 0.1 else 2
            self.highest_tile = max(self.highest_tile, self.grid[r][c])
    def compress(self, grid):
        new_grid = [[0] * 4 for _ in range(4)]
        changed = False
        for i in range(4):
            pos = 0
            for j in range(4):
                if grid[i][j] != 0:
                    new_grid[i][pos] = grid[i][j]
                    if j != pos:
                        changed = True
                    pos += 1
        return new_grid, changed
    def merge(self, grid):
        changed = False
        for i in range(4):
            for j in range(3):
                if grid[i][j] != 0 and grid[i][j] == grid[i][j + 1]:
                    grid[i][j] *= 2
                    self.score += grid[i][j]
                    self.highest_tile = max(self.highest_tile, grid[i][j])
                    grid[i][j + 1] = 0
                    changed = True
        return grid, changed
    def reverse(self, grid):
        return [row[::-1] for row in grid]
    def transpose(self, grid):
        return [list(row) for row in zip(*grid)]
    def move(self, direction: str) -> bool:
        original_grid = copy.deepcopy(self.grid)
        changed = False
        if direction == 'left':
            self.grid, compressed = self.compress(self.grid)
            self.grid, merged = self.merge(self.grid)
            self.grid, _ = self.compress(self.grid)
            changed = compressed or merged
        elif direction == 'right':
            self.grid = self.reverse(self.grid)
            self.grid, compressed = self.compress(self.grid)
            self.grid, merged = self.merge(self.grid)
            self.grid, _ = self.compress(self.grid)
            self.grid = self.reverse(self.grid)
            changed = compressed or merged
        elif direction == 'up':
            self.grid = self.transpose(self.grid)
            self.grid, compressed = self.compress(self.grid)
            self.grid, merged = self.merge(self.grid)
            self.grid, _ = self.compress(self.grid)
            self.grid = self.transpose(self.grid)
            changed = compressed or merged
        elif direction == 'down':
            self.grid = self.transpose(self.grid)
            self.grid = self.reverse(self.grid)
            self.grid, compressed = self.compress(self.grid)
            self.grid, merged = self.merge(self.grid)
            self.grid, _ = self.compress(self.grid)
            self.grid = self.reverse(self.grid)
            self.grid = self.transpose(self.grid)
            changed = compressed or merged
        if changed:
            self.place_random_tile()
        return changed
    def is_game_over(self) -> bool:
        for direction in ['left', 'right', 'up', 'down']:
            grid_copy = copy.deepcopy(self.grid)
            if self.move(direction):
                self.grid = grid_copy
                return False
        return True
    def get_score(self) -> int:
        return self.score
    def get_highest_tile(self) -> int:
        return self.highest_tile