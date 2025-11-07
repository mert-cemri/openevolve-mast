'''
Main file to run the Tic-Tac-Toe game with a user-friendly interface.
'''
from tic_tac_toe import TicTacToe
def main():
    game = TicTacToe()
    print("Welcome to Tic-Tac-Toe!")
    game.display_board()
    while True:
        print(f"Player {game.current_player}'s turn.")
        try:
            row = int(input("Enter row (1-3): ")) - 1
            col = int(input("Enter column (1-3): ")) - 1
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        if not (0 <= row <= 2 and 0 <= col <= 2):
            print("Invalid position. Please enter numbers between 1 and 3.")
            continue
        if not game.make_move(row, col):
            print("Position already taken. Try again.")
            continue
        game.display_board()
        if game.check_winner():
            print(f"Congratulations! Player {game.current_player} wins!")
            break
        if game.is_board_full():
            print("It's a draw!")
            break
        game.switch_player()
    print("Thanks for playing Tic-Tac-Toe!")
if __name__ == "__main__":
    main()