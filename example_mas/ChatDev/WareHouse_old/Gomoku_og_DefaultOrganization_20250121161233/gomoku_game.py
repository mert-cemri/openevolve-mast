'''
Manages the overall game logic for Gomoku.
'''
from game_board import GameBoard
class GomokuGame:
    def __init__(self):
        self.board = GameBoard()
        self.current_player = "Black"
    def switch_player(self):
        self.current_player = "White" if self.current_player == "Black" else "Black"
    def reset_game(self):
        self.board = GameBoard()
        self.current_player = "Black"