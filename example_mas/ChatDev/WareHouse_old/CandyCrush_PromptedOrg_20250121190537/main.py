'''
Main entry point for the match-3 puzzle game.
'''
from board import Board
from game import Game
def main():
    game = Game()
    game.play()
if __name__ == "__main__":
    main()