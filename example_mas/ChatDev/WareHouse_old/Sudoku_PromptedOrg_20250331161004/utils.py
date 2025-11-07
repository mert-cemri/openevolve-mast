'''
Contains utility functions for the Sudoku game, such as printing the board.
'''
def print_board(board):
    for row in board:
        print(" ".join(str(num) if num != 0 else '.' for num in row))