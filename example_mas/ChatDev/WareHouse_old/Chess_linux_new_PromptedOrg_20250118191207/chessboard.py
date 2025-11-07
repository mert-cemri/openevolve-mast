'''
Defines the ChessBoard class to manage the state of the chessboard.
'''
class ChessBoard:
    def __init__(self):
        self.board = self.initialize_board()
    def initialize_board(self):
        # Initialize the board with pieces in starting positions
        board = [[' ' for _ in range(8)] for _ in range(8)]
        # Add pieces to the board (simplified for brevity)
        board[0] = ['R', 'N', 'B', 'Q', 'K', 'B', 'N', 'R']
        board[1] = ['P'] * 8
        board[6] = ['p'] * 8
        board[7] = ['r', 'n', 'b', 'q', 'k', 'b', 'n', 'r']
        return board
    def display_board(self):
        for row in self.board:
            print(' '.join(row))
        print()
    def move_piece(self, start, end):
        piece = self.board[start[0]][start[1]]
        self.board[start[0]][start[1]] = ' '
        self.board[end[0]][end[1]] = piece
    def is_occupied_by_same_color(self, start, end):
        start_piece = self.board[start[0]][start[1]]
        end_piece = self.board[end[0]][end[1]]
        if start_piece.isupper() and end_piece.isupper():
            return True
        if start_piece.islower() and end_piece.islower():
            return True
        return False