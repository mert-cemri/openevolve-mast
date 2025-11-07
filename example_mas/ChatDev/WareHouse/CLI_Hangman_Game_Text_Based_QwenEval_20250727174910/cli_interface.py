'''
Module to handle user input and display the game state for the CLI version.
This module contains the CLIInterface class which manages the interaction
between the user and the game through the command line.
'''
from hangman_game import HangmanGame
class CLIInterface:
    def __init__(self, game):
        '''
        Initializes the CLI interface with the given Hangman game instance.
        '''
        self.game = game
    def run(self):
        '''
        Runs the Hangman game in the command line interface.
        '''
        print("Welcome to Hangman!")
        while not self.game.is_game_over():
            print(f"Word: {self.game.get_display_word()}")
            print(f"Incorrect guesses: {self.game.incorrect_guesses}/{self.game.max_incorrect_guesses}")
            guess = input("Guess a letter: ").lower()
            if len(guess) != 1 or not guess.isalpha():
                print("Please enter a single letter.")
                continue
            result = self.game.guess_letter(guess)
            print(result)
        if self.game.is_game_won():
            print(f"Congratulations! You guessed the word: {self.game.word}")
        else:
            print(f"Game over! You failed to guess the word: {self.game.word}")