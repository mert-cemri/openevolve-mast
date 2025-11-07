'''
Main module to start and manage the Blackjack game.
'''
from deck import Deck
from hand import Hand
from blackjack_game import BlackjackGame
def play_game():
    deck = Deck()
    player_hand = Hand()
    dealer_hand = Hand()
    game = BlackjackGame(deck, player_hand, dealer_hand)
    game.start()
if __name__ == "__main__":
    play_game()