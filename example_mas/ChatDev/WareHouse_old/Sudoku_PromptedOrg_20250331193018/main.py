'''
Main executable file for Sudoku game. Handles user interaction and allows players to check for mistakes explicitly.
'''
from sudoku import Sudoku
from puzzle_generator import generate_puzzle
def main():
    puzzle = generate_puzzle()
    game = Sudoku(puzzle)
    print("Welcome to Sudoku!")
    while not game.is_completed():
        game.display()
        action = input("Enter 'c' to check mistakes or 'p' to play: ").lower()
        if action == 'c':
            mistakes = game.check_for_mistakes()
            if mistakes:
                print("Mistakes found at positions:")
                for row, col in mistakes:
                    print(f"Row {row + 1}, Column {col + 1}")
            else:
                print("No mistakes found. Keep going!")
            continue
        elif action == 'p':
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (1-9): "))
                if not game.is_cell_editable(row, col):
                    print("Cannot change pre-filled cells! Try again.")
                    continue
                if game.is_valid_move(row, col, num):
                    game.set_value(row, col, num)
                else:
                    print("Invalid move! Try again.")
            except (ValueError, IndexError):
                print("Invalid input! Please enter numbers between 1 and 9.")
        else:
            print("Invalid action! Please enter 'c' or 'p'.")
    print("Congratulations! You completed the puzzle!")
    game.display()
if __name__ == "__main__":
    main()