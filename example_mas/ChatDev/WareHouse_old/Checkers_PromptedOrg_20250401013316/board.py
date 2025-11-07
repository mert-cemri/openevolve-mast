'''
Board class to manage the Checkers game state, moves, captures, kinging logic, and mandatory capture enforcement.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.board = [[None]*8 for _ in range(8)]
        for row in range(3):
            for col in range((row+1)%2, 8, 2):
                self.board[row][col] = Piece('B')
        for row in range(5,8):
            for col in range((row+1)%2, 8, 2):
                self.board[row][col] = Piece('W')
    def display(self):
        print("  a b c d e f g h")
        for i in range(7,-1,-1):
            row_str = f"{i+1} "
            for j in range(8):
                piece = self.board[i][j]
                row_str += (str(piece) if piece else '.') + ' '
            print(row_str)
        print()
    def get_piece(self, pos):
        row, col = pos
        return self.board[row][col]
    def remove_piece(self, pos):
        row, col = pos
        self.board[row][col] = None
    def move_piece(self, from_pos, to_pos):
        piece = self.get_piece(from_pos)
        self.board[to_pos[0]][to_pos[1]] = piece
        self.remove_piece(from_pos)
        if self.is_capture_move(from_pos, to_pos):
            mid_row = (from_pos[0] + to_pos[0]) // 2
            mid_col = (from_pos[1] + to_pos[1]) // 2
            self.remove_piece((mid_row, mid_col))
        self.king_piece_if_needed(piece, to_pos)
    def valid_move(self, from_pos, to_pos, player):
        piece = self.get_piece(from_pos)
        if not piece or piece.player != player or self.get_piece(to_pos):
            return False
        capture_available = self.has_capture_moves(player)
        is_capture_move = self.is_capture_move(from_pos, to_pos)
        if capture_available and not is_capture_move:
            return False  # Must perform capture if available
        row_diff = to_pos[0] - from_pos[0]
        col_diff = abs(to_pos[1] - from_pos[1])
        if piece.king:
            valid_direction = abs(row_diff) == 1 or abs(row_diff) == 2
        else:
            valid_direction = (row_diff == 1 if player == 'W' else row_diff == -1) or \
                              (row_diff == 2 if player == 'W' else row_diff == -2)
        if col_diff == 1 and abs(row_diff) == 1 and valid_direction and not capture_available:
            return True
        elif col_diff == 2 and abs(row_diff) == 2 and valid_direction:
            mid_row = (from_pos[0] + to_pos[0]) // 2
            mid_col = (from_pos[1] + to_pos[1]) // 2
            mid_piece = self.get_piece((mid_row, mid_col))
            return mid_piece and mid_piece.player != player
        return False
    def is_capture_move(self, from_pos, to_pos):
        return abs(from_pos[0] - to_pos[0]) == 2
    def king_piece_if_needed(self, piece, to_pos):
        if (piece.player == 'W' and to_pos[0] == 7) or (piece.player == 'B' and to_pos[0] == 0):
            piece.king = True
    def has_winner(self):
        w_pieces = b_pieces = 0
        for row in self.board:
            for piece in row:
                if piece:
                    if piece.player == 'W':
                        w_pieces += 1
                    else:
                        b_pieces += 1
        if w_pieces == 0:
            return 'B'
        elif b_pieces == 0:
            return 'W'
        return None
    def has_capture_moves(self, player):
        for row in range(8):
            for col in range(8):
                piece = self.get_piece((row, col))
                if piece and piece.player == player:
                    directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
                    for dr, dc in directions:
                        mid_row, mid_col = row + dr, col + dc
                        end_row, end_col = row + 2*dr, col + 2*dc
                        if 0 <= end_row < 8 and 0 <= end_col < 8:
                            mid_piece = self.get_piece((mid_row, mid_col))
                            end_piece = self.get_piece((end_row, end_col))
                            if mid_piece and mid_piece.player != player and not end_piece:
                                return True
        return False