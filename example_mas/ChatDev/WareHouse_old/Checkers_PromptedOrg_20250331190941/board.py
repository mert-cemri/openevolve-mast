'''
Defines the Board class to manage the game state, validate moves, and handle game logic, including multiple sequential captures.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.board = [[None for _ in range(8)] for _ in range(8)]
        self.setup_board()
    def setup_board(self):
        for row in range(3):
            for col in range((row + 1) % 2, 8, 2):
                self.board[row][col] = Piece('B')
        for row in range(5, 8):
            for col in range((row + 1) % 2, 8, 2):
                self.board[row][col] = Piece('W')
    def draw_board(self):
        print("  0 1 2 3 4 5 6 7")
        for idx, row in enumerate(self.board):
            print(idx, end=" ")
            for piece in row:
                print(piece if piece else '.', end=" ")
            print()
        print()
    def get_piece(self, position):
        row, col = position
        return self.board[row][col]
    def remove_piece(self, position):
        row, col = position
        self.board[row][col] = None
    def move_piece(self, from_pos, to_pos):
        piece = self.get_piece(from_pos)
        self.board[to_pos[0]][to_pos[1]] = piece
        self.remove_piece(from_pos)
        # Check for kinging
        if piece.color == 'W' and to_pos[0] == 0:
            piece.make_king()
        elif piece.color == 'B' and to_pos[0] == 7:
            piece.make_king()
        # Check for captures
        if abs(from_pos[0] - to_pos[0]) == 2:
            captured_row = (from_pos[0] + to_pos[0]) // 2
            captured_col = (from_pos[1] + to_pos[1]) // 2
            self.remove_piece((captured_row, captured_col))
    def valid_move(self, from_pos, to_pos, player_color):
        fr, fc = from_pos
        tr, tc = to_pos
        piece = self.get_piece(from_pos)
        if not piece or piece.color != player_color:
            return False
        if self.get_piece(to_pos):
            return False
        row_diff = tr - fr
        col_diff = tc - fc
        # Normal move
        if abs(row_diff) == 1 and abs(col_diff) == 1:
            if piece.king:
                return True  # Kings can move in both directions
            direction = -1 if piece.color == 'W' else 1
            return row_diff == direction
        # Capture move
        if abs(row_diff) == 2 and abs(col_diff) == 2:
            mid_row = (fr + tr) // 2
            mid_col = (fc + tc) // 2
            mid_piece = self.get_piece((mid_row, mid_col))
            if mid_piece and mid_piece.color != player_color:
                if piece.king:
                    return True  # Kings can capture in both directions
                direction = -1 if piece.color == 'W' else 1
                return row_diff == 2 * direction
        return False
    def has_capture_moves(self, position):
        piece = self.get_piece(position)
        if not piece:
            return False
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]
        for dr, dc in directions:
            mid_row, mid_col = position[0] + dr, position[1] + dc
            end_row, end_col = position[0] + 2*dr, position[1] + 2*dc
            if 0 <= mid_row < 8 and 0 <= mid_col < 8 and 0 <= end_row < 8 and 0 <= end_col < 8:
                mid_piece = self.get_piece((mid_row, mid_col))
                end_piece = self.get_piece((end_row, end_col))
                if mid_piece and mid_piece.color != piece.color and not end_piece:
                    if piece.king or (piece.color == 'W' and dr == -1) or (piece.color == 'B' and dr == 1):
                        return True
        return False
    def check_winner(self):
        white_pieces = black_pieces = 0
        for row in self.board:
            for piece in row:
                if piece:
                    if piece.color == 'W':
                        white_pieces += 1
                    else:
                        black_pieces += 1
        if white_pieces == 0:
            return 'Black'
        elif black_pieces == 0:
            return 'White'
        return None