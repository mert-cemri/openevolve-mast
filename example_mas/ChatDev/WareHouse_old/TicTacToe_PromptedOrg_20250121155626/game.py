'''
This file contains the Game class, which manages the tic-tac-toe game state and logic.
'''
class Game:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
    def display_board(self):
        for i, row in enumerate(self.board):
            print('|'.join(row))
            if i < 2:  # Only print the separator between rows
                print('-----')
    def make_move(self, row, col):
        if self.board[row][col] == ' ':
            self.board[row][col] = self.current_player
            return True
        return False
    def check_winner(self):
        # Check rows, columns, and diagonals
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != ' ':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != ' ':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != ' ':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != ' ':
            return True
        return False
    def is_draw(self):
        for row in self.board:
            if ' ' in row:
                return False
        return True
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'