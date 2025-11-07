'''
Board class to represent the game board and manage spaces.
'''
from property import Property
from chance import Chance
class Board:
    def __init__(self):
        self.spaces = [Property("Park Place", 350, 35), Chance(), Property("Boardwalk", 400, 50)]
    def get_space_info(self, position):
        return self.spaces[position]
    def get_property_owner(self, position):
        space = self.spaces[position]
        if isinstance(space, Property):
            return space.owner
        return None