'''
sudoku_grid.py
This module contains the SudokuGrid class which represents the Sudoku grid and provides methods to manipulate and validate it.
'''
class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def set_value(self, row, col, value):
        if 0 <= row < 9 and 0 <= col < 9 and 1 <= value <= 9:
            self.grid[row][col] = value
    def is_valid(self):
        # Check rows, columns, and 3x3 subgrids
        for i in range(9):
            if not self.is_valid_line(self.grid[i]) or not self.is_valid_line([self.grid[j][i] for j in range(9)]):
                return False
        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid_subgrid(i, j):
                    return False
        return True
    def is_complete(self):
        return all(all(cell != 0 for cell in row) for row in self.grid)
    def is_valid_line(self, line):
        # Filter out zeros and check if the remaining numbers are unique
        non_zero_numbers = [num for num in line if num != 0]
        return len(non_zero_numbers) == len(set(non_zero_numbers))
    def is_valid_subgrid(self, row, col):
        subgrid = [self.grid[r][c] for r in range(row, row + 3) for c in range(col, col + 3)]
        return self.is_valid_line(subgrid)