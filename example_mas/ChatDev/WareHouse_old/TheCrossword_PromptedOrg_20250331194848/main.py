'''
This module provides an interactive interface for users to play the crossword puzzle game.
'''
from crossword import CrosswordPuzzle
def main():
    puzzle = CrosswordPuzzle()
    print("Welcome to the Crossword Puzzle!")
    while not puzzle.is_completed():
        puzzle.display_grid()
        puzzle.display_clues()
        try:
            clue_number = int(input("Enter clue number: "))
            direction = input("Enter direction (across/down): ").strip().lower()
            if direction not in ['across', 'down']:
                print("Invalid direction. Please enter 'across' or 'down'.")
                continue
            word = input("Enter your word: ").strip()
            puzzle.enter_word(clue_number, direction, word)
        except ValueError:
            print("Invalid input. Please enter numeric clue numbers.")
    puzzle.display_grid()
    print("Congratulations! You have completed the crossword puzzle!")
if __name__ == "__main__":
    main()