'''
This module contains the UserInterface class, which handles user input and output for the crossword puzzle application.
'''
class UserInterface:
    def __init__(self, puzzle):
        self.puzzle = puzzle
    def start(self):
        # Start the user interface loop
        while not self.puzzle.is_completed():
            self.display_grid()
            try:
                clue_number = int(input("Enter clue number: "))
            except ValueError:
                print("Invalid input. Please enter a valid clue number.")
                continue
            direction = input("Enter direction (across/down): ").strip().lower()
            if direction not in ['across', 'down']:
                print("Invalid direction. Please enter 'across' or 'down'.")
                continue
            word = input("Enter word: ").strip().lower()
            if self.puzzle.enter_word(clue_number, direction, word):
                print("Word placed successfully!")
            else:
                print("Invalid word or placement. Try again.")
        print("Congratulations! You have completed the puzzle.")
    def display_grid(self):
        # Display the current state of the grid
        for row in self.puzzle.grid.grid:
            print(' '.join(row))
        print()