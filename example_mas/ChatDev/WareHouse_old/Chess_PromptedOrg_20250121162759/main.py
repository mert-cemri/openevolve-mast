'''
Main module to start and manage the chess game.
'''
from board import Board
from player import Player
class ChessGame:
    def __init__(self):
        self.board = Board()
        self.players = [Player("White"), Player("Black")]
        self.current_turn = 0
    def start_game(self):
        self.board.initialize_board()
        while not self.check_winner():
            self.board.print_board()
            current_player = self.players[self.current_turn]
            print(f"{current_player.color}'s turn")
            move = current_player.make_move()
            if self.board.move_piece(move, current_player.color):
                self.switch_turn()
            else:
                print("Invalid move. Try again.")
    def switch_turn(self):
        self.current_turn = 1 - self.current_turn
    def check_winner(self):
        # Implement checkmate, stalemate, and draw conditions
        return self.board.is_checkmate(self.players[self.current_turn].color) or \
               self.board.is_stalemate(self.players[self.current_turn].color)
if __name__ == "__main__":
    game = ChessGame()
    game.start_game()