'''
Represents the game board and handles board-related operations.
'''
from piece import Piece
from utils import parse_move
class Board:
    def __init__(self):
        self.grid = self.initialize_board()
    def initialize_board(self):
        # Initialize an 8x8 board with pieces in starting positions
        grid = [[None for _ in range(8)] for _ in range(8)]
        # Place black pieces
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    grid[row][col] = Piece('black')
        # Place white pieces
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    grid[row][col] = Piece('white')
        return grid
    def display(self):
        # Display the board in a readable format
        for row in self.grid:
            print(' '.join(['.' if piece is None else piece.color[0] for piece in row]))
    def move_piece(self, move, player_color):
        start, end = parse_move(move)
        if self.is_valid_move(start, end, player_color):
            self.apply_move(start, end)
            return True
        return False
    def is_valid_move(self, start, end, player_color):
        # Check if the move is within bounds
        if not (0 <= start[0] < 8 and 0 <= start[1] < 8 and 0 <= end[0] < 8 and 0 <= end[1] < 8):
            return False
        piece = self.grid[start[0]][start[1]]
        if piece is None or piece.color != player_color:
            return False
        # Check if the destination is empty
        if self.grid[end[0]][end[1]] is not None:
            return False
        # Calculate move direction and distance
        row_diff = end[0] - start[0]
        col_diff = end[1] - start[1]
        # Check for simple move
        if abs(row_diff) == 1 and abs(col_diff) == 1:
            if (piece.is_king or (piece.color == 'black' and row_diff == 1) or (piece.color == 'white' and row_diff == -1)):
                return True
        # Check for capture move
        if abs(row_diff) == 2 and abs(col_diff) == 2:
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2
            mid_piece = self.grid[mid_row][mid_col]
            if mid_piece is not None and mid_piece.color != player_color:
                return True
        return False
    def apply_move(self, start, end):
        # Move the piece and handle captures
        piece = self.grid[start[0]][start[1]]
        self.grid[end[0]][end[1]] = piece
        self.grid[start[0]][start[1]] = None
        # Handle capture
        if abs(end[0] - start[0]) == 2:
            mid_row = (start[0] + end[0]) // 2
            mid_col = (start[1] + end[1]) // 2
            self.grid[mid_row][mid_col] = None
        # Handle kinging
        if (piece.color == 'black' and end[0] == 7) or (piece.color == 'white' and end[0] == 0):
            piece.is_king = True
    def can_continue_capture(self, move):
        # Check if the piece can continue capturing
        _, end = parse_move(move)
        piece = self.grid[end[0]][end[1]]
        if piece is None:
            return False
        for d_row in [-2, 2]:
            for d_col in [-2, 2]:
                new_end = (end[0] + d_row, end[1] + d_col)
                if self.is_valid_move(end, new_end, piece.color):
                    return True
        return False
    def is_player_out_of_moves(self, player_color):
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece is not None and piece.color == player_color:
                    for d_row in [-1, 1]:
                        for d_col in [-1, 1]:
                            if self.is_valid_move((row, col), (row + d_row, col + d_col), player_color):
                                return False
                            if self.is_valid_move((row, col), (row + 2 * d_row, col + 2 * d_col), player_color):
                                return False
        return True