'''
Main entry point for the NYT Strands puzzle game.
'''
from strands_puzzle import StrandsPuzzle, load_words
def main():
    # Load words for the puzzle
    theme_words, spangram = load_words()
    # Initialize the puzzle
    puzzle = StrandsPuzzle(theme_words, spangram)
    # Place words on the grid
    puzzle.place_words()
    # Main game loop
    while not puzzle.is_completed():
        # Display the grid
        puzzle.grid.display()
        # Get user input for a word
        word = input("Enter a word: ").strip().upper()
        # Check if the word is valid
        if puzzle.check_word(word):
            print(f"Word '{word}' found!")
            puzzle.highlight_word(word)
        else:
            print(f"Word '{word}' not found.")
        # Check for hints
        if puzzle.unlock_hint():
            print("Hint unlocked!")
    print("Congratulations! You have completed the puzzle.")
if __name__ == "__main__":
    main()