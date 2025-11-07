'''
This file contains the main function to run the Gomoku game.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    print("Welcome to Gomoku!")
    game.display_board()
    while True:
        print(f"Player {game.current_player}'s turn.")
        try:
            row, col = map(int, input("Enter row and column (separated by space): ").split())
        except ValueError:
            print("Invalid input. Please enter two integers separated by a space.")
            continue
        if not game.place_stone(row, col):
            continue
        game.display_board()
        if game.check_win(row, col):
            print(f"Congratulations! Player {game.current_player} wins!")
            break
        if game.is_full():
            print("The game is a draw! No more moves available.")
            break
        game.switch_player()
if __name__ == "__main__":
    main()