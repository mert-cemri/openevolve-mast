'''
Represents individual pieces on the board.
'''
class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position
        self.is_king = False
    def move(self, new_position):
        self.position = new_position
    def king(self):
        self.is_king = True