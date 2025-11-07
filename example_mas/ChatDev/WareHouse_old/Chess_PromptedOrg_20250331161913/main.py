'''
Main module to start and manage the chess game.
'''
from board import Board
from player import Player
class ChessGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player('White'), Player('Black')]
        self.current_player_index = 0
    def start_game(self):
        self.board.initialize_board()
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"{current_player.color}'s turn")
            move = current_player.make_move()
            if self.board.process_move(move, current_player.color):
                if self.board.is_checkmate(current_player.color):
                    print(f"Checkmate! {current_player.color} wins!")
                    break
                elif self.board.is_stalemate(current_player.color):
                    print("Stalemate! It's a draw!")
                    break
                self.current_player_index = 1 - self.current_player_index
            else:
                print("Invalid move. Try again.")
if __name__ == "__main__":
    game = ChessGame()
    game.start_game()