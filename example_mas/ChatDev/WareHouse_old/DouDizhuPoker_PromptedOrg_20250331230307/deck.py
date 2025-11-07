'''
Deck class to handle card creation, shuffling, and dealing.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        suits = ['♠', '♥', '♣', '♦']
        ranks = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
        self.cards = [Card(rank, suit) for suit in suits for rank in ranks]
        self.cards += [Card('Black Joker', ''), Card('Red Joker', '')]
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, players):
        for i in range(17):
            for player in players:
                player.receive_card(self.cards.pop())
        self.bottom_cards = self.cards  # Remaining 3 cards for landlord