'''
Defines the Board class for managing the checkers board state and operations.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.board = self.initialize_board()
    def initialize_board(self):
        board = [[None for _ in range(8)] for _ in range(8)]
        for row in range(3):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = Piece('black')
        for row in range(5, 8):
            for col in range(8):
                if (row + col) % 2 == 1:
                    board[row][col] = Piece('white')
        return board
    def display_board(self):
        for row in self.board:
            print(' '.join(['.' if piece is None else 'B' if piece.color == 'black' else 'W' for piece in row]))
    def move_piece(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        self.board[tx][ty] = self.board[fx][fy]
        self.board[fx][fy] = None
        if abs(fx - tx) == 2:  # Capture move
            self.capture_piece(from_pos, to_pos)
        self.king_piece(to_pos)
    def is_valid_move(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        piece = self.board[fx][fy]
        if piece is None or self.board[tx][ty] is not None:
            return False
        direction = 1 if piece.color == 'black' else -1
        if piece.is_king:
            return (abs(fx - tx) == 1 and abs(fy - ty) == 1) or self.is_valid_capture(from_pos, to_pos)
        return ((tx - fx == direction) and abs(fy - ty) == 1) or self.is_valid_capture(from_pos, to_pos)
    def is_valid_capture(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        if abs(fx - tx) == 2 and abs(fy - ty) == 2:
            mx, my = (fx + tx) // 2, (fy + ty) // 2
            middle_piece = self.board[mx][my]
            if middle_piece and middle_piece.color != self.board[fx][fy].color:
                return True
        return False
    def capture_piece(self, from_pos, to_pos):
        fx, fy = from_pos
        tx, ty = to_pos
        mx, my = (fx + tx) // 2, (fy + ty) // 2
        self.board[mx][my] = None
    def king_piece(self, position):
        x, y = position
        piece = self.board[x][y]
        if piece and ((piece.color == 'black' and x == 7) or (piece.color == 'white' and x == 0)):
            piece.is_king = True