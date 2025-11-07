'''
Manages the overall game flow, including player turns and game state.
'''
from player import Player
from board import Board
from gui import GUI
import random
class Game:
    def __init__(self):
        self.players = [Player("Player 1"), Player("Player 2")]
        self.board = Board()
        self.gui = GUI(self)
        self.current_player_index = 0
    def start_game(self):
        self.gui.update_display()
        self.next_turn()
        self.gui.root.mainloop()  # Start the Tkinter main event loop here
    def next_turn(self):
        current_player = self.players[self.current_player_index]
        self.gui.prompt_player_action(current_player)
        self.take_turn(current_player)
        self.current_player_index = (self.current_player_index + 1) % len(self.players)
        self.gui.update_display()
    def take_turn(self, player):
        # Roll dice
        dice_roll = random.randint(1, 6) + random.randint(1, 6)
        player.move(dice_roll)
        # Check property
        property = self.board.get_property(player.position)
        if property:
            if property.owner is None:
                if player.money >= property.price:
                    player.buy_property(property)
            else:
                property.charge_rent(player)
        else:
            # Handle chance if no property
            self.board.handle_chance(player, self.players)