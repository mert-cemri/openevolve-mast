'''
Represents the chessboard and manages the state of the game.
'''
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
    def initialize_board(self):
        # Set up the board with all pieces in their starting positions
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Place pawns
        for i in range(8):
            board[1][i] = Pawn('Black')
            board[6][i] = Pawn('White')
        # Place rooks
        board[0][0] = board[0][7] = Rook('Black')
        board[7][0] = board[7][7] = Rook('White')
        # Place knights
        board[0][1] = board[0][6] = Knight('Black')
        board[7][1] = board[7][6] = Knight('White')
        # Place bishops
        board[0][2] = board[0][5] = Bishop('Black')
        board[7][2] = board[7][5] = Bishop('White')
        # Place queens
        board[0][3] = Queen('Black')
        board[7][3] = Queen('White')
        # Place kings
        board[0][4] = King('Black')
        board[7][4] = King('White')
        return board
    def display(self):
        for row in self.board:
            print(' '.join(str(piece) if piece != ' ' else '.' for piece in row))
        print()
    def move_piece(self, start, end, player):
        start_x, start_y = self.convert_position(start)
        end_x, end_y = self.convert_position(end)
        piece = self.board[start_x][start_y]
        if piece != ' ' and piece.color == player and piece.is_valid_move(start, end, self.board):
            self.board[end_x][end_y] = piece
            self.board[start_x][start_y] = ' '
            return True
        return False
    def convert_position(self, pos):
        col, row = pos
        return 8 - int(row), ord(col) - ord('a')
    def is_checkmate(self, player):
        # Find the king's position
        king_position = None
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if isinstance(piece, King) and piece.color == player:
                    king_position = (x, y)
                    break
            if king_position:
                break
        # Check if the king is in check
        if not self.is_in_check(king_position, player):
            return False
        # Check for any legal moves to escape check
        for x in range(8):
            for y in range(8):
                piece = self.board[x][y]
                if piece != ' ' and piece.color == player:
                    for dx in range(-1, 2):
                        for dy in range(-1, 2):
                            if dx != 0 or dy != 0:
                                new_x, new_y = x + dx, y + dy
                                if 0 <= new_x < 8 and 0 <= new_y < 8:
                                    if self.move_piece((x, y), (new_x, new_y), player):
                                        # Undo the move
                                        self.board[x][y], self.board[new_x][new_y] = self.board[new_x][new_y], self.board[x][y]
                                        return False
        return True
    def is_in_check(self, king_position, player):
        # Implement logic to determine if the king is in check
        # This involves checking if any opponent piece can move to the king's position
        return False