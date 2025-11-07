'''
Hangman game logic implementation.
'''
import random
class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guessed_letters = set()
        self.attempts_left = 6
    def select_random_word(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters.clear()
        self.attempts_left = 6
    def guess_letter(self, letter):
        if len(letter) != 1:
            return "Please enter a single letter."
        if letter in self.guessed_letters:
            return "You have already guessed that letter."
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1
        return None
    def is_game_over(self):
        return self.attempts_left <= 0 or self.get_display_word().replace(" ", "") == self.word
    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)