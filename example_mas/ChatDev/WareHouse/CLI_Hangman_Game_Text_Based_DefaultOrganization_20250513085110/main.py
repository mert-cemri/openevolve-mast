'''
This is the main entry point for the CLI Hangman game. It initializes the game and handles user input and output.
'''
from game import HangmanGame
def main():
    game = HangmanGame()
    game.start()
if __name__ == "__main__":
    main()