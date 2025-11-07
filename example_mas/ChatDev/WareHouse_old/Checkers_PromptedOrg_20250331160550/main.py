'''
This module contains the main game loop for the Checkers game, managing the game flow and user interaction.
'''
from board import Board
from utils import parse_move, print_board
class CheckersGame:
    def __init__(self):
        self.board = Board()
        self.current_player = 'W'  # W for White, B for Black
    def switch_player(self):
        self.current_player = 'B' if self.current_player == 'W' else 'W'
    def play(self):
        print("Welcome to Checkers!")
        while not self.board.is_game_over(self.current_player):
            print_board(self.board)
            print(f"Player {self.current_player}'s turn.")
            move = input("Enter your move (e.g., A3-B4): ")
            from_pos, to_pos = parse_move(move)
            if self.board.is_valid_move(from_pos, to_pos, self.current_player):
                turn_over = self.board.apply_move(from_pos, to_pos)
                if turn_over:
                    self.switch_player()
            else:
                print("Invalid move. Try again.")
        print("Game over!")
if __name__ == "__main__":
    game = CheckersGame()
    game.play()