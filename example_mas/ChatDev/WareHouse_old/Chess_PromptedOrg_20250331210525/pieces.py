'''
Defines chess pieces and their movement logic.
'''
class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False
    def is_valid_move(self, move, board):
        raise NotImplementedError
    def move(self, move, board):
        board.board[move.end_row][move.end_col] = self
        board.board[move.start_row][move.start_col] = None
        self.has_moved = True
    def can_attack(self, target_pos, board, current_pos):
        move = Move(current_pos, target_pos, self.color)
        return self.is_valid_move(move, board)
class King(Piece):
    def is_valid_move(self, move, board):
        dr = abs(move.start_row - move.end_row)
        dc = abs(move.start_col - move.end_col)
        return max(dr, dc) == 1
class Queen(Piece):
    def is_valid_move(self, move, board):
        dr = abs(move.start_row - move.end_row)
        dc = abs(move.start_col - move.end_col)
        return dr == dc or move.start_row == move.end_row or move.start_col == move.end_col
class Rook(Piece):
    def is_valid_move(self, move, board):
        return move.start_row == move.end_row or move.start_col == move.end_col
class Bishop(Piece):
    def is_valid_move(self, move, board):
        return abs(move.start_row - move.end_row) == abs(move.start_col - move.end_col)
class Knight(Piece):
    def is_valid_move(self, move, board):
        dr = abs(move.start_row - move.end_row)
        dc = abs(move.start_col - move.end_col)
        return (dr, dc) in [(2, 1), (1, 2)]
class Pawn(Piece):
    def is_valid_move(self, move, board):
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1
        dr = move.end_row - move.start_row
        dc = abs(move.start_col - move.end_col)
        if dc == 0:
            if dr == direction:
                return board.board[move.end_row][move.end_col] is None
            if dr == 2 * direction and move.start_row == start_row:
                return board.board[move.end_row][move.end_col] is None and board.board[move.start_row + direction][move.start_col] is None
        elif dc == 1 and dr == direction:
            target_piece = board.board[move.end_row][move.end_col]
            return target_piece is not None and target_piece.color != self.color
        return False