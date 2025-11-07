'''
This is the main file for the tic-tac-toe game. It initializes the game and handles the game loop.
'''
from game import Game  # Import the Game class from game.py
def main():
    game = Game()
    game.display_board()
    while True:
        try:
            move = input(f"Player {game.current_player}, enter your move as 'row column' (e.g., '1 2'): ")
            row, col = map(int, move.split())
            if row not in range(3) or col not in range(3):
                print("Invalid input. Please enter numbers between 0 and 2 for both row and column.")
                continue
            if game.make_move(row, col):
                game.display_board()
                if game.check_winner():
                    print(f"Player {game.current_player} wins!")
                    break
                elif game.is_draw():
                    print("The game is a draw!")
                    break
                game.switch_player()
            else:
                print("Invalid move. The cell is already occupied. Try again.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")
        except EOFError:
            print("Input ended unexpectedly. Exiting the game.")
            break
if __name__ == "__main__":
    main()