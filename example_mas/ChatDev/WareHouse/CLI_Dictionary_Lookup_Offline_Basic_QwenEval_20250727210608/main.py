'''
Main file for the CLI dictionary lookup tool.
This file initializes the main application and handles user input.
'''
import sys
from dictionary import Dictionary
def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <word>")
        sys.exit(1)
    word = sys.argv[1].strip().lower()
    if not word:
        print("Error: The input word cannot be empty.")
        sys.exit(1)
    dictionary = Dictionary("dictionary.txt")
    definition = dictionary.get_definition(word)
    if definition:
        print(f"Definition of '{word}': {definition}")
    else:
        print(f"No definition found for '{word}'. Please check the spelling and try again.")
if __name__ == "__main__":
    main()