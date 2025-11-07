'''
This is the main module to run the match-3 puzzle game.
'''
from game import Game
def main():
    game = Game(8, 8)  # Initialize an 8x8 board
    game.board.print_board()
    while True:
        print("\nEnter the positions to swap (row1 col1 row2 col2) or 'q' to quit:")
        user_input = input()
        if user_input.lower() == 'q':
            break
        try:
            r1, c1, r2, c2 = map(int, user_input.split())
            if game.make_move((r1, c1), (r2, c2)):
                print("\nMove successful!")
                game.board.print_board()
                game.print_score()
            else:
                print("\nInvalid move. Try again.")
        except ValueError:
            print("\nInvalid input. Please enter four integers separated by spaces.")
if __name__ == "__main__":
    main()