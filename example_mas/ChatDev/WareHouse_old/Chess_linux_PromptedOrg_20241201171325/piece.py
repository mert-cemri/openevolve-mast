'''
Defines the Piece class to represent a chess piece and its behavior.
'''
class Piece:
    def __init__(self, piece_type):
        self.piece_type = piece_type.lower()
        self.color = 'white' if piece_type.isupper() else 'black'
    def is_valid_move(self, start_pos, end_pos, board, turn):
        if self.color != turn:
            return False
        # Implement logic to check if a move is valid for this piece
        if self.piece_type == 'p':  # Pawn
            return self.is_valid_pawn_move(start_pos, end_pos, board)
        elif self.piece_type == 'r':  # Rook
            return self.is_valid_rook_move(start_pos, end_pos, board)
        elif self.piece_type == 'n':  # Knight
            return self.is_valid_knight_move(start_pos, end_pos)
        elif self.piece_type == 'b':  # Bishop
            return self.is_valid_bishop_move(start_pos, end_pos, board)
        elif self.piece_type == 'q':  # Queen
            return self.is_valid_queen_move(start_pos, end_pos, board)
        elif self.piece_type == 'k':  # King
            return self.is_valid_king_move(start_pos, end_pos, board)
        return False
    def is_valid_pawn_move(self, start_pos, end_pos, board):
        # Implement pawn move logic
        direction = -1 if self.color == 'white' else 1
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if start_col == end_col:  # Forward move
            if board[end_row][end_col] == ' ':
                if end_row == start_row + direction:
                    return True
                if (start_row == 1 and self.color == 'black' or start_row == 6 and self.color == 'white') and end_row == start_row + 2 * direction:
                    return board[start_row + direction][start_col] == ' '
        elif abs(start_col - end_col) == 1 and end_row == start_row + direction:  # Capture
            return board[end_row][end_col] != ' ' and board[end_row][end_col].islower() != self.color.islower()
        return False
    def is_valid_rook_move(self, start_pos, end_pos, board):
        # Implement rook move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if start_row == end_row or start_col == end_col:
            step_row = 0 if start_row == end_row else (1 if end_row > start_row else -1)
            step_col = 0 if start_col == end_col else (1 if end_col > start_col else -1)
            current_row, current_col = start_row + step_row, start_col + step_col
            while (current_row, current_col) != (end_row, end_col):
                if board[current_row][current_col] != ' ':
                    return False
                current_row += step_row
                current_col += step_col
            return True
        return False
    def is_valid_knight_move(self, start_pos, end_pos):
        # Implement knight move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        return (abs(start_row - end_row), abs(start_col - end_col)) in [(2, 1), (1, 2)]
    def is_valid_bishop_move(self, start_pos, end_pos, board):
        # Implement bishop move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if abs(start_row - end_row) == abs(start_col - end_col):
            step_row = 1 if end_row > start_row else -1
            step_col = 1 if end_col > start_col else -1
            current_row, current_col = start_row + step_row, start_col + step_col
            while (current_row, current_col) != (end_row, end_col):
                if board[current_row][current_col] != ' ':
                    return False
                current_row += step_row
                current_col += step_col
            return True
        return False
    def is_valid_queen_move(self, start_pos, end_pos, board):
        # Implement queen move logic
        return self.is_valid_rook_move(start_pos, end_pos, board) or self.is_valid_bishop_move(start_pos, end_pos, board)
    def is_valid_king_move(self, start_pos, end_pos, board):
        # Implement king move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        return max(abs(start_row - end_row), abs(start_col - end_col)) == 1