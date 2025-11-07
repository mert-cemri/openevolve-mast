'''
This module contains the Game class, which manages the game flow, including player turns and checking for game over conditions.
'''
from board import Board
from player import Player
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player_index = 0
    def start(self):
        while True:
            self.board.display()
            current_player = self.players[self.current_player_index]
            print(f"Player {current_player.symbol}'s turn.")
            column = current_player.choose_column(self.board)
            if self.board.place_disc(column, current_player.symbol):
                if self.board.check_winner(current_player.symbol):
                    self.board.display()
                    print(f"Player {current_player.symbol} wins!")
                    break
                elif self.board.is_full():
                    self.board.display()
                    print("It's a draw!")
                    break
                self.current_player_index = 1 - self.current_player_index
            else:
                print("Column is full. Try again.")