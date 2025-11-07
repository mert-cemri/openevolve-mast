'''
Represents a checkers piece, including its type (normal or king) and color.
'''
class Piece:
    def __init__(self, color):
        self.color = color
        self.is_king = False
        self.symbol = 'W' if color == 'W' else 'B'
    def make_king(self):
        self.is_king = True
        self.symbol = 'WK' if self.color == 'W' else 'BK'