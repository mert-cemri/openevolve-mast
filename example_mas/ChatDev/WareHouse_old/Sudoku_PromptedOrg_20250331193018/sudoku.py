'''
Contains Sudoku class for puzzle logic, validation, checking completion, and explicitly checking for mistakes.
'''
class Sudoku:
    def __init__(self, puzzle):
        self.initial_grid = [row[:] for row in puzzle]  # Store initial puzzle state
        self.grid = [row[:] for row in puzzle]
    def is_cell_editable(self, row, col):
        # Check if the cell was initially empty
        return self.initial_grid[row][col] == 0
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
        # Check if all cells are filled
        for row in self.grid:
            if 0 in row:
                return False
        # Check rows and columns
        for i in range(9):
            row_nums = set()
            col_nums = set()
            for j in range(9):
                row_nums.add(self.grid[i][j])
                col_nums.add(self.grid[j][i])
            if len(row_nums) != 9 or len(col_nums) != 9:
                return False
        # Check 3x3 subgrids
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                nums = set()
                for i in range(3):
                    for j in range(3):
                        nums.add(self.grid[start_row + i][start_col + j])
                if len(nums) != 9:
                    return False
        return True
    def display(self):
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    print("|", end=" ")
                print(num if num != 0 else ".", end=" ")
            print()
        print()
    def set_value(self, row, col, num):
        if self.is_cell_editable(row, col):
            self.grid[row][col] = num
            return True
        else:
            return False
    def check_for_mistakes(self):
        mistakes = []
        for row in range(9):
            for col in range(9):
                num = self.grid[row][col]
                if num != 0:
                    self.grid[row][col] = 0  # Temporarily remove the number to check validity
                    if not self.is_valid_move(row, col, num):
                        mistakes.append((row, col))
                    self.grid[row][col] = num  # Restore the number
        return mistakes