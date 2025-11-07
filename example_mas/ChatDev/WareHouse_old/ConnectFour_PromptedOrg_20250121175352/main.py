'''
Main function to initialize the game and start the game loop.
'''
from game import Game
from player import Player
def main():
    print("Welcome to Connect Four!")
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")
    game = Game(player1, player2)
    game.play()
if __name__ == "__main__":
    main()