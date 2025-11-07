'''
This file contains the Board class, which represents the game board and handles operations related to it.
'''
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [['.' for _ in range(size)] for _ in range(size)]
    def display(self):
        for row in self.grid:
            print(' '.join(row))
        print()
    def place_piece(self, x, y, symbol):
        self.grid[x][y] = symbol
    def is_valid_move(self, x, y):
        return 0 <= x < self.size and 0 <= y < self.size and self.grid[x][y] == '.'
    def is_full(self):
        return all(self.grid[x][y] != '.' for x in range(self.size) for y in range(self.size))
    def check_five_in_a_row(self, x, y, symbol):
        # Check horizontal, vertical, and both diagonal directions for five in a row
        return (self.check_direction(x, y, symbol, 1, 0) or  # Horizontal
                self.check_direction(x, y, symbol, 0, 1) or  # Vertical
                self.check_direction(x, y, symbol, 1, 1) or  # Diagonal /
                self.check_direction(x, y, symbol, 1, -1))   # Diagonal \
    def check_direction(self, x, y, symbol, dx, dy):
        count = 1
        # Check in both directions (positive and negative) from the starting point
        for direction in [1, -1]:
            nx, ny = x + direction * dx, y + direction * dy
            # Continue in the current direction while the symbol matches and within bounds
            while 0 <= nx < self.size and 0 <= ny < self.size and self.grid[nx][ny] == symbol:
                count += 1
                nx += direction * dx
                ny += direction * dy
        # Return True if five or more consecutive symbols are found
        return count >= 5