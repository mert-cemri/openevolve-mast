'''
Represents a deck of cards.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['♠', '♥', '♦', '♣'] for rank in range(3, 16)] + [Card('Joker', 'Black'), Card('Joker', 'Red')]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num_players):
        return [self.cards[i::num_players] for i in range(num_players)]