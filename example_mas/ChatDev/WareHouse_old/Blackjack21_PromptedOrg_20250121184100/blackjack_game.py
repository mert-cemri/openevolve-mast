'''
Manages the game logic for Blackjack.
'''
from deck import Deck
from hand import Hand
class BlackjackGame:
    def __init__(self, deck, player_hand, dealer_hand, initial_bet=10):
        self.deck = deck
        self.player_hand = player_hand
        self.dealer_hand = dealer_hand
        self.player_bet = initial_bet
    def start(self):
        self.deck.shuffle()
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.show_hands()
        while True:
            action = input("Choose an action: 'hit', 'stand', 'double down': ").lower()
            if action == 'hit':
                self.player_hit()
                if self.player_hand.get_value() > 21:
                    return  # End the game immediately if the player busts
            elif action == 'stand':
                self.player_stand()
                break
            elif action == 'double down':
                self.player_double_down()
                if self.player_hand.get_value() > 21:
                    return  # End the game immediately if the player busts
                break
            else:
                print("Invalid action. Please choose 'hit', 'stand', or 'double down'.")
        self.dealer_play()
        self.check_winner()
    def show_hands(self):
        print("\nPlayer's Hand:")
        for card in self.player_hand.cards:
            print(f"{card.rank} of {card.suit}")
        print(f"Value: {self.player_hand.get_value()}")
        print("\nDealer's Hand:")
        print(f"{self.dealer_hand.cards[0].rank} of {self.dealer_hand.cards[0].suit}")
        print("Hidden Card")
    def player_hit(self):
        self.player_hand.add_card(self.deck.deal_card())
        self.show_hands()
        if self.player_hand.get_value() > 21:
            print("Player busts!")
            self.check_winner()
    def player_stand(self):
        print("Player stands.")
    def player_double_down(self):
        self.player_bet *= 2
        self.player_hand.add_card(self.deck.deal_card())
        print("Player doubles down.")
        self.show_hands()
        if self.player_hand.get_value() > 21:
            print("Player busts!")
            self.check_winner()
            return  # End the game immediately if the player busts
        else:
            print("Player stands after doubling down.")
        self.dealer_play()
        self.check_winner()
    def dealer_play(self):
        print("\nDealer's Turn:")
        while self.dealer_hand.get_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        self.show_final_hands()
    def show_final_hands(self):
        print("\nFinal Hands:")
        print("Player's Hand:")
        for card in self.player_hand.cards:
            print(f"{card.rank} of {card.suit}")
        print(f"Value: {self.player_hand.get_value()}")
        print("\nDealer's Hand:")
        for card in self.dealer_hand.cards:
            print(f"{card.rank} of {card.suit}")
        print(f"Value: {self.dealer_hand.get_value()}")
    def check_winner(self):
        player_value = self.player_hand.get_value()
        dealer_value = self.dealer_hand.get_value()
        if player_value > 21:
            print("Dealer wins!")
        elif dealer_value > 21 or player_value > dealer_value:
            print("Player wins!")
        elif player_value < dealer_value:
            print("Dealer wins!")
        else:
            print("It's a tie!")