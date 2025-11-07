'''
Defines the Game class for managing the Dou Dizhu game logic.
'''
from deck import Deck
from player import Player
class Game:
    def __init__(self):
        self.deck = Deck()
        self.players = [Player("Player 1"), Player("Player 2"), Player("Landlord")]
        self.current_turn = 0
    def start_game(self):
        self.deck.shuffle()
        for player in self.players:
            player.receive_cards(self.deck.deal(17))
        self.players[-1].receive_cards(self.deck.deal(3))  # Landlord gets extra cards
    def next_turn(self):
        self.current_turn = (self.current_turn + 1) % len(self.players)
    def get_current_player(self):
        return self.players[self.current_turn]
    def play_turn(self, player, cards):
        if player.validate_play(cards):
            player.play_cards(cards)
            self.next_turn()
            return True
        return False
    def check_winner(self):
        for player in self.players:
            if not player.hand:
                return player.name
        return None