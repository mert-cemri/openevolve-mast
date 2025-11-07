'''
This file contains the Category class, which represents a category of words, storing the words that belong to it.
'''
class Category:
    def __init__(self, name, words):
        self.name = name
        self.words = set(words)
    def is_correct_group(self, guess):
        return set(guess) == self.words