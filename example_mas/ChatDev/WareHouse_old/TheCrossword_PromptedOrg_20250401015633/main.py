'''
Main entry point for the crossword puzzle application.
'''
from crossword import CrosswordPuzzle
def main():
    puzzle = CrosswordPuzzle()
    print("Welcome to the Crossword Puzzle!")
    while True:
        puzzle.display_grid()
        puzzle.display_clues()
        clue_number = input("Enter clue number (or 'exit' to quit): ")
        if clue_number.lower() == 'exit':
            print("Exiting the crossword puzzle. Goodbye!")
            break
        if not clue_number.isdigit():
            print("Invalid clue number. Please enter a valid number.")
            continue
        clue_number = int(clue_number)
        direction = input("Enter direction ('across' or 'down'): ").lower()
        if direction not in ['across', 'down']:
            print("Invalid direction. Please enter 'across' or 'down'.")
            continue
        word = input("Enter your word: ")
        puzzle.enter_word(clue_number, direction, word)
        if puzzle.check_completion():
            puzzle.display_grid()
            print("Congratulations! You have completed the crossword puzzle!")
            break
if __name__ == "__main__":
    main()