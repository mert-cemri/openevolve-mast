'''
Defines the Player class, which represents a player in the game, including the landlord.
'''
class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []
    def receive_cards(self, cards):
        self.hand.extend(cards)
    def play_cards(self, cards):
        for card in cards:
            self.hand.remove(card)
    def __repr__(self):
        return f"Player({self.name}, Hand: {self.hand})"