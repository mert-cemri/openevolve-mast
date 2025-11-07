'''
Manage the Tic-Tac-Toe game state and logic.
'''
class Game:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def reset_game(self):
        '''
        Reset the game to its initial state.
        '''
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, position):
        '''
        Handle a player's move.
        '''
        if self.board[position] == ' ' and not self.winner:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.current_player = 'O' if self.current_player == 'X' else 'X'
    def check_winner(self):
        '''
        Determine if there's a winner or if the game is a draw.
        '''
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return False
    def is_draw(self):
        '''
        Check if the game is a draw.
        '''
        return ' ' not in self.board and not self.winner