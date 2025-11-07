'''
Represents the chessboard and manages the state of the game.
'''
from pieces import Pawn, Rook, Knight, Bishop, Queen, King
class Board:
    def __init__(self):
        self.board = []
    def initialize_board(self):
        # Initialize board with pieces in starting positions
        self.board = [
            [Rook('Black'), Knight('Black'), Bishop('Black'), Queen('Black'), King('Black'), Bishop('Black'), Knight('Black'), Rook('Black')],
            [Pawn('Black') for _ in range(8)],
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [None] * 8,
            [Pawn('White') for _ in range(8)],
            [Rook('White'), Knight('White'), Bishop('White'), Queen('White'), King('White'), Bishop('White'), Knight('White'), Rook('White')]
        ]
    def print_board(self):
        for row in self.board:
            print(' '.join([piece.symbol if piece else '.' for piece in row]))
    def move_piece(self, start_pos, end_pos, player):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        piece = self.board[start_x][start_y]
        if piece and piece.color == player and piece.is_valid_move(start_pos, end_pos, self.board):
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = None
            return True
        return False
    def is_in_check(self, player):
        # Implement logic to determine if the player's king is in check
        king_pos = None
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.color == player and isinstance(piece, King):
                    king_pos = (x, y)
                    break
            if king_pos:
                break
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.color != player:
                    if piece.is_valid_move((x, y), king_pos, self.board):
                        return True
        return False
    def is_checkmate(self, player):
        if not self.is_in_check(player):
            return False
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece and piece.color == player:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx != 0 or dy != 0:
                                new_x, new_y = x + dx, y + dy
                                if 0 <= new_x < 8 and 0 <= new_y < 8:
                                    if piece.is_valid_move((x, y), (new_x, new_y), self.board):
                                        original_piece = self.board[new_x][new_y]
                                        self.board[new_x][new_y] = piece
                                        self.board[x][y] = None
                                        if not self.is_in_check(player):
                                            self.board[x][y] = piece
                                            self.board[new_x][new_y] = original_piece
                                            return False
                                        self.board[x][y] = piece
                                        self.board[new_x][new_y] = original_piece
        return True