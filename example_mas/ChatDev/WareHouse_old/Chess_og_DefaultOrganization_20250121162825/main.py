'''
Main game loop and user interaction logic.
'''
from chessboard import ChessBoard
class Game:
    def __init__(self):
        self.board = ChessBoard()
        self.current_player = 'White'
    def play(self):
        while True:
            self.board.display()
            print(f"{self.current_player}'s turn. Enter your move (e.g., e2 e4):")
            try:
                move = input().strip()
            except EOFError:
                print("Input stream closed. Exiting game.")
                break
            try:
                start, end = move.split()
                if self.board.move_piece(start, end, self.current_player):
                    if self.board.is_checkmate(self.current_player):
                        print(f"Checkmate! {self.current_player} wins!")
                        break
                    self.current_player = 'Black' if self.current_player == 'White' else 'White'
                else:
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input format. Please enter your move in the format 'e2 e4'.")
if __name__ == "__main__":
    game = Game()
    game.play()