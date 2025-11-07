'''
This module defines the Player and Dealer classes. Player represents a player in the game, including actions like 'hit', 'stand', and 'double down'. Dealer is a subclass of Player, with specific rules for hitting and standing.
'''
from hand import Hand
class Player:
    def __init__(self, name, balance=1000):  # Default balance set to 1000
        self.name = name
        self.hand = Hand()
        self.bet = 0
        self.balance = balance
    def place_bet(self, amount):
        if amount > self.balance:
            print("Insufficient balance to place this bet.")
            return False
        self.bet = amount
        self.balance -= amount
        return True
    def hit(self, deck):
        self.hand.add_card(deck.deal())
    def stand(self):
        pass
    def double_down(self, deck):
        if self.bet * 2 > self.balance + self.bet:
            print("Insufficient balance to double down.")
            return
        self.balance -= self.bet  # Deduct the additional bet amount
        self.bet *= 2
        self.hit(deck)
        # Automatically stand after doubling down
    def __str__(self):
        return f"{self.name}'s hand: {self.hand} (Value: {self.hand.calculate_value()})"
class Dealer(Player):
    def __init__(self):
        super().__init__("Dealer")
    def play(self, deck):
        while self.hand.calculate_value() < 17:
            self.hit(deck)
    def __str__(self, reveal_all=False):
        if reveal_all:
            return super().__str__()
        else:
            return f"Dealer's hand: {self.hand.cards[0]}, [Hidden]"