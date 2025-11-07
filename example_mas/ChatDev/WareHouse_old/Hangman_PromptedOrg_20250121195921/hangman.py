'''
This module contains the HangmanGame class which manages the state and logic of the Hangman game.
'''
import random
class HangmanGame:
    def __init__(self, word_list, max_attempts=6):
        '''
        Initialize the Hangman game with a list of words and maximum attempts.
        '''
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.word_to_guess = self.select_random_word()
        self.attempts_left = max_attempts
        self.correct_guesses = set()
        self.incorrect_guesses = set()
    def select_random_word(self):
        '''
        Select a random word from the word list.
        '''
        return random.choice(self.word_list)
    def guess_letter(self, letter):
        '''
        Process a guessed letter and update the game state.
        '''
        if letter in self.word_to_guess:
            self.correct_guesses.add(letter)
        else:
            self.incorrect_guesses.add(letter)
            self.attempts_left -= 1
    def display_current_state(self):
        '''
        Display the current state of the word with placeholders.
        '''
        display_word = ''.join(
            [letter if letter in self.correct_guesses else '_' for letter in self.word_to_guess]
        )
        print(f"Word: {display_word}")
        print(f"Incorrect guesses: {', '.join(self.incorrect_guesses)}")
        print(f"Attempts left: {self.attempts_left}")
    def is_game_over(self):
        '''
        Check if the game is over (win or lose).
        '''
        return self.attempts_left <= 0 or self.is_word_guessed()
    def is_word_guessed(self):
        '''
        Check if the word has been completely guessed.
        '''
        return all(letter in self.correct_guesses for letter in self.word_to_guess)