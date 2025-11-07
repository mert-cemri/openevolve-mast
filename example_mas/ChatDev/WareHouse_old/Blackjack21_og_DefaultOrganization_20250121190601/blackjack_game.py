'''
Contains the game logic for Blackjack, including player and dealer actions.
'''
import random
from deck import Deck
from hand import Hand
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.start_new_game()
    def start_new_game(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
    def player_hit(self):
        self.player_hand.add_card(self.deck.deal_card())
    def player_stand(self):
        self.dealer_play()
    def player_double_down(self):
        self.player_hand.add_card(self.deck.deal_card())
        self.player_stand()  # Automatically stand after doubling down
    def dealer_play(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if self.player_hand.is_bust():
            return "Dealer wins!"
        elif self.dealer_hand.is_bust():
            return "Player wins!"
        elif player_value > dealer_value:
            return "Player wins!"
        elif dealer_value > player_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"