'''
Represents a single card in the deck.
'''
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def value(self):
        if self.rank > 10:
            return 10
        elif self.rank == 1:
            return [1, 11]  # Return both possible values for an Ace
        else:
            return self.rank