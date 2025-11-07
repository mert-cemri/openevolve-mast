'''
This file contains the HangmanGame class, which encapsulates the logic for the Hangman game.
'''
import random
class HangmanGame:
    def __init__(self, word_list, max_attempts):
        self.word_list = word_list
        self.max_attempts = max_attempts
        self.selected_word = self.select_random_word()
        self.correct_guesses = set()
        self.incorrect_guesses = 0
        self.guessed_letters = set()
    def select_random_word(self):
        return random.choice(self.word_list)
    def guess_letter(self, letter):
        if letter in self.guessed_letters:
            return None  # Indicate no change in guess count
        self.guessed_letters.add(letter)
        if letter in self.selected_word:
            self.correct_guesses.add(letter)
            return True
        else:
            self.incorrect_guesses += 1
            return False
    def display_word(self):
        return ' '.join([letter if letter in self.correct_guesses else '_' for letter in self.selected_word])
    def is_game_over(self):
        return self.incorrect_guesses >= self.max_attempts or self.is_word_guessed()
    def is_word_guessed(self):
        return all(letter in self.correct_guesses for letter in self.selected_word)