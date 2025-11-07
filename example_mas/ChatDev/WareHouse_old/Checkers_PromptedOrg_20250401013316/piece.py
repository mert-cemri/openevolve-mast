'''
Piece class representing a Checkers game piece.
'''
class Piece:
    def __init__(self, player):
        self.player = player  # 'W' for white, 'B' for black
        self.king = False
    def __str__(self):
        if self.king:
            return self.player.upper()
        return self.player.lower()