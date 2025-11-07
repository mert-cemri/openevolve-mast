'''
Grid class to represent the 10x10 grid and manage tile movements.
'''
import random
from tile import Tile
class Grid:
    def __init__(self):
        self.size = 10
        self.grid = [[None for _ in range(self.size)] for _ in range(self.size)]
    def add_random_tile(self):
        empty_positions = self.get_empty_positions()
        if empty_positions:
            x, y = random.choice(empty_positions)
            self.grid[x][y] = Tile(random.choice([2, 4]))
    def get_empty_positions(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.grid[x][y] is None]
    def place_tile(self, x, y, tile):
        self.grid[x][y] = tile
    def can_move(self, direction):
        if direction == 'w':
            return self.can_move_up()
        elif direction == 's':
            return self.can_move_down()
        elif direction == 'a':
            return self.can_move_left()
        elif direction == 'd':
            return self.can_move_right()
        return False
    def move(self, direction):
        if direction == 'w':
            self.move_up()
        elif direction == 's':
            self.move_down()
        elif direction == 'a':
            self.move_left()
        elif direction == 'd':
            self.move_right()
    def can_move_any(self):
        for direction in ['w', 'a', 's', 'd']:
            if self.can_move(direction):
                return True
        return False
    def has_2048(self):
        for row in self.grid:
            for tile in row:
                if tile and tile.value == 2048:
                    return True
        return False
    def __str__(self):
        display = ""
        for row in self.grid:
            display += " ".join(str(tile.value if tile else 0).rjust(4) for tile in row) + "\n"
        return display
    def can_move_up(self):
        for x in range(1, self.size):
            for y in range(self.size):
                if self.grid[x][y] and (self.grid[x-1][y] is None or self.grid[x-1][y].value == self.grid[x][y].value):
                    return True
        return False
    def move_up(self):
        for y in range(self.size):
            self._collapse_column(y, reverse=False)
    def can_move_down(self):
        for x in range(self.size - 1):
            for y in range(self.size):
                if self.grid[x][y] and (self.grid[x+1][y] is None or self.grid[x+1][y].value == self.grid[x][y].value):
                    return True
        return False
    def move_down(self):
        for y in range(self.size):
            self._collapse_column(y, reverse=True)
    def can_move_left(self):
        for x in range(self.size):
            for y in range(1, self.size):
                if self.grid[x][y] and (self.grid[x][y-1] is None or self.grid[x][y-1].value == self.grid[x][y].value):
                    return True
        return False
    def move_left(self):
        for x in range(self.size):
            self._collapse_row(x, reverse=False)
    def can_move_right(self):
        for x in range(self.size):
            for y in range(self.size - 1):
                if self.grid[x][y] and (self.grid[x][y+1] is None or self.grid[x][y+1].value == self.grid[x][y].value):
                    return True
        return False
    def move_right(self):
        for x in range(self.size):
            self._collapse_row(x, reverse=True)
    def _collapse_column(self, y, reverse=False):
        tiles = [self.grid[x][y] for x in range(self.size) if self.grid[x][y] is not None]
        if reverse:
            tiles.reverse()
        merged_tiles = self._merge_tiles(tiles)
        if reverse:
            merged_tiles.reverse()
        for x in range(self.size):
            self.grid[x][y] = merged_tiles[x] if x < len(merged_tiles) else None
    def _collapse_row(self, x, reverse=False):
        tiles = [self.grid[x][y] for y in range(self.size) if self.grid[x][y] is not None]
        if reverse:
            tiles.reverse()
        merged_tiles = self._merge_tiles(tiles)
        if reverse:
            merged_tiles.reverse()
        for y in range(self.size):
            self.grid[x][y] = merged_tiles[y] if y < len(merged_tiles) else None
    def _merge_tiles(self, tiles):
        if not tiles:
            return []
        merged = []
        i = 0
        while i < len(tiles):
            if i < len(tiles) - 1 and tiles[i].value == tiles[i + 1].value:
                merged.append(Tile(tiles[i].value * 2))
                i += 2  # Skip the next tile as it has been merged
            else:
                merged.append(tiles[i])
                i += 1
        return merged