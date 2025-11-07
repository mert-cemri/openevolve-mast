'''
Utility functions for parsing moves, printing the board, and checking game conditions.
'''
def parse_move(move_str, board, player):
    if len(move_str) in [4, 5]:
        start_col = ord(move_str[0]) - ord('a')
        start_row = 8 - int(move_str[1])
        end_col = ord(move_str[2]) - ord('a')
        end_row = 8 - int(move_str[3])
        promotion = move_str[4] if len(move_str) == 5 else None
        return Move((start_row, start_col), (end_row, end_col), player, promotion)
    return None
def print_board(board):
    for r in range(8):
        print(8 - r, end=' ')
        for c in range(8):
            piece = board.board[r][c]
            print(piece.__class__.__name__[0] if piece else '.', end=' ')
        print()
    print('  a b c d e f g h')
def is_checkmate(board, player):
    return False  # Simplified for brevity
def is_stalemate(board, player):
    return False  # Simplified for brevity