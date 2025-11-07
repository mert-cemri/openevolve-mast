'''
Card class representing a single card.
'''
class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
    def __repr__(self):
        return f"{self.rank}{self.suit}"
    def value(self):
        order = {'3': 1, '4': 2, '5': 3, '6': 4, '7': 5, '8': 6, '9': 7, '10': 8,
                 'J': 9, 'Q': 10, 'K': 11, 'A': 12, '2': 13, 'Black Joker': 14, 'Red Joker': 15}
        return order[self.rank]