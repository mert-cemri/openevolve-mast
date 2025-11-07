'''
Module to represent a player in Dou Dizhu.
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
        return cards
    def __repr__(self):
        return f"{self.name} with hand: {self.hand}"