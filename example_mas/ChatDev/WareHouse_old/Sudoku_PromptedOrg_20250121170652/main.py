'''
This is the main module that runs the Sudoku application, allowing users to interact with the Sudoku game.
'''
from sudoku_game import SudokuGame
def main():
    game = SudokuGame()
    print("Welcome to Sudoku!")
    print("Enter your moves in the format: row col num (e.g., 0 0 5)")
    print("Type 'exit' to quit the game.")
    while True:
        user_input = input("Enter your move: ")
        if user_input.lower() == 'exit':
            break
        try:
            row, col, num = map(int, user_input.split())
            feedback = game.input_value(row, col, num)
            print(feedback)
        except ValueError:
            print("Invalid input format. Please enter row, column, and number separated by spaces.")
        if game.check_completion():
            print("Congratulations! The Sudoku puzzle is complete.")
            break
if __name__ == "__main__":
    main()