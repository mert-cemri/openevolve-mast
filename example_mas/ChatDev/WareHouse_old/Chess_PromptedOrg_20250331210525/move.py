'''
Defines the Move class to represent chess moves.
'''
class Move:
    def __init__(self, start_pos, end_pos, player, promotion=None):
        self.start_row, self.start_col = start_pos
        self.end_row, self.end_col = end_pos
        self.player = player
        self.promotion = promotion