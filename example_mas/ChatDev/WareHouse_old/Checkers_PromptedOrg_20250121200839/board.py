'''
Represents the game board and manages piece positions.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    def setup_pieces(self):
        # Set up initial pieces on the board
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('B')
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    self.grid[row][col] = Piece('W')
    def display(self):
        for row in self.grid:
            print(' '.join(['.' if piece is None else piece.symbol for piece in row]))
    def move_piece(self, start_pos, end_pos):
        piece = self.grid[start_pos[0]][start_pos[1]]
        self.grid[end_pos[0]][end_pos[1]] = piece
        self.grid[start_pos[0]][start_pos[1]] = None
        # Capture logic
        if abs(start_pos[0] - end_pos[0]) == 2:
            mid_row = (start_pos[0] + end_pos[0]) // 2
            mid_col = (start_pos[1] + end_pos[1]) // 2
            self.grid[mid_row][mid_col] = None
        # Kinging logic
        if (piece.color == 'W' and end_pos[0] == 0) or (piece.color == 'B' and end_pos[0] == 7):
            piece.make_king()
    def is_valid_move(self, start_pos, end_pos, player):
        if not (0 <= start_pos[0] < 8 and 0 <= start_pos[1] < 8 and 0 <= end_pos[0] < 8 and 0 <= end_pos[1] < 8):
            return False
        piece = self.grid[start_pos[0]][start_pos[1]]
        if piece is None or piece.color != player:
            return False
        if self.grid[end_pos[0]][end_pos[1]] is not None:
            return False
        direction = -1 if player == 'W' else 1
        if piece.is_king:
            if abs(start_pos[0] - end_pos[0]) == 1 and abs(start_pos[1] - end_pos[1]) == 1:
                return True
        else:
            if start_pos[0] + direction == end_pos[0] and abs(start_pos[1] - end_pos[1]) == 1:
                return True
        if abs(start_pos[0] - end_pos[0]) == 2 and abs(start_pos[1] - end_pos[1]) == 2:
            mid_row = (start_pos[0] + end_pos[0]) // 2
            mid_col = (start_pos[1] + end_pos[1]) // 2
            mid_piece = self.grid[mid_row][mid_col]
            if mid_piece is not None and mid_piece.color != player:
                return True
        return False
    def get_capturing_moves(self, player):
        capturing_moves = []
        for row in range(8):
            for col in range(8):
                piece = self.grid[row][col]
                if piece is not None and piece.color == player:
                    # Check all possible capture directions
                    for dr, dc in [(-2, -2), (-2, 2), (2, -2), (2, 2)]:
                        end_pos = (row + dr, col + dc)
                        if self.is_valid_move((row, col), end_pos, player):
                            capturing_moves.append(((row, col), end_pos))
        return capturing_moves