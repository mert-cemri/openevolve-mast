'''
Main entry point for the Hangman game CLI version.
This script initializes the game by selecting a random word,
creating a HangmanGame instance, and running the CLIInterface.
'''
from word_selector import WordSelector
from hangman_game import HangmanGame
from cli_interface import CLIInterface
def main():
    word_selector = WordSelector()
    word = word_selector.select_word()
    game = HangmanGame(word)
    interface = CLIInterface(game)
    interface.run()
if __name__ == "__main__":
    main()