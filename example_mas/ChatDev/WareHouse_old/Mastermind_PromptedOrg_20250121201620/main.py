'''
This is the main entry point for the Mastermind game application. It initializes the game and manages the game loop.
'''
from game import Game
def main():
    # Initialize the game with a sequence length of 4 and a maximum of 10 tries
    game = Game(sequence_length=4, max_tries=10)
    # Start the game loop
    game.start()
if __name__ == "__main__":
    main()