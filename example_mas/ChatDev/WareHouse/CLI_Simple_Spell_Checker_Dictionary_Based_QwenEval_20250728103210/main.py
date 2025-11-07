'''
Main file to run the spell checker application with CLI option.
'''
import sys
from spell_checker import SpellChecker
from dictionary_loader import DictionaryLoader
from cli_interface import CLIInterface
def main():
    # Load dictionary and initialize spell checker
    dictionary_loader = DictionaryLoader('dictionary.txt')
    dictionary = dictionary_loader.load_dictionary()
    spell_checker = SpellChecker(dictionary)
    # Run CLI interface
    cli = CLIInterface(spell_checker)
    cli.run_cli()
if __name__ == '__main__':
    main()