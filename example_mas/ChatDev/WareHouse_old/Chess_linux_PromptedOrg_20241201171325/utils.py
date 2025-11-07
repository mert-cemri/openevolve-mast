'''
Utility functions for the chess game.
'''
def parse_move(move):
    # Convert chess notation to board coordinates
    # Example: 'e2e4' -> ((6, 4), (4, 4))
    start_col, start_row, end_col, end_row = move
    start_pos = (8 - int(start_row), ord(start_col) - ord('a'))
    end_pos = (8 - int(end_row), ord(end_col) - ord('a'))
    return start_pos, end_pos
def is_checkmate(board, color):
    # Placeholder for checkmate logic
    return False