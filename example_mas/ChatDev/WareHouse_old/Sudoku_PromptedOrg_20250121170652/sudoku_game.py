'''
This module defines the SudokuGame class which manages the game logic and allows player interaction.
'''
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
class SudokuGame:
    def __init__(self):
        self.board = SudokuBoard()
        self.solver = SudokuSolver()
        self.board.generate_puzzle()
    def input_value(self, row, col, num):
        if self.board.place_number(row, col, num):
            return "Move accepted."
        else:
            return "Invalid move. Try again."
    def check_completion(self):
        return self.board.is_complete()