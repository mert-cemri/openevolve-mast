'''
Main module to run the Dou Dizhu game.
'''
from deck import Deck
from player import Player
from game import Game
def main():
    # Initialize the game
    game = Game()
    game.start_game()
if __name__ == "__main__":
    main()