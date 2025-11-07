'''
Defines the Sudoku puzzle logic including validation, completion check, and display functionality.
'''
class Sudoku:
    def __init__(self, puzzle):
        self.grid = [row[:] for row in puzzle]  # current puzzle state
        self.initial_grid = [row[:] for row in puzzle]  # initial puzzle state
    def is_valid_move(self, row, col, num):
        # Check row
        if num in self.grid[row]:
            return False
        # Check column
        for i in range(9):
            if self.grid[i][col] == num:
                return False
        # Check 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(start_row, start_row + 3):
            for j in range(start_col, start_col + 3):
                if self.grid[i][j] == num:
                    return False
        return True
    def is_completed(self):
        # Check rows and columns
        for i in range(9):
            row_nums = set()
            col_nums = set()
            for j in range(9):
                row_val = self.grid[i][j]
                col_val = self.grid[j][i]
                if row_val == 0 or col_val == 0:
                    return False
                if row_val in row_nums or col_val in col_nums:
                    return False
                row_nums.add(row_val)
                col_nums.add(col_val)
        # Check 3x3 subgrids
        for row in range(0, 9, 3):
            for col in range(0, 9, 3):
                nums = set()
                for i in range(row, row + 3):
                    for j in range(col, col + 3):
                        val = self.grid[i][j]
                        if val in nums:
                            return False
                        nums.add(val)
        return True
    def is_editable_cell(self, row, col):
        return self.initial_grid[row][col] == 0
    def display(self):
        print("-" * 25)
        for i, row in enumerate(self.grid):
            print("|", end=" ")
            for j, num in enumerate(row):
                print(num if num != 0 else ".", end=" ")
                if (j + 1) % 3 == 0:
                    print("|", end=" ")
            print()
            if (i + 1) % 3 == 0:
                print("-" * 25)