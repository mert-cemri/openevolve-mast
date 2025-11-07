'''
Main module to initialize and run the NYT Strands puzzle game.
'''
from game import Game
def main():
    # Initialize the game
    game = Game()
    # Start the game loop
    game.start()
if __name__ == "__main__":
    main()