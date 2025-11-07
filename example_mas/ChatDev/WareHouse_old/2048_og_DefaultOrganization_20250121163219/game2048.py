'''
Handles the game logic for the 2048 game, including grid management and tile merging.
'''
import random
class Game2048:
    def __init__(self):
        self.grid_size = 10
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0
        self.game_over = False
        self.initialize_grid()
    def initialize_grid(self):
        self.add_random_tile()
        self.add_random_tile()
    def add_random_tile(self):
        empty_tiles = [(r, c) for r in range(self.grid_size) for c in range(self.grid_size) if self.grid[r][c] == 0]
        if empty_tiles:
            r, c = random.choice(empty_tiles)
            self.grid[r][c] = 2 if random.random() < 0.9 else 4
    def move(self, direction):
        if self.game_over:
            return
        if direction in ['UP', 'DOWN', 'LEFT', 'RIGHT']:
            moved = self.merge_tiles(direction)
            if moved:
                self.add_random_tile()
            self.check_game_over()
    def merge_tiles(self, direction):
        moved = False
        if direction == 'UP':
            for c in range(self.grid_size):
                tiles = [self.grid[r][c] for r in range(self.grid_size) if self.grid[r][c] != 0]
                merged_tiles, score = self.merge_line(tiles)
                for r in range(self.grid_size):
                    value = merged_tiles[r] if r < len(merged_tiles) else 0
                    if self.grid[r][c] != value:
                        moved = True
                    self.grid[r][c] = value
                self.score += score
        elif direction == 'DOWN':
            for c in range(self.grid_size):
                tiles = [self.grid[r][c] for r in range(self.grid_size) if self.grid[r][c] != 0]
                merged_tiles, score = self.merge_line(tiles[::-1])
                for r in range(self.grid_size):
                    value = merged_tiles[::-1][r] if r < len(merged_tiles) else 0
                    if self.grid[r][c] != value:
                        moved = True
                    self.grid[r][c] = value
                self.score += score
        elif direction == 'LEFT':
            for r in range(self.grid_size):
                tiles = [self.grid[r][c] for c in range(self.grid_size) if self.grid[r][c] != 0]
                merged_tiles, score = self.merge_line(tiles)
                for c in range(self.grid_size):
                    value = merged_tiles[c] if c < len(merged_tiles) else 0
                    if self.grid[r][c] != value:
                        moved = True
                    self.grid[r][c] = value
                self.score += score
        elif direction == 'RIGHT':
            for r in range(self.grid_size):
                tiles = [self.grid[r][c] for c in range(self.grid_size) if self.grid[r][c] != 0]
                merged_tiles, score = self.merge_line(tiles[::-1])
                for c in range(self.grid_size):
                    value = merged_tiles[::-1][c] if c < len(merged_tiles) else 0
                    if self.grid[r][c] != value:
                        moved = True
                    self.grid[r][c] = value
                self.score += score
        return moved
    def merge_line(self, tiles):
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
                merged.append(tiles[i] * 2)
                score += tiles[i] * 2
                skip = True
            else:
                merged.append(tiles[i])
        return merged, score
    def check_game_over(self):
        if not self.can_move():
            self.game_over = True
    def can_move(self):
        for r in range(self.grid_size):
            for c in range(self.grid_size):
                if self.grid[r][c] == 0:
                    return True
                if c < self.grid_size - 1 and self.grid[r][c] == self.grid[r][c + 1]:
                    return True
                if r < self.grid_size - 1 and self.grid[r][c] == self.grid[r + 1][c]:
                    return True
        return False