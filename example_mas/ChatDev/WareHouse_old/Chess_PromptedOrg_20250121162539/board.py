'''
Board class to manage the chess board and its operations.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.board = []
    def initialize_board(self):
        self.board = [
            ["R", "N", "B", "Q", "K", "B", "N", "R"],
            ["P", "P", "P", "P", "P", "P", "P", "P"],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            [".", ".", ".", ".", ".", ".", ".", "."],
            ["p", "p", "p", "p", "p", "p", "p", "p"],
            ["r", "n", "b", "q", "k", "b", "n", "r"]
        ]
    def display(self):
        for row in self.board:
            print(" ".join(row))
        print()
    def update_board(self, move):
        start_pos, end_pos = self.parse_move(move)
        piece = self.get_piece_at(start_pos)
        self.set_piece_at(end_pos, piece)
        self.set_piece_at(start_pos, ".")
    def is_valid_move(self, move, player_color):
        start_pos, end_pos = self.parse_move(move)
        piece = self.get_piece_at(start_pos)
        if piece.piece_type == "." or piece.color != player_color:
            return False
        return piece.is_valid_move(start_pos, end_pos, self)
    def parse_move(self, move):
        start_pos = (8 - int(move[1]), ord(move[0]) - ord('a'))
        end_pos = (8 - int(move[3]), ord(move[2]) - ord('a'))
        return start_pos, end_pos
    def get_piece_at(self, position):
        row, col = position
        piece_char = self.board[row][col]
        if piece_char == ".":
            return Piece("None", ".")
        color = "White" if piece_char.isupper() else "Black"
        return Piece(color, piece_char)
    def set_piece_at(self, position, piece):
        row, col = position
        self.board[row][col] = piece.piece_type
    def is_checkmate(self, color):
        # Placeholder for checkmate logic
        # Implement checkmate logic here
        return False