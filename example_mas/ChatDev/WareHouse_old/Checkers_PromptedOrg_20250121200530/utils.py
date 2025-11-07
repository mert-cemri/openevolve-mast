'''
Utility functions for the Checkers game.
'''
def parse_move(move):
    # Convert move notation (e.g., "A3-B4") into board coordinates
    start, end = move.split('-')
    start_row, start_col = ord(start[0].upper()) - ord('A'), int(start[1]) - 1
    end_row, end_col = ord(end[0].upper()) - ord('A'), int(end[1]) - 1
    return (start_row, start_col), (end_row, end_col)