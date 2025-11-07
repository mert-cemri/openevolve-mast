'''
Game class to manage the game flow.
'''
from player import Player
from board import Board
from gui import GUI
from dice import Dice
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.gui = GUI(self)
        self.current_player_index = 0
    def start_game(self):
        self.board.setup_board()
        self.gui.setup_gui()
        while len([player for player in self.players if player.money > 0]) > 1:
            self.next_turn()
        # Determine the winner
        winner = max(self.players, key=lambda p: p.money)
        self.gui.display_winner([winner])
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        self.gui.update_display(current_player)
        # Roll the dice
        dice = Dice()
        steps = dice.roll()
        current_player.move(steps)
        # Get the property landed on
        property = self.board.get_property(current_player.position)
        # Handle property buying or rent payment
        if property.owner is None:
            # Logic for buying property
            if self.gui.prompt_buy_property(current_player, property):
                current_player.buy_property(property)
        else:
            # Logic for paying rent
            current_player.pay_rent(property)
        # Switch to next player
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.gui.update_display(current_player)