'''
Main executable file for running the Connect Four game.
'''
from connect_four import ConnectFourGame
def main():
    '''Main function to run the Connect Four game.'''
    print("Welcome to Connect Four!")
    game = ConnectFourGame()
    game.display_board()
    while True:
        try:
            column_input = input(f"Player {game.current_player}, choose a column (0-{game.COLUMNS - 1}): ")
            if not column_input.isdigit():
                print("Invalid input. Please enter a numeric column number.")
                continue
            column = int(column_input)
            if not game.is_valid_move(column):
                print("Invalid move. Column is either full or out of bounds. Try again.")
                continue
            row, col = game.make_move(column)
            game.display_board()
            if game.check_winner(row, col):
                print(f"Congratulations! Player {game.current_player} wins!")
                break
            if game.is_board_full():
                print("The game is a draw!")
                break
            game.switch_player()
        except ValueError as e:
            print(f"Error: {e}. Please try again.")
        except KeyboardInterrupt:
            print("\nGame interrupted. Exiting...")
            break
if __name__ == "__main__":
    main()