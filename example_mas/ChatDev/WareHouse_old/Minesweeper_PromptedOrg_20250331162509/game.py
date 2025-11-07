'''
This file contains the Game class, which manages the overall game state, including the board, difficulty levels, and game status.
'''
from board import Board
class Game:
    def __init__(self, difficulty):
        self.difficulty = difficulty
        self.board = Board(difficulty)
        self.game_over = False
        self.won = False
    def is_over(self):
        return self.game_over
    def is_won(self):
        return self.won
    def display_board(self):
        self.board.display()
    def uncover_cell(self, x, y):
        if not (0 <= x < self.board.size and 0 <= y < self.board.size):
            print("Coordinates out of bounds. Please enter valid coordinates.")
            return
        if self.board.uncover(x, y):
            self.game_over = True
        elif self.board.is_cleared():
            self.won = True
            self.game_over = True
    def flag_cell(self, x, y):
        if not (0 <= x < self.board.size and 0 <= y < self.board.size):
            print("Coordinates out of bounds. Please enter valid coordinates.")
            return
        self.board.flag(x, y)