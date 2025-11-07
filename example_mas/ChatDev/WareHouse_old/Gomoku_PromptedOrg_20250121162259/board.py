'''
Board module to manage the Gomoku board.
'''
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [["." for _ in range(size)] for _ in range(size)]
    def display(self):
        for row in self.grid:
            print(" ".join(row))
        print()
    def place_stone(self, row, col, stone):
        if self.is_within_bounds(row, col) and self.grid[row][col] == ".":
            self.grid[row][col] = stone
            return True
        return False
    def is_within_bounds(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size