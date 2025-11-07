'''
Defines the Deck class for managing a deck of cards.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in range(1, 14)]
        self.cards.extend([Card('Joker', 'Black'), Card('Joker', 'Red')])
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num_cards):
        dealt_cards = self.cards[:num_cards]
        self.cards = self.cards[num_cards:]
        return dealt_cards