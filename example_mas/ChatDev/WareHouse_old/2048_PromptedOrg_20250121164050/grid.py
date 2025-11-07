'''
This module contains the Grid class which manages the grid and tile positions.
'''
class Grid:
    def __init__(self, size):
        self.size = size
        self.grid = [[0] * size for _ in range(size)]
    def get_empty_positions(self):
        return [(x, y) for x in range(self.size) for y in range(self.size) if self.grid[x][y] == 0]
    def set_tile(self, x, y, value):
        self.grid[x][y] = value
    def move(self, direction):
        moved = False
        total_score = 0
        if direction == 'up':
            moved, score = self._move_vertical(reverse=False)
        elif direction == 'down':
            moved, score = self._move_vertical(reverse=True)
        elif direction == 'left':
            moved, score = self._move_horizontal(reverse=False)
        elif direction == 'right':
            moved, score = self._move_horizontal(reverse=True)
        total_score += score
        return moved, total_score
    def _move_vertical(self, reverse):
        moved = False
        total_score = 0
        for col in range(self.size):
            tiles = [self.grid[row][col] for row in range(self.size) if self.grid[row][col] != 0]
            if reverse:
                tiles.reverse()
            merged, score = self._merge_tiles(tiles)
            total_score += score
            if reverse:
                merged.reverse()
            for row in range(self.size):
                value = merged[row] if row < len(merged) else 0
                if self.grid[row][col] != value:
                    moved = True
                self.grid[row][col] = value
        return moved, total_score
    def _move_horizontal(self, reverse):
        moved = False
        total_score = 0
        for row in range(self.size):
            tiles = [self.grid[row][col] for col in range(self.size) if self.grid[row][col] != 0]
            if reverse:
                tiles.reverse()
            merged, score = self._merge_tiles(tiles)
            total_score += score
            if reverse:
                merged.reverse()
            for col in range(self.size):
                value = merged[col] if col < len(merged) else 0
                if self.grid[row][col] != value:
                    moved = True
                self.grid[row][col] = value
        return moved, total_score
    def _merge_tiles(self, tiles):
        if not tiles:
            return [], 0
        merged = []
        score = 0
        skip = False
        for i in range(len(tiles)):
            if skip:
                skip = False
                continue
            if i + 1 < len(tiles) and tiles[i] == tiles[i + 1]:
                merged_value = tiles[i] * 2
                merged.append(merged_value)
                score += merged_value
                skip = True
            else:
                merged.append(tiles[i])
        return merged, score
    def can_move(self):
        if any(0 in row for row in self.grid):
            return True
        for x in range(self.size):
            for y in range(self.size - 1):
                if self.grid[x][y] == self.grid[x][y + 1]:
                    return True
                if self.grid[y][x] == self.grid[y + 1][x]:
                    return True
        return False