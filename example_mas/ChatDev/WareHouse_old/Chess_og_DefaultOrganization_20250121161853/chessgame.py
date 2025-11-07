'''
Defines the ChessGame class to manage the flow of the chess game.
'''
from chessboard import ChessBoard
from player import Player
class ChessGame:
    def __init__(self):
        self.board = ChessBoard()
        self.players = [Player("white"), Player("black")]
        self.current_player_index = 0
    def play(self):
        # Main loop to handle player turns and check game status
        try:
            while True:
                self.board.display_board()
                current_player = self.players[self.current_player_index]
                print(f"{current_player.color}'s turn. Enter your move (e.g., e2e4): ")
                move = input().strip()
                if self.board.is_valid_move(move):
                    self.board.move_piece(move)
                    if self.board.is_checkmate():
                        print(f"Checkmate! {current_player.color} wins!")
                        break
                    elif self.board.is_stalemate():
                        print("Stalemate! The game is a draw.")
                        break
                    self.current_player_index = 1 - self.current_player_index
                else:
                    print("Invalid move. Try again.")
        except EOFError:
            print("Input stream closed unexpectedly. Exiting the game.")