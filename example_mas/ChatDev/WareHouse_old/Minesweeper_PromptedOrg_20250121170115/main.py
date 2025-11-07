'''
This is the main file for the Minesweeper game. It initializes the game and handles user input.
'''
from minesweeper_game import MinesweeperGame
def main():
    print("Welcome to Minesweeper!")
    print("Uncover cells by entering the row and column numbers.")
    print("Avoid mines and uncover all non-mine cells to win.")
    print("Type 'q' to quit the game at any time.")
    game = MinesweeperGame()
    game.display_board()
    while True:
        user_input = input("Enter row and column (e.g., 0 0) or 'q' to quit: ")
        if user_input.lower() == 'q':
            print("Thanks for playing! Goodbye.")
            break
        try:
            row, col = map(int, user_input.split())
            if not (0 <= row < 9 and 0 <= col < 9):
                print("Invalid input. Please enter numbers between 0 and 8.")
                continue
        except ValueError:
            print("Invalid input. Please enter valid numbers or 'q' to quit.")
            continue
        if game.uncover_cell(row, col):
            print("Game Over! You hit a mine.")
            break
        game.display_board()
        if game.check_win():
            print("Congratulations! You have won the game.")
            break
if __name__ == "__main__":
    main()