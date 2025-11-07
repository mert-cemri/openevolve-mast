'''
Defines the Piece class representing a checkers piece.
'''
class Piece:
    def __init__(self, color):
        self.color = color
        self.is_king = False