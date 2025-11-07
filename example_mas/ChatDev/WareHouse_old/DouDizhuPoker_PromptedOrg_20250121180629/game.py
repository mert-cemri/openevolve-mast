'''
Defines the Game class, which manages the overall game flow, including dealing cards, determining the landlord, and handling turns.
'''
from deck import Deck
from player import Player
from hand_validator import HandValidator
class Game:
    def __init__(self):
        self.players = [Player(f"Player {i+1}") for i in range(3)]
        self.deck = Deck()
        self.landlord = None
    def start(self):
        self.deal_cards()
        self.determine_landlord()
        self.play_game()
    def deal_cards(self):
        hands = self.deck.deal(3)
        for i, player in enumerate(self.players):
            player.receive_cards(hands[i])
    def determine_landlord(self):
        # Simple logic to choose the first player as the landlord
        self.landlord = self.players[0]
        print(f"{self.landlord.name} is the landlord.")
    def play_game(self):
        current_player_index = 0
        while not self.is_game_over():
            current_player = self.players[current_player_index]
            print(f"{current_player.name}'s turn. Current hand: {current_player.hand}")
            # Placeholder for player input
            # Example: cards_to_play = self.get_player_input(current_player)
            # if self.validate_play(cards_to_play):
            #     current_player.play_cards(cards_to_play)
            # else:
            #     print("Invalid play. Try again.")
            current_player_index = (current_player_index + 1) % 3
        self.declare_winner()
    def is_game_over(self):
        return any(len(player.hand) == 0 for player in self.players)
    def declare_winner(self):
        for player in self.players:
            if len(player.hand) == 0:
                print(f"{player.name} wins the game!")
    def validate_play(self, cards):
        return HandValidator.validate(cards)