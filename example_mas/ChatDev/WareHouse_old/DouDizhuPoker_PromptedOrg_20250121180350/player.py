'''
Represents a player in the game.
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
    def has_won(self):
        return len(self.hand) == 0