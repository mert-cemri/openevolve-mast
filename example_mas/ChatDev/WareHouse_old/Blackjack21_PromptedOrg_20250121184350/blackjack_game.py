'''
BlackjackGame class to manage the game logic.
'''
from deck import Deck
from hand import Hand
class BlackjackGame:
    def __init__(self):
        self.deck = Deck()
        self.player_hand = Hand()
        self.dealer_hand = Hand()
        self.player_balance = 1000  # Example starting balance
        self.current_bet = 0
    def place_bet(self, amount):
        if amount > self.player_balance:
            print("Insufficient balance to place this bet.")
            return False
        self.current_bet = amount
        self.player_balance -= amount
        return True
    def player_turn(self):
        while True:
            action = input("Choose action: 'hit', 'stand', 'double down': ").lower()
            if action == 'hit':
                self.player_hand.add_card(self.deck.deal_card())
                print(f"Player's hand value: {self.player_hand.calculate_value()}")
                if self.player_hand.is_bust():
                    print("Player busts!")
                    return False
            elif action == 'stand':
                return True
            elif action == 'double down':
                if self.player_balance >= self.current_bet:  # Ensure sufficient balance for doubling
                    self.current_bet *= 2  # Double the bet
                    self.player_hand.add_card(self.deck.deal_card())
                    print(f"Player's hand value: {self.player_hand.calculate_value()}")
                    return not self.player_hand.is_bust()
                else:
                    print("Unable to double down due to insufficient balance.")
            else:
                print("Invalid action. Please choose 'hit', 'stand', or 'double down'.")
    def dealer_turn(self):
        while self.dealer_hand.calculate_value() < 17:
            self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Dealer's hand value: {self.dealer_hand.calculate_value()}")
        if self.dealer_hand.is_bust():
            print("Dealer busts!")
    def determine_winner(self):
        player_value = self.player_hand.calculate_value()
        dealer_value = self.dealer_hand.calculate_value()
        if player_value > 21:
            return "Dealer wins!"
        elif dealer_value > 21 or player_value > dealer_value:
            self.player_balance += self.current_bet * 2  # Player wins, double the bet
            return "Player wins!"
        elif player_value < dealer_value:
            return "Dealer wins!"
        else:
            self.player_balance += self.current_bet  # Tie, return the bet
            return "It's a tie!"
    def play_round(self):
        bet_amount = int(input("Enter your bet amount: "))
        if not self.place_bet(bet_amount):
            return
        self.player_hand.add_card(self.deck.deal_card())
        self.player_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        self.dealer_hand.add_card(self.deck.deal_card())
        print(f"Player's initial hand value: {self.player_hand.calculate_value()}")
        print(f"Dealer's visible card value: {self.dealer_hand.cards[0].value()}")
        if self.player_turn():
            self.dealer_turn()
            print(self.determine_winner())
        print(f"Player's balance: {self.player_balance}")