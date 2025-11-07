'''
This module contains the Game class that manages the tic-tac-toe game state, including the board, current player, and game status.
'''
class Game:
    def __init__(self):
        '''Initialize the game board and set the starting player.'''
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def display_board(self):
        '''Print the current state of the board.'''
        for row in [self.board[i:i+3] for i in range(0, 9, 3)]:
            print('|'.join(row))
            print('-' * 5)
    def make_move(self, position):
        '''Allow a player to make a move if the chosen cell is empty.'''
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            return True
        return False
    def check_winner(self):
        '''Determine if there's a winner or if the game is a draw.'''
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Horizontal
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Vertical
            [0, 4, 8], [2, 4, 6]              # Diagonal
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False
    def switch_player(self):
        '''Change the current player after a move.'''
        self.current_player = 'O' if self.current_player == 'X' else 'X'