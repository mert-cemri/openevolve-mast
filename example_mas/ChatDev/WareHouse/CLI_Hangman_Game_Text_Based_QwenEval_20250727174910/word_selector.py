'''
Module to select a random word from a predefined list.
This module contains the WordSelector class which is responsible
for selecting a random word from a list of words.
'''
import random
class WordSelector:
    def __init__(self):
        self.words = self.load_words_from_file("words.txt")
        if not self.words:
            raise ValueError("No valid words found in the file.")
    def load_words_from_file(self, filename):
        '''
        Loads words from a file and returns them as a list.
        '''
        try:
            with open(filename, 'r') as file:
                words = [line.strip().lower() for line in file if line.strip()]
            if not words:
                print(f"Warning: The file {filename} contains no valid words.")
            return words
        except FileNotFoundError:
            print(f"Error: The file {filename} was not found.")
            return []
        except Exception as e:
            print(f"An error occurred while reading the file {filename}: {e}")
            return []
    def select_word(self):
        '''
        Selects and returns a random word from the predefined list.
        '''
        return random.choice(self.words)