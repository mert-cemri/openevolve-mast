'''
Game class to manage the overall game flow.
'''
from player import Player
from board import Board
from dice import Dice
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.dice = Dice()
        self.current_player_index = 0
    def start_game(self):
        while not self.check_winner():
            self.next_turn()
    def next_turn(self):
        if not self.players:
            print("No players left in the game.")
            return
        player = self.players[self.current_player_index]
        roll = self.dice.roll()
        player.move(roll, self.board)
        if player.money <= 0:
            print(f"{player.name} is bankrupt and removed from the game.")
            self.players.pop(self.current_player_index)
            if self.current_player_index >= len(self.players):
                self.current_player_index = 0
        else:
            self.current_player_index = (self.current_player_index + 1) % len(self.players)
    def check_winner(self):
        active_players = [player for player in self.players if player.money > 0]
        if len(active_players) == 1:
            print(f"{active_players[0].name} is the winner!")
            return True
        return False