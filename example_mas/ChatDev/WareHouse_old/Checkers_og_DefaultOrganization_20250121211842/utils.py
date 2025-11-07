'''
Utility functions for handling moves and board positions.
'''
def parse_move(move_notation):
    # Mapping from letters to column indices
    letter_to_col = {'a': 0, 'b': 1, 'c': 2, 'd': 3, 'e': 4, 'f': 5, 'g': 6, 'h': 7}
    from_pos, to_pos = move_notation.split('-')
    from_row, from_col = int(from_pos[1]) - 1, letter_to_col[from_pos[0].lower()]
    to_row, to_col = int(to_pos[1]) - 1, letter_to_col[to_pos[0].lower()]
    return (from_row, from_col), (to_row, to_col)
def is_valid_move(board, from_pos, to_pos, current_player_color):
    piece = board.grid[from_pos[0]][from_pos[1]]
    if not piece or piece.color != current_player_color:
        return False
    if board.grid[to_pos[0]][to_pos[1]] is not None:
        return False
    row_diff = to_pos[0] - from_pos[0]
    col_diff = to_pos[1] - from_pos[1]
    # Check for regular piece movement
    if not piece.is_king:
        if piece.color == 'red' and row_diff != -1:
            return False
        if piece.color == 'black' and row_diff != 1:
            return False
        if abs(col_diff) != 1:
            return False
    # Check for king movement
    if piece.is_king:
        if abs(row_diff) != 1 or abs(col_diff) != 1:
            return False
    # Check for capture move
    if abs(row_diff) == 2 and abs(col_diff) == 2:
        mid_row = (from_pos[0] + to_pos[0]) // 2
        mid_col = (from_pos[1] + to_pos[1]) // 2
        mid_piece = board.grid[mid_row][mid_col]
        if mid_piece is None or mid_piece.color == piece.color:
            return False
    return True