'''
This is the main file for the Strands puzzle application. It initializes the puzzle with strands and provides an interface for the user to interact with the puzzle.
'''
from strand_puzzle import StrandPuzzle
from utils import load_strands_from_file
def main():
    # Load strands from a file
    strands = load_strands_from_file('strands.txt')
    # Initialize the puzzle
    puzzle = StrandPuzzle(strands)
    print("Welcome to the Strands Puzzle!")
    print("Combine the strands to form meaningful words or phrases.")
    while not puzzle.is_complete():
        print("\nCurrent strands:")
        for i, strand in enumerate(puzzle.strands):
            print(f"{i}: {strand}")
        try:
            indices = input("Enter the indices of strands to combine (comma-separated): ")
            indices = [int(i) for i in indices.split(',')]
            if any(i < 0 or i >= len(puzzle.strands) for i in indices):
                raise ValueError("Indices out of range.")
            if puzzle.combine_strands(indices):
                print("Valid combination!")
            else:
                print("Invalid combination. Try again.")
        except ValueError as e:
            print(f"Invalid input: {e}. Please enter valid indices.")
    print("Congratulations! You have completed the puzzle.")
if __name__ == "__main__":
    main()