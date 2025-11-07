'''
This is the main file for the crossword puzzle application. It initializes the puzzle and handles user interaction.
'''
from crossword_puzzle import CrosswordPuzzle, Clue
def main():
    # Define the grid size and clues with starting positions
    grid_size = 5
    clues = [
        Clue(1, 'across', 'First letter of the alphabet', 'A', 0, 0),
        Clue(2, 'down', 'Opposite of yes', 'NO', 0, 1),
        Clue(3, 'across', 'Not old', 'NEW', 1, 0),
        Clue(4, 'down', 'A color', 'RED', 0, 2)
    ]
    # Initialize the crossword puzzle
    crossword = CrosswordPuzzle(grid_size, clues)
    # Display the initial grid
    crossword.display_grid()
    # Example user interaction
    while not crossword.check_completion():
        try:
            clue_number = int(input("Enter clue number: "))
        except ValueError:
            print("Invalid input. Please enter a valid clue number.")
            continue
        direction = input("Enter direction (across/down): ").strip().lower()
        word = input("Enter word: ").strip().upper()
        if crossword.enter_word(clue_number, direction, word):
            print("Word entered successfully!")
        crossword.display_grid()
    print("Congratulations! You've completed the crossword puzzle.")
if __name__ == "__main__":
    main()