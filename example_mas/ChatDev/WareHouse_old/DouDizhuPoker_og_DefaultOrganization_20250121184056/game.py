'''
Handles the main game logic for Dou Dizhu.
'''
from deck import Deck
from player import Player
from rules import is_valid_combination
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(3)]
        self.landlord = None
        self.current_player_index = 0
        self.deal_cards()
        self.determine_landlord()
    def deal_cards(self):
        self.deck.shuffle()
        for i in range(17):
            for player in self.players:
                player.add_card(self.deck.draw_card())
        # Remaining cards are for the landlord
        self.landlord_cards = [self.deck.draw_card() for _ in range(3)]
    def determine_landlord(self):
        # Simple logic to assign landlord (could be more complex)
        self.landlord = self.players[0]
        self.landlord.add_cards(self.landlord_cards)
    def update(self):
        # Update game state, check for win conditions, etc.
        current_player = self.players[self.current_player_index]
        # Example logic for playing a turn
        # This would be replaced with actual game logic
        if current_player.has_won():
            print(f"{current_player.name} has won the game!")
            return
        self.current_player_index = (self.current_player_index + 1) % len(self.players)