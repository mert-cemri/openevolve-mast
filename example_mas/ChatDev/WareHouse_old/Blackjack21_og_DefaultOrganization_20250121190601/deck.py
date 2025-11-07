'''
Represents a deck of cards for the Blackjack game.
'''
from card import Card
import random
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in range(1, 14)]
        random.shuffle(self.cards)
    def deal_card(self):
        return self.cards.pop()