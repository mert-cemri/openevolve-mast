'''
Game logic for the 2048 game, including grid management and game state.
'''
import random
from tile import Tile
class Game:
    def __init__(self):
        self.size = 10
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.score = 0
        self.reset()
    def reset(self):
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
        self.score = 0
        self.add_random_tile()
        self.add_random_tile()
    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] is None]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = Tile(2 if random.random() < 0.9 else 4)
    def move(self, direction):
        def slide(row):
            new_row = [tile for tile in row if tile is not None]
            for i in range(len(new_row) - 1):
                if new_row[i].merge(new_row[i + 1]):
                    self.score += new_row[i].value
                    new_row[i + 1] = None
            new_row = [tile for tile in new_row if tile is not None]
            return new_row + [None] * (self.size - len(new_row))
        moved = False
        if direction in ('left', 'right'):
            for i in range(self.size):
                row = self.grid[i][:]
                if direction == 'right':
                    row.reverse()
                new_row = slide(row)
                if direction == 'right':
                    new_row.reverse()
                if new_row != self.grid[i]:
                    moved = True
                    self.grid[i] = new_row
        elif direction in ('up', 'down'):
            for j in range(self.size):
                column = [self.grid[i][j] for i in range(self.size)]
                if direction == 'down':
                    column.reverse()
                new_column = slide(column)
                if direction == 'down':
                    new_column.reverse()
                if new_column != column:
                    moved = True
                    for i in range(self.size):
                        self.grid[i][j] = new_column[i]
        if moved:
            self.add_random_tile()
    def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] is None:
                    return False
                if j < self.size - 1 and self.grid[i][j].value == self.grid[i][j + 1].value:
                    return False
                if i < self.size - 1 and self.grid[i][j].value == self.grid[i + 1][j].value:
                    return False
        return True