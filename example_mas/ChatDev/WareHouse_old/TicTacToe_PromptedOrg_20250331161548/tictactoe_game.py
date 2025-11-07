'''
Handles the game logic for Tic-Tac-Toe, including the game board, player turns, and determining the winner.
'''
class TicTacToeGame:
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_player
            if self.check_winner(row, col):
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
            return True
        return False
    def check_winner(self, row, col):
        # Check the row, column, and diagonals for a win
        if all(self.board[row][c] == self.current_player for c in range(3)) or \
           all(self.board[r][col] == self.current_player for r in range(3)) or \
           (row == col and all(self.board[i][i] == self.current_player for i in range(3))) or \
           (row + col == 2 and all(self.board[i][2-i] == self.current_player for i in range(3))):
            return True
        return False
    def is_full(self):
        return all(self.board[row][col] != '' for row in range(3) for col in range(3))
    def reset(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None