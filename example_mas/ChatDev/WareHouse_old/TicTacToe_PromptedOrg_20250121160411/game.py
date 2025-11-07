'''
This file contains the Game class which manages the game state, including the board, player turns, and determining the winner.
'''
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.current_player = 'X'
    def make_move(self, row, col):
        if self.board.update(row, col, self.current_player):
            return True
        return False
    def check_winner(self):
        # Check rows, columns, and diagonals for a win
        for i in range(3):
            if self.board.grid[i][0] == self.board.grid[i][1] == self.board.grid[i][2] != ' ':
                return True
            if self.board.grid[0][i] == self.board.grid[1][i] == self.board.grid[2][i] != ' ':
                return True
        if self.board.grid[0][0] == self.board.grid[1][1] == self.board.grid[2][2] != ' ':
            return True
        if self.board.grid[0][2] == self.board.grid[1][1] == self.board.grid[2][0] != ' ':
            return True
        return False
    def is_draw(self):
        for row in self.board.grid:
            if ' ' in row:
                return False
        return True
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'