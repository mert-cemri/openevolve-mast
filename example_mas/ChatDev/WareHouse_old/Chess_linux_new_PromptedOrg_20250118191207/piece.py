'''
Defines the Piece class and its subclasses for different types of chess pieces.
'''
class Piece:
    def __init__(self, color):
        self.color = color
    def is_valid_move(self, start_pos, end_pos, board):
        raise NotImplementedError("This method should be overridden in subclasses.")
class Pawn(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement pawn-specific move logic
        direction = 1 if self.color == 'white' else -1
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        # Move forward
        if start_col == end_col:
            if end_row == start_row + direction and board[end_row][end_col] == ' ':
                return True
            if (start_row == 1 and self.color == 'white' or start_row == 6 and self.color == 'black') and \
               end_row == start_row + 2 * direction and board[end_row][end_col] == ' ':
                return True
        # Capture
        if abs(start_col - end_col) == 1 and end_row == start_row + direction and board[end_row][end_col] != ' ':
            return True
        return False
class Rook(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement rook-specific move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if start_row != end_row and start_col != end_col:
            return False
        if start_row == end_row:
            step = 1 if start_col < end_col else -1
            for col in range(start_col + step, end_col, step):
                if board[start_row][col] != ' ':
                    return False
        if start_col == end_col:
            step = 1 if start_row < end_row else -1
            for row in range(start_row + step, end_row, step):
                if board[row][start_col] != ' ':
                    return False
        return True
class Knight(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement knight-specific move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        row_diff = abs(start_row - end_row)
        col_diff = abs(start_col - end_col)
        return (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2)
class Bishop(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement bishop-specific move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        if abs(start_row - end_row) != abs(start_col - end_col):
            return False
        row_step = 1 if start_row < end_row else -1
        col_step = 1 if start_col < end_col else -1
        for step in range(1, abs(start_row - end_row)):
            if board[start_row + step * row_step][start_col + step * col_step] != ' ':
                return False
        return True
class Queen(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement queen-specific move logic
        rook = Rook(self.color)
        bishop = Bishop(self.color)
        return rook.is_valid_move(start_pos, end_pos, board) or bishop.is_valid_move(start_pos, end_pos, board)
class King(Piece):
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement king-specific move logic
        start_row, start_col = start_pos
        end_row, end_col = end_pos
        return max(abs(start_row - end_row), abs(start_col - end_col)) == 1