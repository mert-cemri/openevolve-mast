'''
Manages the flow of the chess game, handling player input and turn switching.
'''
from chessboard import ChessBoard
class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'
    def play(self):
        while True:
            self.board.display()
            move = input(f"{self.current_player}'s move: ")
            if self.board.move_piece(move):
                if self.board.is_checkmate(self.current_player):
                    print(f"Checkmate! {self.current_player} wins!")
                    break
                self.switch_player()
            else:
                print("Invalid move. Try again.")
    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'