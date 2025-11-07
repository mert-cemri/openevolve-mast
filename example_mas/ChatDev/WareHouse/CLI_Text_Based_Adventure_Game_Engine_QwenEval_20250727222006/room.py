'''
Room class that represents a room in the game with descriptions, items, and choices.
This class stores information about each room, including its name, description, items, and possible exits.
'''
class Room:
    def __init__(self, data):
        self.name = data['name']
        self.description = data['description']
        self.items = data.get('items', [])
        self.choices = data.get('choices', {})