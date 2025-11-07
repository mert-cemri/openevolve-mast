'''
Main executable file to run the chess game from terminal.
'''
from chessboard import ChessBoard
from utils import parse_move, print_board, is_checkmate, is_stalemate
class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'white'
    def switch_player(self):
        self.current_player = 'black' if self.current_player == 'white' else 'white'
    def play(self):
        while True:
            print_board(self.board)
            if is_checkmate(self.board, self.current_player):
                print(f"Checkmate! {self.current_player.capitalize()} loses.")
                break
            if is_stalemate(self.board, self.current_player):
                print("Stalemate! It's a draw.")
                break
            move_input = input(f"{self.current_player.capitalize()} move (e.g., e2e4, O-O, e7e8Q): ")
            move = parse_move(move_input, self.board, self.current_player)
            if move and self.board.make_move(move):
                self.switch_player()
            else:
                print("Invalid move. Try again.")
if __name__ == "__main__":
    game = ChessGame()
    game.play()