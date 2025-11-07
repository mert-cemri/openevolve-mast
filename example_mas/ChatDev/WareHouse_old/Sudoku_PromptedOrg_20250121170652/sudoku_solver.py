'''
This module defines the SudokuSolver class which provides a method to solve a Sudoku puzzle using backtracking.
'''
class SudokuSolver:
    def solve(self, board):
        for row in range(9):
            for col in range(9):
                if board.grid[row][col] == 0:
                    for num in range(1, 10):
                        if board.place_number(row, col, num):
                            if self.solve(board):
                                return True
                            board.remove_number(row, col)
                    return False
        return True