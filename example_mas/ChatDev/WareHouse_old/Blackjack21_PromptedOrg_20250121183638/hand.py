'''
This module defines the Hand class, which represents a player's or dealer's hand, with methods to add cards and calculate the hand's value.
'''
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = 0
        aces = 0
        for card in self.cards:
            value += card.value()
            if card.rank == 'A':
                aces += 1
        while value > 21 and aces:
            value -= 10
            aces -= 1
        return value
    def is_bust(self):
        return self.calculate_value() > 21
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)