'''
This file contains the Category class which represents a category of words.
'''
class Category:
    def __init__(self, words):
        self.words = set(words)
    def contains(self, guess):
        return set(guess) == self.words