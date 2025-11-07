'''
This module contains the WordGrid class, which handles the 4x4 grid of words, including shuffling and displaying the grid.
'''
import random
class WordGrid:
    def __init__(self):
        self.words = []
    def shuffle(self):
        random.shuffle(self.words)
    def display(self):
        for i in range(0, len(self.words), 4):
            print(self.words[i:i+4])
    def remove_words(self, words):
        self.words = [word for word in self.words if word not in words]