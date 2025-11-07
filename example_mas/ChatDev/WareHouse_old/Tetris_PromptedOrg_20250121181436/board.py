'''
Represents the Tetris board and handles operations like clearing lines and checking for collisions.
'''
class Board:
    def __init__(self, width=10, height=20):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]
    def clear_lines(self):
        new_grid = [row for row in self.grid if any(cell == 0 for cell in row)]
        lines_cleared = self.height - len(new_grid)
        self.grid = [[0] * self.width for _ in range(lines_cleared)] + new_grid
        return lines_cleared
    def is_collision(self, tetromino):
        for x, y in tetromino.get_blocks():
            if x < 0 or x >= self.width or y >= self.height or self.grid[y][x]:
                return True
        return False
    def place_tetromino(self, tetromino):
        for x, y in tetromino.get_blocks():
            self.grid[y][x] = 1