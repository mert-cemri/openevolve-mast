'''
Module to solve the Sudoku puzzle using backtracking.
'''
from sudoku_grid import SudokuGrid
class SudokuSolver:
    def __init__(self, grid):
        self.grid = grid
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.grid.is_valid(row, col, num):
                            self.grid.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid.grid[row][col] = 0
                    return False
        return True