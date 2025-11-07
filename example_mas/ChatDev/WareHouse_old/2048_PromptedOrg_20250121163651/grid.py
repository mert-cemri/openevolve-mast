'''
Grid class to manage the 10x10 grid and its operations for the 2048 game.
'''
import random
from tile import Tile
class Grid:
    def __init__(self, size=10):
        self.size = size
        self.grid = [[None for _ in range(size)] for _ in range(size)]
    def add_random_tile(self):
        empty_tiles = [(i, j) for i in range(self.size) for j in range(self.size) if self.grid[i][j] is None]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
            self.grid[i][j] = Tile()
    def move(self, direction):
        moved = False
        total_score = 0
        if direction == 'w':
            moved, total_score = self.move_up()
        elif direction == 'a':
            moved, total_score = self.move_left()
        elif direction == 's':
            moved, total_score = self.move_down()
        elif direction == 'd':
            moved, total_score = self.move_right()
        return moved, total_score
    def move_up(self):
        moved = False
        total_score = 0
        for j in range(self.size):
            tiles = [self.grid[i][j] for i in range(self.size) if self.grid[i][j] is not None]
            merged_tiles, score = self.merge_tiles(tiles)
            total_score += score
            for i in range(self.size):
                if i < len(merged_tiles):
                    if self.grid[i][j] != merged_tiles[i]:
                        moved = True
                    self.grid[i][j] = merged_tiles[i]
                else:
                    if self.grid[i][j] is not None:
                        moved = True
                    self.grid[i][j] = None
        return moved, total_score
    def move_down(self):
        moved = False
        total_score = 0
        for j in range(self.size):
            tiles = [self.grid[i][j] for i in range(self.size) if self.grid[i][j] is not None]
            tiles.reverse()  # Reverse the tiles for correct merging
            merged_tiles, score = self.merge_tiles(tiles)
            merged_tiles.reverse()  # Reverse back after merging
            total_score += score
            for i in range(self.size):
                if i < len(merged_tiles):
                    if self.grid[self.size - 1 - i][j] != merged_tiles[i]:
                        moved = True
                    self.grid[self.size - 1 - i][j] = merged_tiles[i]
                else:
                    if self.grid[self.size - 1 - i][j] is not None:
                        moved = True
                    self.grid[self.size - 1 - i][j] = None
        return moved, total_score
    def move_left(self):
        moved = False
        total_score = 0
        for i in range(self.size):
            tiles = [self.grid[i][j] for j in range(self.size) if self.grid[i][j] is not None]
            merged_tiles, score = self.merge_tiles(tiles)
            total_score += score
            for j in range(self.size):
                if j < len(merged_tiles):
                    if self.grid[i][j] != merged_tiles[j]:
                        moved = True
                    self.grid[i][j] = merged_tiles[j]
                else:
                    if self.grid[i][j] is not None:
                        moved = True
                    self.grid[i][j] = None
        return moved, total_score
    def move_right(self):
        moved = False
        total_score = 0
        for i in range(self.size):
            tiles = [self.grid[i][j] for j in range(self.size) if self.grid[i][j] is not None]
            tiles.reverse()  # Reverse the tiles for correct merging
            merged_tiles, score = self.merge_tiles(tiles)
            merged_tiles.reverse()  # Reverse back after merging
            total_score += score
            for j in range(self.size):
                if j < len(merged_tiles):
                    if self.grid[i][self.size - 1 - j] != merged_tiles[j]:
                        moved = True
                    self.grid[i][self.size - 1 - j] = merged_tiles[j]
                else:
                    if self.grid[i][self.size - 1 - j] is not None:
                        moved = True
                    self.grid[i][self.size - 1 - j] = None
        return moved, total_score
    def merge_tiles(self, tiles):
        if not tiles:
            return [], 0
        merged = []
        score = 0
        skip = False
        for i in range(len(tiles)):
            if skip:
                skip = False
                continue
            if i + 1 < len(tiles) and tiles[i].value == tiles[i + 1].value:
                merged.append(Tile(tiles[i].value * 2))
                score += tiles[i].value * 2
                skip = True
            else:
                merged.append(tiles[i])
        return merged, score
    def is_game_over(self):
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j] is None:
                    return False
                if j + 1 < self.size and self.grid[i][j].value == self.grid[i][j + 1].value:
                    return False
                if i + 1 < self.size and self.grid[i][j].value == self.grid[i + 1][j].value:
                    return False
        return True
    def display(self):
        for row in self.grid:
            print(' '.join(str(tile) if tile else '.' for tile in row))