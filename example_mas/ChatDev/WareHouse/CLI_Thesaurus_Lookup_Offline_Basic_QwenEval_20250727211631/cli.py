'''
Module to handle user interaction for the CLI Thesaurus Lookup Tool.
This module defines the CLI class which manages user input and displays results.
'''
class CLI:
    def __init__(self, thesaurus):
        self.thesaurus = thesaurus
    def run(self):
        print("Welcome to the CLI Thesaurus Lookup Tool!")
        while True:
            word = self.get_user_input()
            if word.lower() == 'exit':
                print("Goodbye!")
                break
            synonyms = self.thesaurus.get_synonyms(word)
            antonyms = self.thesaurus.get_antonyms(word)
            self.display_results(word, synonyms, antonyms)
    def get_user_input(self):
        return input("Enter a word to look up (or 'exit' to quit): ")
    def display_results(self, word, synonyms, antonyms):
        print(f"Word: {word}")
        if synonyms:
            print(f"Synonyms: {', '.join(synonyms)}")
        else:
            print("No synonyms found.")
        if antonyms:
            print(f"Antonyms: {', '.join(antonyms)}")
        else:
            print("No antonyms found.")
        print()