'''
This is the main module that runs the tic-tac-toe game loop, allowing two players to take turns until the game ends.
'''
from game import Game
from player import Player
def display_board_cli(board):
    '''Display the board in the command-line interface.'''
    for row in [board[i:i+3] for i in range(0, 9, 3)]:
        print('|'.join(row))
        print('-' * 5)
def get_player_move():
    '''Get the player's move from the command-line interface.'''
    while True:
        try:
            position = int(input("Enter a position (1-9): ")) - 1
            if position in range(9):
                return position
            else:
                print("Invalid position. Please enter a number between 1 and 9.")
        except ValueError:
            print("Invalid input. Please enter a number.")
        except EOFError:
            print("No input available. Exiting game.")
            exit()
def main():
    '''Run the game loop in a command-line interface.'''
    game = Game()
    print("Welcome to Tic-Tac-Toe!")
    display_board_cli(game.board)
    while not game.winner and ' ' in game.board:
        print(f"Player {game.current_player}'s turn.")
        position = get_player_move()
        if game.make_move(position):
            display_board_cli(game.board)
            if game.winner:
                print(f"Player {game.winner} wins!")
            elif ' ' not in game.board:
                print("It's a draw!")
            else:
                game.switch_player()
        else:
            print("Position already taken. Try again.")
if __name__ == "__main__":
    main()