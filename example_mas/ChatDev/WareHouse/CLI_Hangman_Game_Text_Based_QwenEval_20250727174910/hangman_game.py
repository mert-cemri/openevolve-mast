'''
Module to handle the game logic for Hangman.
This module contains the HangmanGame class which manages the game state,
including guessed letters, incorrect guesses, and game status.
'''
class HangmanGame:
    def __init__(self, word):
        '''
        Initializes the Hangman game with the given word.
        '''
        self.word = word
        self.guessed_letters = set()
        self.incorrect_guesses = 0
        self.max_incorrect_guesses = 6
    def guess_letter(self, letter):
        '''
        Processes a guessed letter, updating the game state accordingly.
        Returns a message indicating whether the guess was correct or incorrect.
        '''
        if letter in self.guessed_letters:
            return "You already guessed that letter."
        self.guessed_letters.add(letter)
        if letter in self.word:
            return "Correct!"
        else:
            self.incorrect_guesses += 1
            return "Incorrect!"
    def get_display_word(self):
        '''
        Returns the current state of the word with guessed letters filled in.
        '''
        return ''.join([letter if letter in self.guessed_letters else '_' for letter in self.word])
    def is_game_over(self):
        '''
        Checks if the game is over, either by winning or losing.
        '''
        return self.incorrect_guesses >= self.max_incorrect_guesses or self.is_game_won()
    def is_game_won(self):
        '''
        Checks if the player has won the game by guessing all letters correctly.
        '''
        return all(letter in self.guessed_letters for letter in self.word)