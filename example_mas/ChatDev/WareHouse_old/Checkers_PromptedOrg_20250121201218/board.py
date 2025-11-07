'''
Board class to represent the game board.
'''
from piece import Piece
class Board:
    def __init__(self):
        self.grid = [[None for _ in range(8)] for _ in range(8)]
        self.setup_pieces()
    def setup_pieces(self):
        # Initialize pieces on the board for both players
        for y in range(3):
            for x in range(8):
                if (x + y) % 2 == 1:
                    self.grid[y][x] = Piece('B')
        for y in range(5, 8):
            for x in range(8):
                if (x + y) % 2 == 1:
                    self.grid[y][x] = Piece('W')
    def display(self):
        # Display the board
        for y in range(8):
            row = ''
            for x in range(8):
                piece = self.grid[y][x]
                if piece is None:
                    row += '. '
                else:
                    row += ('B ' if piece.color == 'B' else 'W ')
            print(row)
        print()
    def update_position(self, pos, piece):
        x, y = pos
        self.grid[y][x] = piece
    def get_piece(self, pos):
        x, y = pos
        return self.grid[y][x]