'''
Defines the BlackjackGame class managing the game logic.
'''
from deck import Deck
from hand import Hand
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False
        self.player_standing = False
        self.bet = 0
    def start_new_round(self, initial_bet):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.game_over = False
        self.player_standing = False
        self.bet = initial_bet
        for _ in range(2):
            self.player_hand.add_card(self.deck.deal_card())
            self.dealer_hand.add_card(self.deck.deal_card())
    def hit(self):
        if not self.game_over and not self.player_standing:
            self.player_hand.add_card(self.deck.deal_card())
            if self.player_hand.get_value() > 21:
                self.game_over = True
    def stand(self):
        self.player_standing = True
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        self.game_over = True
    def double_down(self):
        if len(self.player_hand.cards) == 2 and not self.game_over:
            self.bet *= 2
            self.player_hand.add_card(self.deck.deal_card())
            self.player_standing = True
            self.stand()
    def check_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21 or player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"