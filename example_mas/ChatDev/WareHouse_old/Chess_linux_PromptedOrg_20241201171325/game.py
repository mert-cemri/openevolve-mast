'''
Defines the Game class to manage the chess game flow.
'''
from utils import is_checkmate
class Game:
    def __init__(self, board):
        self.board = board
        self.turn = 'white'
    def play(self):
        while True:
            self.board.display()
            move = input(f"{self.turn}'s move: ")
            if self.board.is_valid_move(move, self.turn):
                self.board.move_piece(move)
                if self.check_winner():
                    print(f"{self.turn} wins!")
                    break
                self.switch_turn()
            else:
                print("Invalid move. Try again.")
    def check_winner(self):
        return is_checkmate(self.board, self.turn)
    def switch_turn(self):
        self.turn = 'black' if self.turn == 'white' else 'white'