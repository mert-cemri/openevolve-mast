'''
ChessBoard class to manage the state of the chessboard and validate moves.
'''
from pieces import King, Queen, Rook, Bishop, Knight, Pawn
from move import Move
import copy
class ChessBoard:
    def __init__(self):
        self.board = self.setup_board()
        self.move_history = []
        self.en_passant_target = None
    def setup_board(self):
        board = [[None]*8 for _ in range(8)]
        for i in range(8):
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')
        placement = [Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook]
        for i, piece in enumerate(placement):
            board[0][i] = piece('black')
            board[7][i] = piece('white')
        return board
    def make_move(self, move):
        piece = self.board[move.start_row][move.start_col]
        if piece and piece.color == move.player and piece.is_valid_move(move, self):
            temp_board = copy.deepcopy(self)
            piece.move(move, temp_board)
            if temp_board.is_in_check(move.player):
                return False
            piece.move(move, self)
            self.move_history.append(move)
            self.update_en_passant(piece, move)
            return True
        return False
    def update_en_passant(self, piece, move):
        if isinstance(piece, Pawn) and abs(move.start_row - move.end_row) == 2:
            self.en_passant_target = ((move.start_row + move.end_row)//2, move.start_col)
        else:
            self.en_passant_target = None
    def is_in_check(self, color):
        king_pos = None
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if isinstance(piece, King) and piece.color == color:
                    king_pos = (r, c)
                    break
        opponent_color = 'black' if color == 'white' else 'white'
        for r in range(8):
            for c in range(8):
                piece = self.board[r][c]
                if piece and piece.color == opponent_color:
                    if piece.can_attack(king_pos, self, (r, c)):
                        return True
        return False