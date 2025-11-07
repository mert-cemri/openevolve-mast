'''
Main entry point for the chess game. Manages the game loop and player interactions.
'''
from board import Board
from input_handler import InputHandler
class ChessGame:
    def __init__(self):
        self.board = Board()
        self.input_handler = InputHandler()
        self.current_player = 'White'
    def start_game(self):
        self.board.initialize_board()
        while True:
            self.board.print_board()
            print(f"{self.current_player}'s turn.")
            move = input("Enter your move (e.g., Ke8): ")
            if self.input_handler.validate_input(move):
                start_pos, end_pos = self.input_handler.parse_input(move)
                if self.board.move_piece(start_pos, end_pos, self.current_player):
                    if self.check_winner():
                        print(f"{self.current_player} wins!")
                        break
                    self.current_player = 'Black' if self.current_player == 'White' else 'White'
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid input format. Try again.")
    def check_winner(self):
        if self.board.is_checkmate(self.current_player):
            return True
        return False
if __name__ == "__main__":
    game = ChessGame()
    game.start_game()