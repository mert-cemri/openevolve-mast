'''
This module contains the main function which serves as the entry point of the application. It manages user input and the game loop.
'''
from minesweeper import MinesweeperGame
def main():
    game = MinesweeperGame()
    game.display_board()
    while True:
        try:
            user_input = input("Enter row and column to uncover (e.g., 0 1): ")
            row, col = map(int, user_input.split())
            game.uncover_cell(row, col)
            game.display_board()
            if game.check_win():
                print("Congratulations! You've won the game!")
                break
        except ValueError as e:
            print(e)
            break
        except Exception as e:
            print(f"Invalid input: {e}")
if __name__ == "__main__":
    main()