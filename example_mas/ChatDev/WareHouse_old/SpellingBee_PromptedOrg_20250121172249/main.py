'''
DOCSTRING: Entry point for the Spelling Bee puzzle application. Initializes and starts the game loop.
'''
from spelling_bee_game import SpellingBeeGame
def main():
    central_letter = input("Enter the central letter: ").strip().lower()
    surrounding_letters = input("Enter six surrounding letters separated by spaces: ").strip().lower().split()
    if len(surrounding_letters) != 6:
        print("Error: You must enter exactly six surrounding letters.")
        return
    valid_words = load_valid_words()  # Load the valid words from a file or source
    game = SpellingBeeGame(central_letter, surrounding_letters, valid_words)
    game.start()
def load_valid_words():
    try:
        with open('valid_words.txt', 'r') as file:
            words = file.read().splitlines()
        return words
    except FileNotFoundError:
        print("Error: The valid words file is missing.")
        return []
if __name__ == "__main__":
    main()