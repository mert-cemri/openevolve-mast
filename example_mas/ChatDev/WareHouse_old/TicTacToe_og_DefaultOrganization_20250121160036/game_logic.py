'''
This module contains the TicTacToeGame class which handles the game logic,
including checking for a winner, checking for a draw, and resetting the game.
'''
class TicTacToeGame:
    def __init__(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
    def make_move(self, row, col, player):
        if self.board[row][col] == "":
            self.board[row][col] = player
    def check_winner(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False
    def is_draw(self):
        for row in self.board:
            if "" in row:
                return False
        return not self.check_winner()
    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]