'''
This module contains the SpellCheckerCLI class, which provides a command-line interface for checking spelling in text input or files.
'''
import os
import string
class SpellCheckerCLI:
    def __init__(self, dictionary_file):
        self.dictionary = set()
        self.load_dictionary(dictionary_file)
    def load_dictionary(self, filepath):
        '''Load words from a dictionary file into a set for quick lookup.'''
        if not os.path.exists(filepath):
            print(f"Error: Dictionary file '{filepath}' not found.")
            return
        with open(filepath, 'r') as file:
            for line in file:
                self.dictionary.add(line.strip().lower())
    def check_spelling(self, text):
        '''Check the spelling of words in the input text and print misspellings.'''
        translator = str.maketrans('', '', string.punctuation)
        words = text.split()
        misspelled_words = [word for word in words if word.lower().translate(translator) not in self.dictionary]
        if misspelled_words:
            print("Misspelled words:", ', '.join(misspelled_words))
        else:
            print("No misspellings found.")
if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='CLI Spell Checker')
    parser.add_argument('input', help='Text or path to a text file to check')
    args = parser.parse_args()
    spell_checker = SpellCheckerCLI("dictionary.txt")
    if os.path.isfile(args.input):
        with open(args.input, 'r') as file:
            content = file.read()
            spell_checker.check_spelling(content)
    else:
        spell_checker.check_spelling(args.input)