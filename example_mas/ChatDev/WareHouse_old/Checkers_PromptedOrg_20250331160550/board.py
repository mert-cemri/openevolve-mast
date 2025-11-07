'''
This module defines the Board class, which represents the game board and manages piece positions and moves.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    def setup_pieces(self):
        # Initialize pieces on the board
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('B')
                    self.grid[7-row][col] = Piece('W')
    def is_valid_move(self, from_pos, to_pos, player):
        # Check if the move is within bounds
        if not self.is_within_bounds(from_pos) or not self.is_within_bounds(to_pos):
            return False
        # Check if the move is to an empty square
        if self.grid[to_pos[0]][to_pos[1]] is not None:
            return False
        # Check if the move is diagonal
        row_diff = to_pos[0] - from_pos[0]
        col_diff = to_pos[1] - from_pos[1]
        if abs(row_diff) != abs(col_diff):
            return False
        # Check if the move is a simple move or a capture
        piece = self.grid[from_pos[0]][from_pos[1]]
        if piece is None or piece.color != player:
            return False
        # Allow king pieces to move in any diagonal direction
        if piece.is_king:
            if abs(row_diff) == 1:
                return True
            elif abs(row_diff) == 2:
                mid_row = (from_pos[0] + to_pos[0]) // 2
                mid_col = (from_pos[1] + to_pos[1]) // 2
                mid_piece = self.grid[mid_row][mid_col]
                if mid_piece is not None and mid_piece.color != player:
                    return True
        else:
            # Normal pieces can only move forward
            direction = -1 if player == 'W' else 1
            if row_diff == direction and abs(row_diff) == 1:
                return True
            elif row_diff == 2 * direction and abs(row_diff) == 2:
                mid_row = (from_pos[0] + to_pos[0]) // 2
                mid_col = (from_pos[1] + to_pos[1]) // 2
                mid_piece = self.grid[mid_row][mid_col]
                if mid_piece is not None and mid_piece.color != player:
                    return True
        return False
    def apply_move(self, from_pos, to_pos):
        piece = self.grid[from_pos[0]][from_pos[1]]
        self.grid[to_pos[0]][to_pos[1]] = piece
        self.grid[from_pos[0]][from_pos[1]] = None
        # Check for capture
        if abs(to_pos[0] - from_pos[0]) == 2:
            mid_row = (from_pos[0] + to_pos[0]) // 2
            mid_col = (from_pos[1] + to_pos[1]) // 2
            self.grid[mid_row][mid_col] = None
        # Check for kinging
        if (piece.color == 'W' and to_pos[0] == 0) or (piece.color == 'B' and to_pos[0] == 7):
            piece.make_king()
    def is_game_over(self, current_player):
        # Check if either player has no pieces left
        white_pieces = black_pieces = 0
        for row in self.grid:
            for piece in row:
                if piece is not None:
                    if piece.color == 'W':
                        white_pieces += 1
                    else:
                        black_pieces += 1
        if white_pieces == 0 or black_pieces == 0:
            return True
        # Check if the current player has any valid moves
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece is not None and piece.color == current_player:
                    # Check all possible moves for this piece
                    for d_row in [-1, 1]:
                        for d_col in [-1, 1]:
                            to_pos = (row + d_row, col + d_col)
                            if self.is_valid_move((row, col), to_pos, current_player):
                                return False
                            # Check for capture moves
                            to_pos = (row + 2*d_row, col + 2*d_col)
                            if self.is_valid_move((row, col), to_pos, current_player):
                                return False
        return True
    def is_within_bounds(self, pos):
        return 0 <= pos[0] < 8 and 0 <= pos[1] < 8