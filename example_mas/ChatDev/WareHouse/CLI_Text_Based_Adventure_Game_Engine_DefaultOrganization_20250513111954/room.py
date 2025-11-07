'''
Represents a room in the game.
'''
class Room:
    def __init__(self, name, description, items, choices):
        self.name = name
        self.description = description
        self.items = items
        self.choices = choices