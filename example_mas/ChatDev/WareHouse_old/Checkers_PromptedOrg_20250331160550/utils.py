'''
This module contains utility functions for parsing moves and printing the board.
'''
def parse_move(move):
    # Convert move notation (e.g., "A3-B4") to board indices
    from_pos, to_pos = move.split('-')
    from_pos = (8 - int(from_pos[1]), ord(from_pos[0].upper()) - ord('A'))
    to_pos = (8 - int(to_pos[1]), ord(to_pos[0].upper()) - ord('A'))
    return from_pos, to_pos
def print_board(board):
    # Print the current state of the board
    for row in board.grid:
        print(' '.join(['.' if piece is None else piece.color for piece in row]))