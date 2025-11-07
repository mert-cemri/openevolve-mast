'''
Contains utility functions for the Checkers game.
'''
def parse_move(start_pos, end_pos):
    # Convert mouse positions to board coordinates
    start_col, start_row = start_pos[0] // 100, start_pos[1] // 100
    end_col, end_row = end_pos[0] // 100, end_pos[1] // 100
    return (start_row, start_col), (end_row, end_col)
def validate_move(move, board, player):
    start, end = move
    return board.is_valid_move(start, end, player)