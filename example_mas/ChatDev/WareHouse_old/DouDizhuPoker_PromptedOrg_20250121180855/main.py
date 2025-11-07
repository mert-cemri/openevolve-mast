'''
Main module to run the Dou Dizhu game.
'''
from deck import Deck
from player import Player
from game import Game
def main():
    # Initialize deck and players
    deck = Deck()
    players = [Player(f"Player {i+1}") for i in range(3)]
    # Initialize and start the game
    game = Game(deck, players)
    game.start()
if __name__ == "__main__":
    main()