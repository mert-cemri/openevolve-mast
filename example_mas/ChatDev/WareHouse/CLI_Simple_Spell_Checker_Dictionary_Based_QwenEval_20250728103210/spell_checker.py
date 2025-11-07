'''
SpellChecker class to check words against a dictionary.
'''
import re
class SpellChecker:
    def __init__(self, dictionary):
        # Convert dictionary to a set for faster lookup
        self.dictionary = set(dictionary)
    def check_word(self, word):
        # Check if the word is in the dictionary (case-insensitive)
        return word.lower() in self.dictionary
    def check_text(self, text):
        # Remove punctuation using regular expressions and split text into words
        words = re.findall(r'\b\w+\b', text)
        # Find misspelled words
        misspelled_words = [word for word in words if not self.check_word(word)]
        return misspelled_words