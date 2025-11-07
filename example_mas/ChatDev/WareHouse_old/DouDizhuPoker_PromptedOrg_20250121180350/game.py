'''
Manages the overall game logic.
'''
from deck import Deck
from player import Player
from combination_validator import CombinationValidator
import random
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player(f"Player {i+1}") for i in range(3)]
        self.landlord = None
        self.validator = CombinationValidator()
    def start_game(self):
        hands = self.deck.deal(3)
        for i, player in enumerate(self.players):
            player.receive_cards(hands[i])
        self.determine_landlord()
        self.play_rounds()
    def determine_landlord(self):
        # Simple logic to determine landlord (e.g., random or highest card)
        self.landlord = random.choice(self.players)
        print(f"{self.landlord.name} is the landlord.")
    def play_rounds(self):
        current_player_index = 0
        while True:
            current_player = self.players[current_player_index]
            print(f"{current_player.name}'s turn with hand: {current_player.hand}")
            played_cards = self.get_player_input(current_player)
            if played_cards:
                print(f"{current_player.name} played: {played_cards}")
                if current_player.has_won():
                    print(f"{current_player.name} has won the game!")
                    break
            current_player_index = (current_player_index + 1) % 3
    def get_player_input(self, player):
        # Simulate a valid play by the player
        valid_plays = self.get_valid_plays(player.hand)
        if valid_plays:
            return player.play_cards(valid_plays[0])
        return []
    def get_valid_plays(self, hand):
        # Generate all valid plays from the player's hand
        valid_plays = []
        for card in hand:
            if self.is_valid_play([card]):
                valid_plays.append([card])
        # Add more logic for pairs, straights, etc.
        return valid_plays
    def is_valid_play(self, cards):
        return self.validator.is_valid(cards)