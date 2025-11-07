'''
Player class that represents the player's state and actions.
This class keeps track of the player's current location and inventory.
'''
class Player:
    def __init__(self, starting_room):
        self.current_room = starting_room
        self.inventory = []