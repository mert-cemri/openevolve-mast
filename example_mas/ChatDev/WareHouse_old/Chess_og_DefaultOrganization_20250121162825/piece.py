'''
Represents a chess piece and its possible moves.
'''
class Piece:
    def __init__(self, color):
        self.color = color
    def is_valid_move(self, start, end, board):
        # Simplified move validation
        return True
    def __str__(self):
        return self.type[0].upper() if self.color == 'White' else self.type[0].lower()
class Pawn(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Pawn'
    def is_valid_move(self, start, end, board):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        direction = 1 if self.color == 'White' else -1
        if start_y == end_y and board[end_x][end_y] == ' ':
            if end_x == start_x + direction:
                return True
            if (start_x == 1 and self.color == 'Black') or (start_x == 6 and self.color == 'White'):
                if end_x == start_x + 2 * direction and board[start_x + direction][start_y] == ' ':
                    return True
        if abs(start_y - end_y) == 1 and end_x == start_x + direction and board[end_x][end_y] != ' ':
            return True
        return False
class Rook(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Rook'
    def is_valid_move(self, start, end, board):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        if start_x == end_x or start_y == end_y:
            if all(board[x][y] == ' ' for x, y in self.path(start_x, start_y, end_x, end_y)):
                return True
        return False
    def path(self, start_x, start_y, end_x, end_y):
        if start_x == end_x:
            step = 1 if start_y < end_y else -1
            return [(start_x, y) for y in range(start_y + step, end_y, step)]
        else:
            step = 1 if start_x < end_x else -1
            return [(x, start_y) for x in range(start_x + step, end_x, step)]
class Knight(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Knight'
    def is_valid_move(self, start, end, board):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        dx, dy = abs(start_x - end_x), abs(start_y - end_y)
        return (dx, dy) in [(2, 1), (1, 2)]
class Bishop(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Bishop'
    def is_valid_move(self, start, end, board):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        if abs(start_x - end_x) == abs(start_y - end_y):
            if all(board[x][y] == ' ' for x, y in self.path(start_x, start_y, end_x, end_y)):
                return True
        return False
    def path(self, start_x, start_y, end_x, end_y):
        step_x = 1 if start_x < end_x else -1
        step_y = 1 if start_y < end_y else -1
        return [(start_x + i * step_x, start_y + i * step_y) for i in range(1, abs(start_x - end_x))]
class Queen(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'Queen'
    def is_valid_move(self, start, end, board):
        return Rook(self.color).is_valid_move(start, end, board) or Bishop(self.color).is_valid_move(start, end, board)
class King(Piece):
    def __init__(self, color):
        super().__init__(color)
        self.type = 'King'
    def is_valid_move(self, start, end, board):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        return max(abs(start_x - end_x), abs(start_y - end_y)) == 1