'''
Main execution file for the Strands puzzle game.
'''
from strand_puzzle import StrandPuzzle
def main():
    # Initialize the puzzle
    puzzle = StrandPuzzle()
    # Load strands into the puzzle
    puzzle.load_strands()
    # Main game loop
    while not puzzle.check_completion():
        print("Current strands:", puzzle.strands)
        user_input = input("Enter strands to combine (comma-separated): ")
        strands_to_combine = user_input.split(',')
        if puzzle.combine_strands(strands_to_combine):
            print("Valid combination!")
        else:
            print("Invalid combination. Try again.")
    print("Congratulations! You've completed the puzzle.")
if __name__ == "__main__":
    main()