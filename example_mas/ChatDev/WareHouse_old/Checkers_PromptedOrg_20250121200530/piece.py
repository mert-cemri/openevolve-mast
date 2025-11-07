'''
Represents a single piece on the board.
'''
class Piece:
    def __init__(self, color):
        self.is_king = False
        self.color = color