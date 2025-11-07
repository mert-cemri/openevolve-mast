'''
This module is the entry point for the crossword puzzle application.
'''
from crossword_puzzle import Clue, CrosswordPuzzle
def main():
    clues = [
        Clue(1, 'across', 'HELLO', (0, 0)),
        Clue(2, 'down', 'WORLD', (0, 0))
    ]
    crossword = CrosswordPuzzle(5, clues)
    print("Welcome to the Crossword Puzzle!")
    crossword.display_grid()
    while not crossword.check_completion():
        try:
            clue_number = int(input("Enter clue number: "))
            direction = input("Enter direction (across/down): ").strip().lower()
            word = input("Enter word: ").strip().upper()
            if crossword.enter_word(clue_number, direction, word):
                print("Word entered successfully!")
            else:
                print("Failed to enter word. Please try again.")
            crossword.display_grid()
        except ValueError:
            print("Invalid input. Please enter the correct format.")
    print("Congratulations! You have completed the crossword puzzle.")
if __name__ == "__main__":
    main()