'''
This module defines the Category class, which represents a category of words in the puzzle.
'''
class Category:
    def __init__(self, name, words):
        self.name = name
        self.words = words
    def is_match(self, guess):
        return set(guess) == set(word.lower() for word in self.words)