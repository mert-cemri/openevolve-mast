'''
Manages the overall game flow, including player turns and game state.
'''
from player import Player
from board import Board
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.current_player_index = 0
    def start_game(self):
        while not self.check_winner():
            self.next_turn()
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        print(f"{current_player.name}'s turn.")
        dice_roll = current_player.roll_dice()
        current_player.move(self.board, dice_roll)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    def check_winner(self):
        active_players = [player for player in self.players if player.money > 0]
        if len(active_players) == 1:
            print(f"{active_players[0].name} is the winner!")
            return True
        return False