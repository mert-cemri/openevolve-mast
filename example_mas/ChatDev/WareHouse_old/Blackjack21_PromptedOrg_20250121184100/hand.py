'''
Represents a player's or dealer's hand.
'''
from card import Card
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def get_value(self):
        value = 0
        num_aces = 0
        for card in self.cards:
            card_value = card.value()
            value += card_value
            if card.rank == 'A':
                num_aces += 1
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value