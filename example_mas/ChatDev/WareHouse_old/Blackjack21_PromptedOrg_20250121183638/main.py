'''
This is the main file to run the Blackjack game. It initializes the game and manages the game loop.
'''
from deck import Deck
from player import Player, Dealer
from blackjack_game import BlackjackGame
def main():
    print("Welcome to Blackjack!")
    game = BlackjackGame()
    game.start_game()
if __name__ == "__main__":
    main()