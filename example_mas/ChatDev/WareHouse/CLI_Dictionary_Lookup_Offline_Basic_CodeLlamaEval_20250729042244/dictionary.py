#!/usr/bin/env python3
import os
class Dictionary:
    def __init__(self):
        self.dictionary_file = os.path.join(os.path.dirname(__file__), 'dictionary.txt')
        self.dictionary = self.load_dictionary()
    def load_dictionary(self):
        with open(self.dictionary_file, 'r') as f:
            return {line.split(':')[0]: line.split(':')[1] for line in f.readlines()}
    def lookup(self, word):
        return self.dictionary.get(word)