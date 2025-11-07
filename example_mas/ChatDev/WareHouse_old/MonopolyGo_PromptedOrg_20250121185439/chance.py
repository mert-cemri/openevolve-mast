'''
Represents chance events that can occur when landing on a chance space.
'''
import random
class Chance:
    def __init__(self):
        self.cards = [
            "Advance to Go (Collect $200)",
            "Bank error in your favor. Collect $75",
            "Doctor's fees. Pay $50",
            # Add more chance cards as needed
        ]
    def draw_card(self):
        return random.choice(self.cards)