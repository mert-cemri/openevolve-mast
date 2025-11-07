'''
Defines the Card class representing a single playing card.
'''
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def __str__(self):
        return f"{self.rank} of {self.suit}"
    def __repr__(self):
        return self.__str__()