'''
Contains the SudokuSolver class which implements the backtracking algorithm to solve Sudoku puzzles.
'''
class SudokuSolver:
    def is_valid(self, board, row, col, num):
        # Check if the number is not repeated in the current row, column, and 3x3 box
        for i in range(9):
            if board[row][i] == num or board[i][col] == num:
                return False
        box_row_start = row - row % 3
        box_col_start = col - col % 3
        for i in range(3):
            for j in range(3):
                if board[i + box_row_start][j + box_col_start] == num:
                    return False
        return True
    def find_empty_location(self, board):
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0:
                    return row, col
        return None
    def solve(self, board):
        empty_location = self.find_empty_location(board)
        if not empty_location:
            return True  # Puzzle solved
        row, col = empty_location
        for num in range(1, 10):
            if self.is_valid(board, row, col, num):
                board[row][col] = num
                if self.solve(board):
                    return True
                board[row][col] = 0  # Backtrack
        return False