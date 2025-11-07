'''
This module defines the SudokuGrid class, which represents the 9x9 Sudoku grid and provides methods to check for mistakes and confirm puzzle completion.
'''
class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def set_value(self, row, col, value):
        if 1 <= value <= 9:
            self.grid[row][col] = value
    def is_valid(self, row, col, value):
        # Check row and column
        for i in range(9):
            if self.grid[row][i] == value or self.grid[i][col] == value:
                return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == value:
                    return False
        return True
    def is_complete(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return False
        return True