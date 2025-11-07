'''
Main file to manage the game flow of Monopoly Go!
'''
from board import Board
from player import Player
from dice import Dice
class Game:
    def __init__(self, player_names):
        self.players = [Player(name) for name in player_names]
        self.board = Board()
        self.dice = Dice()
        self.current_player_index = 0
    def start_game(self):
        print("Starting Monopoly Go!")
        while not self.check_winner():
            self.next_turn()
    def next_turn(self):
        if self.current_player_index >= len(self.players):
            self.current_player_index = 0
        player = self.players[self.current_player_index]
        print(f"{player.name}'s turn.")
        roll = self.dice.roll()
        print(f"Rolled a {roll}.")
        player.move(roll, self.board)
        self.remove_bankrupt_players()
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
    def check_winner(self):
        active_players = [player for player in self.players if player.money > 0]
        if len(active_players) == 1:
            print(f"{active_players[0].name} wins the game!")
            return True
        return False
    def remove_bankrupt_players(self):
        current_player = self.players[self.current_player_index]
        self.players = [player for player in self.players if player.money >= 0]
        if current_player not in self.players:
            self.current_player_index -= 1  # Adjust index if current player was removed
if __name__ == "__main__":
    player_names = ["Alice", "Bob"]
    game = Game(player_names)
    game.start_game()