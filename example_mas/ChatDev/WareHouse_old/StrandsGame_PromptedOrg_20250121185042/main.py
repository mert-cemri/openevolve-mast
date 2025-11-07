'''
Main module for the Strands puzzle game. Initializes the game and manages user interaction.
'''
import sys
from strand_puzzle import StrandPuzzle
from utils import load_strands_from_file
def main():
    if len(sys.argv) != 3:
        print("Usage: python main.py <strands_file> <valid_words_file>")
        return
    strands_file_path = sys.argv[1]
    valid_words_file_path = sys.argv[2]
    strands = load_strands_from_file(strands_file_path)
    valid_words = load_strands_from_file(valid_words_file_path)
    puzzle = StrandPuzzle(strands, valid_words)
    print("Welcome to the Strands Puzzle!")
    print("Combine the strands to form meaningful words or phrases.")
    while not puzzle.is_completed():
        combination = input("Enter your combination: ")
        if puzzle.is_valid_combination(combination):
            print("Valid combination!")
        else:
            print("Invalid combination, try again.")
    print("Congratulations! You've completed the puzzle.")
if __name__ == "__main__":
    main()