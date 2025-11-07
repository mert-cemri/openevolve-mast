'''
This module contains the Game class, which manages the overall game state, player turns, and determines the winner.
'''
from board import Board
from player import Player
class Game:
    def __init__(self):
        self.board = Board()
        self.players = [Player("X"), Player("O")]
        self.current_player_index = 0
    def start(self):
        self.board.create_window(self.players, self.switch_player)
    def switch_player(self):
        self.current_player_index = 1 - self.current_player_index
        return self.players[self.current_player_index]