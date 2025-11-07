'''
This module defines the SudokuBoard class which represents the Sudoku board and provides methods to manipulate, validate, and generate the board.
'''
import random
class SudokuBoard:
    def __init__(self, grid=None):
        if grid:
            self.grid = grid
        else:
            self.grid = [[0 for _ in range(9)] for _ in range(9)]
    def is_valid_move(self, row, col, num):
        # Check if the number is not already in the row, column, or 3x3 subgrid
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True
    def place_number(self, row, col, num):
        if self.is_valid_move(row, col, num):
            self.grid[row][col] = num
            return True
        return False
    def remove_number(self, row, col):
        self.grid[row][col] = 0
    def is_complete(self):
        for row in self.grid:
            if 0 in row:
                return False
        return True
    def generate_puzzle(self, num_clues=30):
        # Generate a complete solution
        self.solve()
        # Remove numbers to create a puzzle
        attempts = 81 - num_clues
        while attempts > 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            while self.grid[row][col] == 0:
                row, col = random.randint(0, 8), random.randint(0, 8)
            backup = self.grid[row][col]
            self.grid[row][col] = 0
            # Make a copy of the board and try to solve it
            board_copy = [row[:] for row in self.grid]
            from sudoku_solver import SudokuSolver
            solver = SudokuSolver()
            if not solver.solve(SudokuBoard(board_copy)):
                self.grid[row][col] = backup
                attempts -= 1
    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.place_number(row, col, num):
                            if self.solve():
                                return True
                            self.remove_number(row, col)
                    return False
        return True