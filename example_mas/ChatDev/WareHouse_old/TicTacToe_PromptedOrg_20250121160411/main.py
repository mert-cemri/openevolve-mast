'''
This is the main file to run the tic-tac-toe game. It handles user input and game loop.
'''
from game import Game
def main():
    game = Game()
    game_running = True
    while game_running:
        game.board.display()
        try:
            row = int(input(f"Player {game.current_player}, enter the row (1, 2, or 3): ")) - 1
            col = int(input(f"Player {game.current_player}, enter the column (1, 2, or 3): ")) - 1
            if row not in [0, 1, 2] or col not in [0, 1, 2]:
                print("Invalid input. Please enter numbers between 1 and 3.")
                continue
        except EOFError:
            print("No input received. Exiting the game.")
            game_running = False
            continue
        except ValueError:
            print("Invalid input. Please enter valid numbers.")
            continue
        if game.make_move(row, col):
            if game.check_winner():
                game.board.display()
                print(f"Player {game.current_player} wins!")
                game_running = False
            elif game.is_draw():
                game.board.display()
                print("The game is a draw!")
                game_running = False
            else:
                game.switch_player()
        else:
            print("Invalid move. Try again.")
if __name__ == "__main__":
    main()