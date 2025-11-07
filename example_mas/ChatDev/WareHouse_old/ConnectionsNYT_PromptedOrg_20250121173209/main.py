'''
This is the main entry point for the puzzle game. It handles user interaction and game loop.
'''
from puzzle import Puzzle
def main():
    # Initialize the puzzle
    puzzle = Puzzle()
    # Game loop
    while not puzzle.is_solved() and puzzle.remaining_tries > 0:
        print("\nCurrent Words: ", puzzle.get_shuffled_words())
        guess = input("Enter four words separated by commas: ").strip().split(',')
        guess = [word.strip() for word in guess]
        if len(guess) != 4:
            print("Please enter exactly four words.")
            continue
        # Check if all guessed words are in the shuffled words list
        if not all(word.lower() in [w.lower() for w in puzzle.get_shuffled_words()] for word in guess):
            print("Please enter words from the current list.")
            continue
        if puzzle.check_guess(guess):
            print("Correct group!")
        else:
            print("Incorrect group.")
        print(f"Remaining tries: {puzzle.remaining_tries}")
    if puzzle.is_solved():
        print("Congratulations! You've solved the puzzle.")
    else:
        print("Game over. Better luck next time!")
if __name__ == "__main__":
    main()