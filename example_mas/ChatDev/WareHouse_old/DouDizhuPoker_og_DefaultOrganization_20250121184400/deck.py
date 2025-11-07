'''
Contains the Deck class which manages the deck of cards.
'''
from card import Card
import random
class Deck:
    def __init__(self):
        self.cards = [Card(suit, rank) for suit in ['Hearts', 'Diamonds', 'Clubs', 'Spades']
                      for rank in range(1, 14)]
        self.cards += [Card('Joker', 1), Card('Joker', 2)]  # Add two jokers
    def shuffle(self):
        random.shuffle(self.cards)
    def deal(self, players):
        '''
        Deals cards to players, with the landlord receiving more cards.
        '''
        num_players = len(players)
        num_cards_per_player = len(self.cards) // num_players
        for player in players:
            player.draw_cards(self, num_cards_per_player)
        # Give remaining cards to the landlord
        players[-1].draw_cards(self, len(self.cards))