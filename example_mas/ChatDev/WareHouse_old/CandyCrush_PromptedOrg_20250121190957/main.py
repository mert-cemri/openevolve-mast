'''
This is the main entry point for the match-3 puzzle game. It initializes the game and handles user input.
'''
from board import Board
from game import Game
def print_board(board):
    for row in board.grid:
        print(' '.join(candy.type[0].upper() for candy in row))
    print(f"Score: {board.score}")
def main():
    # Initialize the game
    board = Board()
    game = Game(board)
    while True:
        # Display the current board state
        print_board(board)
        # Get user input for the move
        try:
            x1, y1 = map(int, input("Enter the coordinates of the first candy to swap (row col): ").split())
            x2, y2 = map(int, input("Enter the coordinates of the second candy to swap (row col): ").split())
        except ValueError:
            print("Invalid input. Please enter numbers only.")
            continue
        # Check if the user wants to quit
        if (x1, y1, x2, y2) == (-1, -1, -1, -1):
            print("Exiting the game.")
            break
        # Validate and make the move
        if game.is_valid_move(x1, y1, x2, y2):
            game.make_move(x1, y1, x2, y2)
        else:
            print("Invalid move! Please try again.")
if __name__ == "__main__":
    main()