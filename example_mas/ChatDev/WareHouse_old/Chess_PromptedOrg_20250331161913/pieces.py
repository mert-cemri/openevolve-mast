'''
Pieces module to define chess pieces and their movements.
'''
class Piece:
    def __init__(self, color):
        self.color = color
    def get_legal_moves(self, position, board):
        raise NotImplementedError
    def __str__(self):
        return self.__class__.__name__[0]
class Pawn(Piece):
    def get_legal_moves(self, position, board):
        moves = []
        direction = -1 if self.color == 'White' else 1
        start_row = 6 if self.color == 'White' else 1
        # Move forward
        forward_pos = (position[0] + direction, position[1])
        if self.is_in_bounds(forward_pos) and board[forward_pos[0]][forward_pos[1]] is None:
            moves.append(forward_pos)
            # Double move from starting position
            if position[0] == start_row:
                double_forward_pos = (position[0] + 2 * direction, position[1])
                if board[double_forward_pos[0]][double_forward_pos[1]] is None:
                    moves.append(double_forward_pos)
        # Captures
        for dx in [-1, 1]:
            capture_pos = (position[0] + direction, position[1] + dx)
            if self.is_in_bounds(capture_pos) and board[capture_pos[0]][capture_pos[1]] is not None:
                if board[capture_pos[0]][capture_pos[1]].color != self.color:
                    moves.append(capture_pos)
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
class Rook(Piece):
    def get_legal_moves(self, position, board):
        return self.get_straight_line_moves(position, board)
    def get_straight_line_moves(self, position, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            moves.extend(self.get_moves_in_direction(position, direction, board))
        return moves
    def get_moves_in_direction(self, position, direction, board):
        moves = []
        current_pos = (position[0] + direction[0], position[1] + direction[1])
        while self.is_in_bounds(current_pos):
            if board[current_pos[0]][current_pos[1]] is None:
                moves.append(current_pos)
            elif board[current_pos[0]][current_pos[1]].color != self.color:
                moves.append(current_pos)
                break
            else:
                break
            current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
class Knight(Piece):
    def get_legal_moves(self, position, board):
        moves = []
        knight_moves = [
            (2, 1), (2, -1), (-2, 1), (-2, -1),
            (1, 2), (1, -2), (-1, 2), (-1, -2)
        ]
        for move in knight_moves:
            new_pos = (position[0] + move[0], position[1] + move[1])
            if self.is_in_bounds(new_pos):
                if board[new_pos[0]][new_pos[1]] is None or board[new_pos[0]][new_pos[1]].color != self.color:
                    moves.append(new_pos)
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
class Bishop(Piece):
    def get_legal_moves(self, position, board):
        return self.get_diagonal_moves(position, board)
    def get_diagonal_moves(self, position, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            moves.extend(self.get_moves_in_direction(position, direction, board))
        return moves
    def get_moves_in_direction(self, position, direction, board):
        moves = []
        current_pos = (position[0] + direction[0], position[1] + direction[1])
        while self.is_in_bounds(current_pos):
            if board[current_pos[0]][current_pos[1]] is None:
                moves.append(current_pos)
            elif board[current_pos[0]][current_pos[1]].color != self.color:
                moves.append(current_pos)
                break
            else:
                break
            current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
class Queen(Piece):
    def get_legal_moves(self, position, board):
        return self.get_straight_line_moves(position, board) + self.get_diagonal_moves(position, board)
    def get_straight_line_moves(self, position, board):
        moves = []
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        for direction in directions:
            moves.extend(self.get_moves_in_direction(position, direction, board))
        return moves
    def get_diagonal_moves(self, position, board):
        moves = []
        directions = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
        for direction in directions:
            moves.extend(self.get_moves_in_direction(position, direction, board))
        return moves
    def get_moves_in_direction(self, position, direction, board):
        moves = []
        current_pos = (position[0] + direction[0], position[1] + direction[1])
        while self.is_in_bounds(current_pos):
            if board[current_pos[0]][current_pos[1]] is None:
                moves.append(current_pos)
            elif board[current_pos[0]][current_pos[1]].color != self.color:
                moves.append(current_pos)
                break
            else:
                break
            current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8
class King(Piece):
    def get_legal_moves(self, position, board):
        moves = []
        king_moves = [
            (1, 0), (-1, 0), (0, 1), (0, -1),
            (1, 1), (1, -1), (-1, 1), (-1, -1)
        ]
        for move in king_moves:
            new_pos = (position[0] + move[0], position[1] + move[1])
            if self.is_in_bounds(new_pos):
                if board[new_pos[0]][new_pos[1]] is None or board[new_pos[0]][new_pos[1]].color != self.color:
                    moves.append(new_pos)
        return moves
    def is_in_bounds(self, position):
        return 0 <= position[0] < 8 and 0 <= position[1] < 8