'''
This file contains the main function that runs the Gomoku game.
'''
from gomoku import GomokuGame
def main():
    game = GomokuGame()
    print("Welcome to Gomoku!")
    game.display_board()
    while True:
        print(f"Player {'Black' if game.current_player == 'B' else 'White'}'s turn.")
        try:
            move = input("Enter your move (row col): ").split()
            if len(move) != 2:
                print("Invalid input. Please enter two integers separated by space.")
                continue
            x, y = map(int, move)
        except ValueError:
            print("Invalid input. Please enter integers.")
            continue
        if not game.make_move(x, y):
            continue
        game.display_board()
        if game.check_win(x, y, game.current_player):
            print(f"Congratulations! Player {'Black' if game.current_player == 'B' else 'White'} wins!")
            break
        elif game.is_board_full():
            print("The game is a draw!")
            break
        game.switch_player()
if __name__ == "__main__":
    main()