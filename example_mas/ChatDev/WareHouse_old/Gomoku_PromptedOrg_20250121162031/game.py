'''
Game class to manage the Gomoku game state.
'''
from board import Board
class Game:
    def __init__(self, player1, player2):
        self.board = Board(15)
        self.players = [player1, player2]
        self.current_player_index = 0
    @property
    def current_player(self):
        return self.players[self.current_player_index]
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
    def play_move(self, row, col):
        return self.board.place_stone(row, col, self.current_player.stone)
    def check_winner(self):
        return self.board.check_winner(self.current_player.stone)
    def is_draw(self):
        return self.board.is_full()