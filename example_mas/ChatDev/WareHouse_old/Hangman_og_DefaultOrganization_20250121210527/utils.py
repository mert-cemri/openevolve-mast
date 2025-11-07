'''
Utility functions for the Hangman game.
'''
def load_words(filename):
    with open(filename, 'r') as file:
        return [line.strip() for line in file if line.strip()]