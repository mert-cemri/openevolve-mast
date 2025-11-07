'''
Main file to start and manage the chess game.
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
        while True:
            self.print_board()
            move = self.players[self.current_turn].get_move()
            if self.board.is_valid_move(move, self.players[self.current_turn].color):
                self.board.update_board(move)
                if self.check_winner():
                    print(f"{self.players[self.current_turn].color} wins!")
                    break
                self.current_turn = 1 - self.current_turn
            else:
                print("Invalid move. Try again.")
    def print_board(self):
        self.board.display()
    def check_winner(self):
        return self.board.is_checkmate(self.players[self.current_turn].color)
if __name__ == "__main__":
    game = ChessGame()
    game.start_game()