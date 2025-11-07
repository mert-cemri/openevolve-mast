'''
Defines the Piece class representing individual checker pieces.
'''
class Piece:
    def __init__(self, color, king=False):
        self.color = color  # 'W' for white, 'B' for black
        self.king = king
    def make_king(self):
        self.king = True
    def __repr__(self):
        if self.king:
            return self.color + 'K'
        return self.color