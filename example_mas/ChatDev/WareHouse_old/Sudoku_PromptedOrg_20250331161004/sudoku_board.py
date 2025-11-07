'''
Defines the SudokuBoard class, which represents the Sudoku grid and contains methods for board manipulation and validation.
'''
class SudokuBoard:
    def __init__(self, board):
        self.board = board
    def is_valid_move(self, row, col, num):
        # Check if the number is not in the current row, column, and 3x3 subgrid
        for i in range(9):
            if self.board[row][i] == num or self.board[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.board[start_row + i][start_col + j] == num:
                    return False
        return True
    def is_complete(self):
        # Check if there are any zeros left in the board
        for row in self.board:
            if 0 in row:
                return False
        # Check if all rows, columns, and 3x3 subgrids contain numbers 1-9 exactly once
        for i in range(9):
            if not self.is_valid_group(self.board[i]) or not self.is_valid_group([self.board[j][i] for j in range(9)]):
                return False
        for start_row in range(0, 9, 3):
            for start_col in range(0, 9, 3):
                subgrid = [self.board[r][c] for r in range(start_row, start_row + 3) for c in range(start_col, start_col + 3)]
                if not self.is_valid_group(subgrid):
                    return False
        return True
    def is_valid_group(self, group):
        # Helper method to check if a group (row, column, or subgrid) contains numbers 1-9 exactly once
        return sorted(group) == list(range(1, 10))
    def place_number(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.board[row][col] = num
            return True
        return False