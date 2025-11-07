'''
This module defines the BlackjackGame class, which manages the game flow, including dealing cards, handling player actions, and determining the winner.
'''
from deck import Deck
from player import Player, Dealer
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player("Player")
        self.dealer = Dealer()
    def start_game(self):
        self.deck.shuffle()
        while not self.player.place_bet(float(input("Place your bet: "))):
            pass  # Keep asking for a valid bet
        self.initial_deal()
        self.player_turn()
        self.dealer_turn()
        self.determine_winner()
    def initial_deal(self):
        for _ in range(2):
            self.player.hit(self.deck)
            self.dealer.hit(self.deck)
        print(self.player)
        print(self.dealer.__str__(reveal_all=False))
    def player_turn(self):
        while True:
            action = input("Choose an action: 'hit', 'stand', 'double down': ").lower()
            if action == 'hit':
                self.player.hit(self.deck)
                print(self.player)
                if self.player.hand.is_bust():
                    print("Player busts!")
                    return
            elif action == 'stand':
                break
            elif action == 'double down':
                self.player.double_down(self.deck)
                print(self.player)
                if self.player.hand.is_bust():
                    print("Player busts!")
                return
    def dealer_turn(self):
        print("Dealer's turn.")
        self.dealer.play(self.deck)
        print(self.dealer.__str__(reveal_all=True))
        if self.dealer.hand.is_bust():
            print("Dealer busts!")
    def determine_winner(self):
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.hand.calculate_value()
        if player_value > 21:
            print("Dealer wins!")
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")