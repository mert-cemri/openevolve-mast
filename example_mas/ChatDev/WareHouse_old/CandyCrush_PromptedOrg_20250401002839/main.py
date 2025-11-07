'''
Main executable file for Candy Crush-like match-3 puzzle game with move-based constraints.
'''
from game import CandyCrushGame
def get_user_input(rows, cols):
    try:
        pos1 = tuple(map(int, input("Enter first candy position (row col): ").split()))
        pos2 = tuple(map(int, input("Enter second candy position (row col): ").split()))
        for r, c in [pos1, pos2]:
            if not (0 <= r < rows and 0 <= c < cols):
                print("Positions out of bounds. Please enter valid positions.")
                return None, None
        return pos1, pos2
    except ValueError:
        print("Invalid input. Please enter row and column numbers separated by a space.")
        return None, None
def main():
    game = CandyCrushGame(max_moves=30)
    while True:
        game.print_board()
        if game.moves >= game.max_moves:
            print("Reached maximum number of moves! Game Over.")
            break
        if not game.has_possible_moves():
            print("No more possible moves! Game Over.")
            break
        pos1, pos2 = get_user_input(game.rows, game.cols)
        if pos1 is None or pos2 is None:
            continue
        if not game.swap_candies(pos1, pos2):
            print("Invalid swap or no match created. Try again.")
    print(f"Final Score: {game.score}")
if __name__ == "__main__":
    main()