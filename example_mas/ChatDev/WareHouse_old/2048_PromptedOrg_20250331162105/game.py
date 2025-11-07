'''
This module contains the Game class, which manages the game state, including the grid, score, and game logic for moving and merging tiles.
'''
import random
from tile import Tile
from utils import generate_random_tile, can_move
class Game:
    def __init__(self):
        self.grid = [[None for _ in range(4)] for _ in range(4)]
        self.score = 0
        self.highest_tile = 0
        self.add_random_tile()
        self.add_random_tile()
    def add_random_tile(self):
        tile_value = generate_random_tile()
        empty_cells = [(r, c) for r in range(4) for c in range(4) if self.grid[r][c] is None]
        if empty_cells:
            r, c = random.choice(empty_cells)
            self.grid[r][c] = Tile(tile_value)
    def move(self, direction):
        moved = False
        if direction == 'up':
            moved = self.move_up()
        elif direction == 'down':
            moved = self.move_down()
        elif direction == 'left':
            moved = self.move_left()
        elif direction == 'right':
            moved = self.move_right()
        if moved:
            self.add_random_tile()
            self.update_highest_tile()
    def move_up(self):
        moved = False
        for c in range(4):
            tiles = [self.grid[r][c] for r in range(4) if self.grid[r][c] is not None]
            merged = self.merge_tiles(tiles)
            for r in range(4):
                if r < len(merged):
                    if self.grid[r][c] != merged[r]:
                        moved = True
                    self.grid[r][c] = merged[r]
                else:
                    if self.grid[r][c] is not None:
                        moved = True
                    self.grid[r][c] = None
        return moved
    def move_down(self):
        moved = False
        for c in range(4):
            tiles = [self.grid[r][c] for r in range(4) if self.grid[r][c] is not None]
            merged = self.merge_tiles(tiles[::-1])[::-1]
            for r in range(4):
                if r < len(merged):
                    if self.grid[3-r][c] != merged[r]:
                        moved = True
                    self.grid[3-r][c] = merged[r]
                else:
                    if self.grid[3-r][c] is not None:
                        moved = True
                    self.grid[3-r][c] = None
        return moved
    def move_left(self):
        moved = False
        for r in range(4):
            tiles = [self.grid[r][c] for c in range(4) if self.grid[r][c] is not None]
            merged = self.merge_tiles(tiles)
            for c in range(4):
                if c < len(merged):
                    if self.grid[r][c] != merged[c]:
                        moved = True
                    self.grid[r][c] = merged[c]
                else:
                    if self.grid[r][c] is not None:
                        moved = True
                    self.grid[r][c] = None
        return moved
    def move_right(self):
        moved = False
        for r in range(4):
            tiles = [self.grid[r][c] for c in range(4) if self.grid[r][c] is not None]
            merged = self.merge_tiles(tiles[::-1])[::-1]
            for c in range(4):
                if c < len(merged):
                    if self.grid[r][3-c] != merged[c]:
                        moved = True
                    self.grid[r][3-c] = merged[c]
                else:
                    if self.grid[r][3-c] is not None:
                        moved = True
                    self.grid[r][3-c] = None
        return moved
    def merge_tiles(self, tiles):
        if not tiles:
            return []
        merged = []
        i = 0
        while i < len(tiles):
            if i + 1 < len(tiles) and tiles[i].value == tiles[i + 1].value:
                merged_value = tiles[i].value * 2
                self.score += merged_value
                merged.append(Tile(merged_value))
                i += 2  # Skip the next tile since it has been merged
            else:
                merged.append(tiles[i])
                i += 1
        return merged
    def update_highest_tile(self):
        for row in self.grid:
            for tile in row:
                if tile and tile.value > self.highest_tile:
                    self.highest_tile = tile.value
    def is_game_over(self):
        return not can_move(self.grid)
    def get_score(self):
        return self.score
    def get_highest_tile(self):
        return self.highest_tile
    def display_grid(self):
        for row in self.grid:
            print(' '.join(str(tile.value if tile else '.') for tile in row))
        print(f"Score: {self.score}, Highest Tile: {self.highest_tile}")