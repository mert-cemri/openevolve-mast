'''
Defines the ChessBoard class to represent the chessboard and its operations.
'''
from piece import Piece
from utils import parse_move
class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
    def initialize_board(self):
        # Initialize the board with pieces in their starting positions
        board = [['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R'],
                 ['P', 'P', 'P', 'P', 'P', 'P', 'P', 'P'],
                 [' ' for _ in range(8)],
                 [' ' for _ in range(8)],
                 [' ' for _ in range(8)],
                 [' ' for _ in range(8)],
                 ['p', 'p', 'p', 'p', 'p', 'p', 'p', 'p'],
                 ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']]
        return board
    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()
    def move_piece(self, move):
        start_pos, end_pos = parse_move(move)
        piece = self.board[start_pos[0]][start_pos[1]]
        self.board[end_pos[0]][end_pos[1]] = piece
        self.board[start_pos[0]][start_pos[1]] = ' '
    def is_valid_move(self, move, turn):
        start_pos, end_pos = parse_move(move)
        piece = self.board[start_pos[0]][start_pos[1]]
        if piece == ' ':
            return False
        piece_obj = Piece(piece)
        return piece_obj.is_valid_move(start_pos, end_pos, self.board, turn)