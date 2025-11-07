'''
Module to manage the deck of cards for Dou Dizhu.
'''
import random
from card import Card
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in range(3, 16)] + [Card('Joker', rank) for rank in ['Black', 'Red']]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, num_players):
        hands = [[] for _ in range(num_players)]
        for i in range(len(self.cards) - 3):
            hands[i % num_players].append(self.cards[i])
        return hands, self.cards[-3:]  # Return player hands and landlord cards