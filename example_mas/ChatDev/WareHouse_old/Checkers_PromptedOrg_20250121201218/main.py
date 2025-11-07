'''
Main file to run the Checkers game.
'''
from board import Board
from checkers_game import CheckersGame
def main():
    game = CheckersGame()
    game.play()
if __name__ == "__main__":
    main()