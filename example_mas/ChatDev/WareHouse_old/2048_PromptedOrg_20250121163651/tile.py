'''
Tile class to represent individual tiles in the 2048 game.
'''
class Tile:
    def __init__(self, value=2):
        self.value = value
    def __str__(self):
        return str(self.value)