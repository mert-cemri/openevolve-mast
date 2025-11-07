'''
Defines chess pieces and their movement logic.
'''
class Piece:
    def __init__(self, color):
        self.color = color
    def is_valid_move(self, start_pos, end_pos, board):
        raise NotImplementedError("This method should be overridden in derived classes.")
class Pawn(Piece):
    symbol = 'P'
    def is_valid_move(self, start_pos, end_pos, board):
        # Implement pawn-specific movement logic
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        direction = 1 if self.color == 'White' else -1
        if start_y == end_y and board[end_x][end_y] is None:
            if end_x == start_x + direction:
                return True
            if (start_x == 1 and self.color == 'Black' or start_x == 6 and self.color == 'White') and end_x == start_x + 2 * direction:
                return board[start_x + direction][start_y] is None
        if abs(start_y - end_y) == 1 and end_x == start_x + direction and board[end_x][end_y] is not None:
            return board[end_x][end_y].color != self.color
        return False
class Rook(Piece):
    symbol = 'R'
    def is_valid_move(self, start_pos, end_pos, board):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        if start_x == end_x or start_y == end_y:
            step_x = 0 if start_x == end_x else (1 if end_x > start_x else -1)
            step_y = 0 if start_y == end_y else (1 if end_y > start_y else -1)
            x, y = start_x + step_x, start_y + step_y
            while (x, y) != (end_x, end_y):
                if board[x][y] is not None:
                    return False
                x += step_x
                y += step_y
            return board[end_x][end_y] is None or board[end_x][end_y].color != self.color
        return False
class Knight(Piece):
    symbol = 'N'
    def is_valid_move(self, start_pos, end_pos, board):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        dx, dy = abs(start_x - end_x), abs(start_y - end_y)
        return (dx, dy) in [(2, 1), (1, 2)] and (board[end_x][end_y] is None or board[end_x][end_y].color != self.color)
class Bishop(Piece):
    symbol = 'B'
    def is_valid_move(self, start_pos, end_pos, board):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        if abs(start_x - end_x) == abs(start_y - end_y):
            step_x = 1 if end_x > start_x else -1
            step_y = 1 if end_y > start_y else -1
            x, y = start_x + step_x, start_y + step_y
            while (x, y) != (end_x, end_y):
                if board[x][y] is not None:
                    return False
                x += step_x
                y += step_y
            return board[end_x][end_y] is None or board[end_x][end_y].color != self.color
        return False
class Queen(Piece):
    symbol = 'Q'
    def is_valid_move(self, start_pos, end_pos, board):
        # Queen's move is a combination of Rook and Bishop
        return Rook(self.color).is_valid_move(start_pos, end_pos, board) or Bishop(self.color).is_valid_move(start_pos, end_pos, board)
class King(Piece):
    symbol = 'K'
    def is_valid_move(self, start_pos, end_pos, board):
        start_x, start_y = start_pos
        end_x, end_y = end_pos
        dx, dy = abs(start_x - end_x), abs(start_y - end_y)
        return max(dx, dy) == 1 and (board[end_x][end_y] is None or board[end_x][end_y].color != self.color)