'''
This module contains the SudokuSolver class which implements the backtracking algorithm to solve a Sudoku puzzle.
'''
class SudokuSolver:
    def __init__(self, board):
        self.board = board
    def solve(self):
        '''
        Public method to solve the Sudoku puzzle.
        Returns the solved board if a solution exists, otherwise returns None.
        '''
        if self._solve_sudoku():
            return self.board
        else:
            return None
    def _solve_sudoku(self):
        '''
        Private method to solve the Sudoku puzzle using backtracking.
        Returns True if a solution is found, otherwise returns False.
        '''
        empty = self._find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self._is_valid(num, row, col):
                self.board[row][col] = num
                if self._solve_sudoku():
                    return True
                self.board[row][col] = 0
        return False
    def _find_empty(self):
        '''
        Private method to find an empty cell in the Sudoku board.
        Returns the position of the empty cell as a tuple (row, col), otherwise returns None.
        '''
        for i in range(9):
            for j in range(9):
                if self.board[i][j] == 0:
                    return (i, j)
        return None
    def _is_valid(self, num, row, col):
        '''
        Private method to check if placing a number in a specific cell is valid.
        Returns True if the placement is valid, otherwise returns False.
        '''
        # Check row
        for i in range(9):
            if self.board[row][i] == num and col != i:
                return False
        # Check column
        for i in range(9):
            if self.board[i][col] == num and row != i:
                return False
        # Check box
        box_x = col // 3
        box_y = row // 3
        for i in range(box_y * 3, box_y * 3 + 3):
            for j in range(box_x * 3, box_x * 3 + 3):
                if self.board[i][j] == num and (i, j) != (row, col):
                    return False
        return True