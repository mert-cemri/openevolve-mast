'''
This is the main application file for the crossword puzzle. It handles user interaction and manages the crossword puzzle instance.
'''
from crossword_puzzle import CrosswordPuzzle, Clue
def main():
    # Example clues for a 5x5 crossword puzzle
    clues = [
        Clue(1, 'across', (0, 0), 'hello'),
        Clue(2, 'down', (0, 0), 'house'),
        Clue(3, 'across', (1, 0), 'apple'),
        Clue(4, 'down', (0, 2), 'loop'),
    ]
    crossword = CrosswordPuzzle(5, clues)
    print("Welcome to the Crossword Puzzle!")
    crossword.display_clues()
    while not crossword.is_complete():
        crossword.display_grid()
        print("Enter your word:")
        try:
            clue_number = int(input("Clue number: "))
        except ValueError:
            print("Invalid input. Please enter a valid clue number.")
            continue
        direction = input("Direction (across/down): ").strip().lower()
        word = input("Word: ").strip().lower()
        if crossword.add_word(clue_number, direction, word):
            print("Word added successfully!")
        else:
            print("Invalid word. Please try again.")
    print("Congratulations! You've completed the crossword puzzle.")
if __name__ == "__main__":
    main()