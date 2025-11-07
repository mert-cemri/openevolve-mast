'''
This module defines the Deck class, which represents a deck of cards, allowing for shuffling and dealing.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self):
        return self.cards.pop()