'''
Player class to represent a player in the Gomoku game.
'''
class Player:
    def __init__(self, stone):
        '''
        Initialize a player with a specific stone ('B' for black or 'W' for white).
        '''
        self.stone = stone