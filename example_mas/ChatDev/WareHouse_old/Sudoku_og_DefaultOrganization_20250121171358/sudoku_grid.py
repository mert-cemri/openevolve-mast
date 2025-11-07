'''
Module to represent and manage the Sudoku grid.
'''
class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def is_valid(self, row, col, num):
        # Check if num is not in the current row, column, and 3x3 subgrid
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True
    def is_complete(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True
    def is_grid_valid(self):
        # Check all rows and columns
        for i in range(9):
            row_numbers = [num for num in self.grid[i] if num != 0]
            col_numbers = [row[i] for row in self.grid if row[i] != 0]
            if len(set(row_numbers)) != len(row_numbers) or len(set(col_numbers)) != len(col_numbers):
                return False
        # Check all 3x3 subgrids
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                subgrid = [self.grid[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3) if self.grid[r][c] != 0]
                if len(set(subgrid)) != len(subgrid):
                    return False
        return True