'''
Represents a hand of cards for a player or dealer.
'''
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        # Calculate the total value considering Aces as 11 initially
        value = sum(card.value() if isinstance(card.value(), int) else card.value()[1] for card in self.cards)
        # Adjust for Aces
        num_aces = sum(1 for card in self.cards if card.rank == 1)
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def is_bust(self):
        return self.calculate_value() > 21