'''
wordle_game.py
This module contains the WordleGame class, which handles the game logic for the Wordle game.
'''
import random
class WordleGame:
    def __init__(self, word_list):
        '''
        Initializes the WordleGame with a list of possible words.
        :param word_list: List of 5-letter words to choose from.
        '''
        self.word_list = word_list
        self.daily_word = random.choice(self.word_list)
        self.max_attempts = 6
    def check_guess(self, guess):
        '''
        Checks the player's guess against the daily word and returns feedback.
        :param guess: The player's guessed word.
        :return: A list of feedback for each letter in the guess.
        '''
        feedback = ['grey'] * len(guess)
        daily_word_chars = list(self.daily_word)
        # First pass: Check for correct letters in the correct position
        for i in range(len(guess)):
            if guess[i] == self.daily_word[i]:
                feedback[i] = 'green'
                daily_word_chars[i] = None  # Mark this character as used
        # Second pass: Check for correct letters in the wrong position
        for i in range(len(guess)):
            if feedback[i] == 'grey' and guess[i] in daily_word_chars:
                feedback[i] = 'yellow'
                daily_word_chars[daily_word_chars.index(guess[i])] = None  # Mark this character as used
        return feedback
    def is_valid_word(self, word):
        '''
        Validates if the word is a valid 5-letter word from the word list.
        :param word: The word to validate.
        :return: True if valid, False otherwise.
        '''
        return word in self.word_list
    def get_daily_word(self):
        '''
        Returns the daily word for testing purposes.
        :return: The daily word.
        '''
        return self.daily_word