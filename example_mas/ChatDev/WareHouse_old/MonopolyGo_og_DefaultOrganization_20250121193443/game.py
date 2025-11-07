'''
Manages the overall game state and flow.
'''
from player import Player
from board import Board
from dice import Dice
from gui import GUI
from chance import Chance
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.dice = Dice()
        self.gui = GUI(self)
        self.chance = Chance()
        self.current_player_index = 0
    def start_game(self):
        self.gui.update_display()
        self.gui.start()  # Start the GUI's main loop
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        self.gui.prompt_player_action(current_player)
    def roll_dice_and_move(self, player):
        roll = self.dice.roll()
        player.move(roll, self.board, self.chance)
        self.gui.update_display()
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.next_turn()