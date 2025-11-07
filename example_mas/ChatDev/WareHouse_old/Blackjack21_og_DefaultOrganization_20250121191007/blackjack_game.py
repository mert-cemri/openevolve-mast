'''
Contains the core game logic for the Blackjack game.
'''
import random
class Card:
    def __init__(self, suit, rank):
        self.suit = suit
        self.rank = rank
    def value(self):
        if self.rank in ['J', 'Q', 'K']:
            return 10
        elif self.rank == 'A':
            return 11
        else:
            return int(self.rank)
class Deck:
    def __init__(self):
        suits = ['Hearts', 'Diamonds', 'Clubs', 'Spades']
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
        self.cards = [Card(suit, rank) for suit in suits for rank in ranks]
        random.shuffle(self.cards)
    def draw_card(self):
        return self.cards.pop()
class Hand:
    def __init__(self):
        self.cards = []
    def add_card(self, card):
        self.cards.append(card)
    def calculate_value(self):
        value = sum(card.value() for card in self.cards)
        num_aces = sum(1 for card in self.cards if card.rank == 'A')
        while value > 21 and num_aces:
            value -= 10
            num_aces -= 1
        return value
    def is_bust(self):
        return self.calculate_value() > 21
class Player:
    def __init__(self, bankroll=100):
        self.hand = Hand()
        self.bankroll = bankroll
        self.current_bet = 0
        self.turn_over = False
    def bet(self, amount):
        self.current_bet = amount
        self.bankroll -= amount
    def hit(self, deck):
        self.hand.add_card(deck.draw_card())
    def stand(self):
        self.turn_over = True
    def double_down(self, deck):
        if self.bankroll >= self.current_bet:
            self.bet(self.current_bet)
            self.hit(deck)
            self.stand()
        else:
            print("Insufficient funds to double down.")
class Dealer:
    def __init__(self):
        self.hand = Hand()
    def play(self, deck):
        while self.hand.calculate_value() < 17:
            self.hand.add_card(deck.draw_card())
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player = Player()
        self.dealer = Dealer()
    def start_game(self):
        self.player.hand = Hand()
        self.dealer.hand = Hand()
        self.player.hit(self.deck)
        self.player.hit(self.deck)
        self.dealer.hand.add_card(self.deck.draw_card())
        self.dealer.hand.add_card(self.deck.draw_card())
    def player_turn(self, action):
        if not self.player.turn_over:
            if action == 'hit':
                self.player.hit(self.deck)
            elif action == 'stand':
                self.player.stand()
            elif action == 'double_down':
                self.player.double_down(self.deck)
    def dealer_turn(self):
        self.dealer.play(self.deck)
    def determine_winner(self):
        player_value = self.player.hand.calculate_value()
        dealer_value = self.dealer.hand.calculate_value()
        if self.player.hand.is_bust():
            return "Dealer wins!"
        elif self.dealer.hand.is_bust() or player_value > dealer_value:
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            return "It's a tie!"