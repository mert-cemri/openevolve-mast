'''
Game logic for the Spelling Bee puzzle game.
'''
import random
from utils import load_dictionary
class SpellingBeeGame:
    def __init__(self):
        self.central_letter = ''
        self.surrounding_letters = []
        self.valid_words = set()
        self.score = 0
        self.load_game()
    def load_game(self):
        self.valid_words = load_dictionary()
        self.generate_letters()
    def generate_letters(self):
        letters = random.sample('abcdefghijklmnopqrstuvwxyz', 7)
        self.central_letter = letters[0]
        self.surrounding_letters = letters[1:]  # Ensure the central letter is not repeated
        if self.central_letter in self.surrounding_letters:
            self.surrounding_letters.remove(self.central_letter)
        self.surrounding_letters.append(self.central_letter)  # Include the central letter in the surrounding letters
    def is_valid_word(self, word):
        if len(word) < 4 or self.central_letter not in word:
            return False
        for letter in word:
            if letter not in self.surrounding_letters:
                return False
        return word in self.valid_words
    def calculate_score(self, word):
        if self.is_valid_word(word):
            self.score += len(word)
            return True
        return False