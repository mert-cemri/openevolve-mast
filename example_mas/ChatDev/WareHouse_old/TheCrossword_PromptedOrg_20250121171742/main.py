'''
This is the main entry point for the crossword puzzle application. It initializes the puzzle and starts the user interface.
'''
from crossword_puzzle import CrosswordPuzzle
from user_interface import UserInterface
def main():
    # Initialize the crossword puzzle
    puzzle = CrosswordPuzzle()
    # Initialize the user interface
    ui = UserInterface(puzzle)
    # Start the user interface
    ui.start()
if __name__ == "__main__":
    main()