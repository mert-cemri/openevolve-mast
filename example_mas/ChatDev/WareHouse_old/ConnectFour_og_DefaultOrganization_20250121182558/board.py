'''
Contains the Board class to represent the Connect Four game board.
'''
class Board:
    def __init__(self):
        self.reset_board()
    def reset_board(self):
        self.board = [[0 for _ in range(7)] for _ in range(6)]
    def update_board(self, row, column, player):
        self.board[row][column] = player