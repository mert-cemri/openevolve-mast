'''
Grid management for the 2048 game, including tile spawning and movement logic.
'''
import random
from tile import Tile
class Grid:
    def __init__(self):
        self.size = 10
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.spawn_tile()
        self.spawn_tile()
    def spawn_tile(self):
        empty_cells = [(r, c) for r in range(self.size) for c in range(self.size) if self.grid[r][c] is None]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = Tile(2 if random.random() < 0.9 else 4, (r, c))
    def move(self, direction):
        def slide(row):
            new_row = [tile for tile in row if tile is not None]
            for i in range(len(new_row) - 1):
                if new_row[i].value == new_row[i + 1].value:
                    new_row[i].value *= 2
                    new_row[i + 1] = None
            return [tile for tile in new_row if tile is not None]
        def merge(grid):
            for i in range(self.size):
                if direction in ['left', 'right']:
                    row = grid[i]
                else:
                    row = [grid[j][i] for j in range(self.size)]
                if direction in ['right', 'down']:
                    row.reverse()
                new_row = slide(row)
                if direction in ['right', 'down']:
                    new_row.reverse()
                for j in range(self.size):
                    if direction in ['left', 'right']:
                        grid[i][j] = new_row[j] if j < len(new_row) else None
                    else:
                        grid[j][i] = new_row[j] if j < len(new_row) else None
        # Make a copy of the grid before the move
        grid_before_move = [row[:] for row in self.grid]
        if direction in ['left', 'right']:
            merge(self.grid)
        else:
            merge(list(map(list, zip(*self.grid))))
        # Check if the grid has changed
        grid_after_move = [row[:] for row in self.grid]
        if grid_before_move != grid_after_move:
            self.spawn_tile()
    def can_move(self):
        for r in range(self.size):
            for c in range(self.size):
                if self.grid[r][c] is None:
                    return True
                if c < self.size - 1 and self.grid[r][c].value == self.grid[r][c + 1].value:
                    return True
                if r < self.size - 1 and self.grid[r][c].value == self.grid[r + 1][c].value:
                    return True
        return False