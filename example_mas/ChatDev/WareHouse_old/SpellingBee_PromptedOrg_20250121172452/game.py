'''
Game logic for the Spelling Bee puzzle.
'''
from utils import load_dictionary
class SpellingBeeGame:
    def __init__(self, central_letter, surrounding_letters):
        self.central_letter = central_letter
        self.surrounding_letters = surrounding_letters
        self.found_words = set()
        self.dictionary = load_dictionary()  # Use the utility function to load the dictionary
    def is_valid_word(self, word):
        if len(word) < 4:
            return False
        if self.central_letter not in word:
            return False
        available_letters = set(self.surrounding_letters + [self.central_letter])
        for letter in word:
            if letter not in available_letters:
                return False
        return word in self.dictionary
    def calculate_score(self, word):
        length = len(word)
        if length == 4:
            return 1
        elif length == 5:
            return 2
        elif length == 6:
            return 3
        elif length == 7:
            return 5
        elif length >= 8:
            return 11
        return 0
    def add_word(self, word):
        self.found_words.add(word)