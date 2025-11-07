'''
Board class representing the game board.
'''
from property import Property
class Board:
    def __init__(self):
        self.properties = []
    def setup_board(self):
        # Initialize properties (simplified example)
        self.properties = [Property("Mediterranean Avenue", 60, 2),
                           Property("Baltic Avenue", 60, 4)]
        # Add more properties and chance cards as needed
    def get_property(self, position):
        return self.properties[position % len(self.properties)]