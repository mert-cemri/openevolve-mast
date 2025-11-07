'''
Main module to run the NYT Strands puzzle game.
'''
from puzzle import Puzzle
from user_interface import UserInterface
def main():
    # Initialize the puzzle with a set of word segments
    segments = ["con", "nect", "ion", "str", "and", "s"]
    # Load a comprehensive word list from a file or an API
    word_list = load_word_list()
    puzzle = Puzzle(segments, word_list)
    # Initialize the user interface
    ui = UserInterface(puzzle)
    # Start the game
    ui.start_game()
def load_word_list():
    # Example: Load words from a file or an API
    # Here we use a simple example list for demonstration
    return ["connection", "strand", "connections", "strands"]
if __name__ == "__main__":
    main()