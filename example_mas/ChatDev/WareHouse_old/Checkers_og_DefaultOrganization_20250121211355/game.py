'''
Manages the overall game logic, including turn management and win conditions.
'''
from board import Board
class Game:
    def __init__(self):
        self.board = Board()
        self.current_turn = 'black'
        self.winner = None
    def play_turn(self, move):
        if self.winner:
            return
        if self.board.update(move, self.current_turn):
            self.current_turn = 'white' if self.current_turn == 'black' else 'black'
            self.check_winner()
    def check_winner(self):
        black_pieces = 0
        white_pieces = 0
        for row in self.board.grid:
            for piece in row:
                if piece:
                    if piece.color == 'black':
                        black_pieces += 1
                    elif piece.color == 'white':
                        white_pieces += 1
        if black_pieces == 0:
            self.winner = 'white'
        elif white_pieces == 0:
            self.winner = 'black'