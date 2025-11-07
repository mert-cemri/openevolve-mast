'''
This module contains the CLI class which handles the command-line interface for the thesaurus tool.
'''
class CLI:
    def __init__(self, thesaurus):
        '''
        Initializes the CLI with a thesaurus instance.
        :param thesaurus: An instance of the Thesaurus class.
        '''
        self.thesaurus = thesaurus
    def run(self):
        '''
        Starts the CLI loop to accept user input and display results.
        '''
        print("Welcome to the CLI Thesaurus Lookup Tool!")
        while True:
            word = input("Enter a word (or 'exit' to quit): ").strip()
            if word.lower() == 'exit':
                print("Goodbye!")
                break
            synonyms = self.thesaurus.get_synonyms(word)
            antonyms = self.thesaurus.get_antonyms(word)
            print(f"Synonyms for '{word}': {', '.join(synonyms) if synonyms else 'None'}")
            print(f"Antonyms for '{word}': {', '.join(antonyms) if antonyms else 'None'}")