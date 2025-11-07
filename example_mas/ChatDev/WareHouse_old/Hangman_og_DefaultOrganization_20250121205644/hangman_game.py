'''
Contains the HangmanGame class which manages the game logic.
'''
import random
class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.secret_word = random.choice(self.word_list).upper()
        self.correct_guesses = set()
        self.incorrect_guesses = set()
        self.max_attempts = 6
    def guess_letter(self, letter):
        letter = letter.upper()
        if letter in self.correct_guesses or letter in self.incorrect_guesses:
            return  # Ignore if the letter has already been guessed
        if letter in self.secret_word:
            self.correct_guesses.add(letter)
        else:
            self.incorrect_guesses.add(letter)
    def is_game_over(self):
        return self.is_winner() or len(self.incorrect_guesses) >= self.max_attempts
    def is_winner(self):
        return all(letter in self.correct_guesses for letter in self.secret_word)
    def get_display_word(self):
        return ' '.join(letter if letter in self.correct_guesses else '_' for letter in self.secret_word)
    def get_incorrect_guesses(self):
        return ', '.join(self.incorrect_guesses)