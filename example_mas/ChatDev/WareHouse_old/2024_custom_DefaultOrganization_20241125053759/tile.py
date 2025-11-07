'''
Tile class representing a single tile in the 2048 game.
'''
class Tile:
    def __init__(self, value):
        self.value = value
    def merge(self, other):
        if self.value == other.value:
            self.value *= 2
            return True
        return False