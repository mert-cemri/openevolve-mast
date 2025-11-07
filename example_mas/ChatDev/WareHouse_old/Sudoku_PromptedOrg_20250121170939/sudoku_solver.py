'''
Defines the SudokuSolver class to solve the Sudoku puzzle.
'''
class SudokuSolver:
    def __init__(self, board):
        self.board = board
    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True  # Puzzle solved
        row, col = empty
        for num in range(1, 10):
            if self.board.is_valid_move(row, col, num):
                self.board.grid[row][col] = num
                if self.solve():
                    return True
                self.board.grid[row][col] = 0
        return False
    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.board.grid[i][j] == 0:
                    return (i, j)
        return None