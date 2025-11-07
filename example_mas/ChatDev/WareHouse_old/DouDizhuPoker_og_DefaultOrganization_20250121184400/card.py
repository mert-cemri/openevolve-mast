'''
Contains the Card class which represents a single card.
'''
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __repr__(self):
        return f"{self.rank} of {self.suit}"