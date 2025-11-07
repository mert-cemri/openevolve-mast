'''
Defines the SudokuGrid class to represent and manipulate the Sudoku grid.
'''
class SudokuGrid:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def is_valid_move(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False
        # Check column
        if num in [self.grid[i][col] for i in range(9)]:
            return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True
    def is_complete(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True
    def set_value(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.grid[row][col] = num
            return True
        return False
    def get_value(self, row, col):
        return self.grid[row][col]
    def print_grid(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))