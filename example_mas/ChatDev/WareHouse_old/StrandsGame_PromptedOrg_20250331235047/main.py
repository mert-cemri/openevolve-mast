'''
Main executable file for the Strands puzzle game.
'''
from strand_puzzle import StrandPuzzle
def main():
    print("🎲 Welcome to Strands Puzzle! 🎲\n")
    strands = ["py", "thon", "pro", "gram", "ming", "lan", "guage"]
    solutions = ["python", "programming", "language"]
    puzzle = StrandPuzzle(strands, solutions)
    while not puzzle.is_completed():
        puzzle.display_strands()
        user_input = input("\nEnter indices of strands to merge (comma-separated, e.g., 0,1): ")
        try:
            indices = [int(i.strip()) for i in user_input.split(",")]
            merged_strand, valid = puzzle.merge_strands(indices)
            if valid:
                print(f"✅ Correct! '{merged_strand}' is a valid merge.\n")
            else:
                print(f"❌ '{merged_strand}' is not a valid merge. Try again.\n")
        except (ValueError, IndexError) as e:
            print(f"⚠️ Invalid input: {e}. Please try again.\n")
    print("🎉 Congratulations! You have successfully completed the Strands Puzzle! 🎉")
if __name__ == "__main__":
    main()