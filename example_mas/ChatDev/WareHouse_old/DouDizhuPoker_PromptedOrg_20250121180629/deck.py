'''
Defines the Deck class, which manages a collection of cards and handles shuffling and dealing.
'''
import random
from card import Card
class Deck:
    suits = ['♠', '♥', '♦', '♣']
    ranks = ['3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A', '2']
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in self.suits for rank in self.ranks]
        self.cards.extend([Card('', 'Joker'), Card('', 'Joker')])  # Add Jokers
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num_players):
        self.shuffle()
        return [self.cards[i::num_players] for i in range(num_players)]