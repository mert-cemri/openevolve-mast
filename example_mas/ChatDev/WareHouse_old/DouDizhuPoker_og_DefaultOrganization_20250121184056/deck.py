'''
Manages the deck of cards for the Dou Dizhu game.
'''
import random
class Deck:
    def __init__(self):
        self.cards = [f"{rank}{suit}" for rank in "34567890JQKA2" for suit in "♠♥♦♣"] + ["Joker", "joker"]
        self.shuffle()
    def shuffle(self):
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()