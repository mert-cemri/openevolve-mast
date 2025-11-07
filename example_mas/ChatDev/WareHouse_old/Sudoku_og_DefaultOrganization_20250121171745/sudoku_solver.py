'''
This module defines the SudokuSolver class, which provides methods to solve the Sudoku puzzle using backtracking.
'''
class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Puzzle solved
        row, col = empty
        for num in range(1, 10):
            if self.grid.is_valid(row, col, num):
                self.grid.set_value(row, col, num)
                if self.solve():
                    return True
                self.grid.set_value(row, col, 0)
        return False
    def find_empty(self):
        for row in range(9):
            for col in range(9):
                if self.grid.grid[row][col] == 0:
                    return (row, col)
        return None