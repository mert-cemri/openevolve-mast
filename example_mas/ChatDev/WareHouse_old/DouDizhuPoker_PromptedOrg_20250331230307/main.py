'''
Main file to run the Dou Dizhu game.
'''
from deck import Deck
from player import Player
from game_logic import Game
def main():
    deck = Deck()
    deck.shuffle()
    players = [Player("Player1"), Player("Player2"), Player("Player3")]
    deck.deal(players)
    game = Game(players, deck)
    game.start_game()
if __name__ == "__main__":
    main()