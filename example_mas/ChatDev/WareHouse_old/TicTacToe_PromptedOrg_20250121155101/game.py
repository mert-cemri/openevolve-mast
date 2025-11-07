'''
This module contains the Game class which manages the tic-tac-toe game logic.
'''
class Game:
    def __init__(self):
        '''Initialize the game board and set the starting player.'''
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
        self.game_over = False
    def check_winner(self):
        '''Check if there is a winner after each move.'''
        win_conditions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # columns
            [0, 4, 8], [2, 4, 6]  # diagonals
        ]
        for condition in win_conditions:
            if self.board[condition[0]] == self.board[condition[1]] == self.board[condition[2]] != ' ':
                return True
        return False
    def switch_player(self):
        '''Switch the current player after a move.'''
        self.current_player = 'O' if self.current_player == 'X' else 'X'
    def is_draw(self):
        '''Check if the game is a draw.'''
        return ' ' not in self.board
    def make_move(self, position):
        '''Allow a player to make a move on the board.'''
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            if self.check_winner():
                self.game_over = True
                return f"Player {self.current_player} wins!"
            elif self.is_draw():
                self.game_over = True
                return "The game is a draw!"
            else:
                self.switch_player()
                return None
        else:
            return "Invalid move. Try again."