'''
Defines the ChessBoard class, which manages the state of the chessboard.
'''
from piece import Piece, Pawn, Rook, Knight, Bishop, Queen, King
class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
        self.current_player = 'white'
    def initialize_board(self):
        # Initialize the board with pieces in starting positions
        board = [[None for _ in range(8)] for _ in range(8)]
        # Place pieces on the board
        for i in range(8):
            board[1][i] = Pawn('black')
            board[6][i] = Pawn('white')
        # Rooks
        board[0][0] = Rook('black')
        board[0][7] = Rook('black')
        board[7][0] = Rook('white')
        board[7][7] = Rook('white')
        # Knights
        board[0][1] = Knight('black')
        board[0][6] = Knight('black')
        board[7][1] = Knight('white')
        board[7][6] = Knight('white')
        # Bishops
        board[0][2] = Bishop('black')
        board[0][5] = Bishop('black')
        board[7][2] = Bishop('white')
        board[7][5] = Bishop('white')
        # Queens
        board[0][3] = Queen('black')
        board[7][3] = Queen('white')
        # Kings
        board[0][4] = King('black')
        board[7][4] = King('white')
        return board
    def display(self):
        # Print the board state
        for row in self.board:
            print(' '.join([str(piece) if piece else '.' for piece in row]))
    def move_piece(self, move):
        # Validate and execute a move
        try:
            start_pos, end_pos = self.parse_move(move)
            piece = self.get_piece_at(start_pos)
            if piece and piece.color == self.current_player and end_pos in piece.valid_moves(start_pos, self.board):
                self.set_piece_at(end_pos, piece)
                self.set_piece_at(start_pos, None)
                return True
        except Exception as e:
            print(f"Error processing move: {e}")
        return False
    def parse_move(self, move):
        # Parse the move in algebraic notation
        start_pos = (8 - int(move[1]), ord(move[0]) - ord('a'))
        end_pos = (8 - int(move[3]), ord(move[2]) - ord('a'))
        return start_pos, end_pos
    def get_piece_at(self, position):
        return self.board[position[0]][position[1]]
    def set_piece_at(self, position, piece):
        self.board[position[0]][position[1]] = piece
    def is_in_check(self, color):
        # Determine if the player's king is in check
        king_position = None
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and isinstance(piece, King) and piece.color == color:
                    king_position = (i, j)
                    break
        if not king_position:
            return False
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color != color:
                    if king_position in piece.valid_moves((i, j), self.board):
                        return True
        return False
    def is_checkmate(self, color):
        # Check if the player of the given color is in checkmate
        if not self.is_in_check(color):
            return False
        for i in range(8):
            for j in range(8):
                piece = self.board[i][j]
                if piece and piece.color == color:
                    for move in piece.valid_moves((i, j), self.board):
                        original_piece = self.get_piece_at(move)
                        self.set_piece_at(move, piece)
                        self.set_piece_at((i, j), None)
                        if not self.is_in_check(color):
                            self.set_piece_at((i, j), piece)
                            self.set_piece_at(move, original_piece)
                            return False
                        self.set_piece_at((i, j), piece)
                        self.set_piece_at(move, original_piece)
        return True