'''
DOCSTRING: Validates words based on the game's rules, ensuring they include the central letter and only use allowed letters.
'''
class WordValidator:
    def __init__(self, central_letter, letters, valid_words):
        self.central_letter = central_letter
        self.letters = set(letters)
        self.valid_words = set(valid_words)  # Add a set of valid words
    def is_valid(self, word):
        if self.central_letter not in word:
            return False
        if not all(letter in self.letters for letter in word):
            return False
        return word in self.valid_words  # Check if the word is in the valid words list