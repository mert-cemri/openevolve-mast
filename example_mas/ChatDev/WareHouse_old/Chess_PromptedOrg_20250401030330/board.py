'''
Manages the chessboard state, moves, validations, and special moves tracking.
'''
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
class Board:
    def __init__(self):
        self.board = [[None]*8 for _ in range(8)]
        self.setup_board()
        self.en_passant_target = None
    def setup_board(self):
        for i in range(8):
            self.board[1][i] = Pawn('black')
            self.board[6][i] = Pawn('white')
        order = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(order):
            self.board[0][i] = piece('black')
            self.board[7][i] = piece('white')
    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        piece.has_moved = True
        # En passant capture
        if isinstance(piece, Pawn) and end == self.en_passant_target:
            self.board[start[0]][end[1]] = None
        # Castling move
        if isinstance(piece, King) and abs(end[1] - start[1]) == 2:
            rook_start_y = 0 if end[1] < start[1] else 7
            rook_end_y = start[1] + (-1 if rook_start_y == 0 else 1)
            self.move_piece((start[0], rook_start_y), (start[0], rook_end_y))
        self.board[end[0]][end[1]] = piece
        self.board[start[0]][start[1]] = None
        # Pawn promotion
        if isinstance(piece, Pawn) and (end[0] == 0 or end[0] == 7):
            self.board[end[0]][end[1]] = Queen(piece.color)
        # En passant target update
        self.en_passant_target = None
        if isinstance(piece, Pawn) and abs(end[0] - start[0]) == 2:
            self.en_passant_target = ((start[0] + end[0]) // 2, start[1])
    def is_empty(self, position):
        x, y = position
        return self.in_bounds(position) and self.board[x][y] is None
    def is_enemy(self, position, color):
        x, y = position
        return self.in_bounds(position) and self.board[x][y] and self.board[x][y].color != color
    def in_bounds(self, position):
        x, y = position
        return 0 <= x < 8 and 0 <= y < 8
    def print_board(self):
        for row in self.board:
            print(' '.join([type(piece).__name__[0] if piece else '.' for piece in row]))