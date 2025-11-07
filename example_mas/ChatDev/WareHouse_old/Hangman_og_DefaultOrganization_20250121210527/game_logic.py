'''
Game logic for the Hangman game.
'''
import random
class HangmanGame:
    def __init__(self, word_list):
        self.word_list = word_list
        self.word = ""
        self.guessed_letters = set()
        self.attempts_left = 6
        self.won = False
    def select_random_word(self):
        self.word = random.choice(self.word_list)
        self.guessed_letters.clear()
        self.attempts_left = 6
        self.won = False
    def make_guess(self, letter):
        if letter in self.guessed_letters:
            return
        self.guessed_letters.add(letter)
        if letter not in self.word:
            self.attempts_left -= 1
        self.won = all(letter in self.guessed_letters for letter in self.word)
    def is_game_over(self):
        return self.won or self.attempts_left <= 0
    def get_display_word(self):
        return " ".join(letter if letter in self.guessed_letters else "_" for letter in self.word)