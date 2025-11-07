'''
Main entry point for the Reversi (Othello) game application.
'''
from board import Board
from game import Game
from player import Player
def main():
    # Initialize players
    player1 = Player("Black")
    player2 = Player("White")
    # Initialize board
    board = Board()
    # Initialize game
    game = Game(board, player1, player2)
    # Start the game
    game.start()
if __name__ == "__main__":
    main()