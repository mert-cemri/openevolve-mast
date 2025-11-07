'''
Main application file for the CLI spell checker.
'''
import sys
import os
import re
class SpellCheckerCLI:
    def __init__(self):
        self.dictionary = set()
        self.load_dictionary()
    def load_dictionary(self):
        '''Loads words from a local dictionary file into a set for quick lookup.'''
        try:
            with open('dictionary.txt', 'r') as file:
                for line in file:
                    self.dictionary.add(line.strip().lower())
        except FileNotFoundError:
            print("Error: Dictionary file not found.")
            sys.exit(1)
    def check_spelling(self, text):
        '''Checks the input text for misspellings and prints them.'''
        # Use regex to split text into words, ignoring punctuation
        words = re.findall(r'\b\w+\b', text.lower())
        misspelled_words = [word for word in words if word not in self.dictionary]
        if misspelled_words:
            print("Misspelled words:", ", ".join(misspelled_words))
        else:
            print("No misspellings found.")
    def run(self):
        '''Runs the CLI spell checker.'''
        if len(sys.argv) < 3:
            print("Usage: python main.py --file <text_file> or --string <string>")
            sys.exit(1)
        input_type = sys.argv[1]
        input_arg = sys.argv[2]
        if input_type == '--file':
            if os.path.isfile(input_arg):
                with open(input_arg, 'r') as file:
                    content = file.read()
                    self.check_spelling(content)
            else:
                print("Error: File not found.")
                sys.exit(1)
        elif input_type == '--string':
            self.check_spelling(input_arg)
        else:
            print("Error: Invalid input type. Use --file or --string.")
            sys.exit(1)
if __name__ == "__main__":
    spell_checker = SpellCheckerCLI()
    spell_checker.run()