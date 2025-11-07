'''
Utils module for utility functions used in the Gomoku game.
'''
def is_valid_move(board, row, col):
    return board.is_within_bounds(row, col) and board.grid[row][col] == "."
def get_input(board_size, input_func=None):
    if input_func is None:
        input_func = input
    while True:
        try:
            row, col = map(int, input_func("Enter row and column (e.g., 7 7): ").split())
            if 0 <= row < board_size and 0 <= col < board_size:
                return row, col
            else:
                print(f"Invalid input. Please enter numbers between 0 and {board_size - 1}.")
        except ValueError:
            print("Invalid input. Please enter two numbers separated by a space.")