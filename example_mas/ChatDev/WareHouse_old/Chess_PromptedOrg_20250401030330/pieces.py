'''
Defines chess pieces and their movement rules, including special moves like castling, en passant, and pawn promotion.
'''
class Piece:
    def __init__(self, color):
        self.color = color
        self.has_moved = False
    def valid_moves(self, board, position):
        raise NotImplementedError("Must be implemented by subclasses")
class Pawn(Piece):
    def valid_moves(self, board, position):
        moves = []
        x, y = position
        direction = -1 if self.color == 'white' else 1
        # Normal move
        if board.is_empty((x + direction, y)):
            moves.append((x + direction, y))
            if (self.color == 'white' and x == 6) or (self.color == 'black' and x == 1):
                if board.is_empty((x + 2 * direction, y)):
                    moves.append((x + 2 * direction, y))
        # Capture moves
        for dy in [-1, 1]:
            if board.is_enemy((x + direction, y + dy), self.color):
                moves.append((x + direction, y + dy))
        # En passant
        if board.en_passant_target:
            ep_x, ep_y = board.en_passant_target
            if abs(ep_y - y) == 1 and ep_x == x + direction:
                moves.append((ep_x, ep_y))
        return moves
class Rook(Piece):
    def valid_moves(self, board, position):
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        for dx, dy in directions:
            x, y = position
            while True:
                x += dx
                y += dy
                if not board.in_bounds((x,y)):
                    break
                if board.is_empty((x,y)):
                    moves.append((x,y))
                elif board.is_enemy((x,y), self.color):
                    moves.append((x,y))
                    break
                else:
                    break
        return moves
class Knight(Piece):
    def valid_moves(self, board, position):
        moves = []
        x, y = position
        offsets = [(2,1),(1,2),(-1,2),(-2,1),(-2,-1),(-1,-2),(1,-2),(2,-1)]
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if board.in_bounds((nx,ny)) and (board.is_empty((nx,ny)) or board.is_enemy((nx,ny), self.color)):
                moves.append((nx,ny))
        return moves
class Bishop(Piece):
    def valid_moves(self, board, position):
        moves = []
        directions = [(1,1),(-1,1),(-1,-1),(1,-1)]
        for dx, dy in directions:
            x, y = position
            while True:
                x += dx
                y += dy
                if not board.in_bounds((x,y)):
                    break
                if board.is_empty((x,y)):
                    moves.append((x,y))
                elif board.is_enemy((x,y), self.color):
                    moves.append((x,y))
                    break
                else:
                    break
        return moves
class Queen(Piece):
    def valid_moves(self, board, position):
        return Rook(self.color).valid_moves(board, position) + Bishop(self.color).valid_moves(board, position)
class King(Piece):
    def valid_moves(self, board, position):
        moves = []
        x, y = position
        offsets = [(1,0),(-1,0),(0,1),(0,-1),(1,1),(-1,1),(-1,-1),(1,-1)]
        for dx, dy in offsets:
            nx, ny = x + dx, y + dy
            if board.in_bounds((nx,ny)) and (board.is_empty((nx,ny)) or board.is_enemy((nx,ny), self.color)):
                moves.append((nx,ny))
        # Castling
        if not self.has_moved and not board.is_in_check(self.color):
            for rook_y in [0, 7]:
                rook = board.board[x][rook_y]
                if isinstance(rook, Rook) and not rook.has_moved:
                    step = 1 if rook_y > y else -1
                    clear = all(board.is_empty((x, y + step*i)) for i in range(1, abs(rook_y - y)))
                    if clear and not board.would_be_in_check(position, (x, y + step), self.color):
                        moves.append((x, y + 2*step))
        return moves