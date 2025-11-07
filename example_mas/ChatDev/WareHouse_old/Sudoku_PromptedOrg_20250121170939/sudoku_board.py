'''
Defines the SudokuBoard class to represent the Sudoku board.
'''
class SudokuBoard:
    def __init__(self):
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def is_valid_move(self, row, col, num):
        # Check if the number is not repeated in the row, column, and 3x3 subgrid
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
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
    def print_board(self):
        for row in self.grid:
            print(" ".join(str(num) if num != 0 else '.' for num in row))