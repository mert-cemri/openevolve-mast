'''
Defines the Piece class and its subclasses for each type of chess piece.
'''
class Piece:
    def __init__(self, color):
        self.color = color
    def __str__(self):
        return self.symbol()
    def symbol(self):
        return 'P'
    def valid_moves(self, position, board):
        # Return a list of valid moves for the piece
        return []
class Pawn(Piece):
    def symbol(self):
        return 'P' if self.color == 'white' else 'p'
    def valid_moves(self, position, board):
        # Implement pawn-specific movement rules
        moves = []
        direction = -1 if self.color == 'white' else 1
        start_row = 6 if self.color == 'white' else 1
        # Move forward
        if board[position[0] + direction][position[1]] is None:
            moves.append((position[0] + direction, position[1]))
            # Double move from starting position
            if position[0] == start_row and board[position[0] + 2 * direction][position[1]] is None:
                moves.append((position[0] + 2 * direction, position[1]))
        # Capture diagonally
        for dx in [-1, 1]:
            if 0 <= position[1] + dx < 8:
                target = board[position[0] + direction][position[1] + dx]
                if target and target.color != self.color:
                    moves.append((position[0] + direction, position[1] + dx))
        return moves
class Rook(Piece):
    def symbol(self):
        return 'R' if self.color == 'white' else 'r'
    def valid_moves(self, position, board):
        # Implement rook-specific movement rules
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for dx, dy in directions:
            x, y = position
            while True:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8:
                    if board[x][y] is None:
                        moves.append((x, y))
                    elif board[x][y].color != self.color:
                        moves.append((x, y))
                        break
                    else:
                        break
                else:
                    break
        return moves
class Knight(Piece):
    def symbol(self):
        return 'N' if self.color == 'white' else 'n'
    def valid_moves(self, position, board):
        # Implement knight-specific movement rules
        moves = []
        knight_moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
        for dx, dy in knight_moves:
            x, y = position[0] + dx, position[1] + dy
            if 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] is None or board[x][y].color != self.color:
                    moves.append((x, y))
        return moves
class Bishop(Piece):
    def symbol(self):
        return 'B' if self.color == 'white' else 'b'
    def valid_moves(self, position, board):
        # Implement bishop-specific movement rules
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in directions:
            x, y = position
            while True:
                x += dx
                y += dy
                if 0 <= x < 8 and 0 <= y < 8:
                    if board[x][y] is None:
                        moves.append((x, y))
                    elif board[x][y].color != self.color:
                        moves.append((x, y))
                        break
                    else:
                        break
                else:
                    break
        return moves
class Queen(Piece):
    def symbol(self):
        return 'Q' if self.color == 'white' else 'q'
    def valid_moves(self, position, board):
        # Implement queen-specific movement rules
        moves = Rook(self.color).valid_moves(position, board) + Bishop(self.color).valid_moves(position, board)
        return moves
class King(Piece):
    def symbol(self):
        return 'K' if self.color == 'white' else 'k'
    def valid_moves(self, position, board):
        # Implement king-specific movement rules
        moves = []
        king_moves = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (1, -1), (-1, 1), (-1, -1)]
        for dx, dy in king_moves:
            x, y = position[0] + dx, position[1] + dy
            if 0 <= x < 8 and 0 <= y < 8:
                if board[x][y] is None or board[x][y].color != self.color:
                    moves.append((x, y))
        return moves