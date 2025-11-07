'''
Room class to represent each room in the game.
'''
from item import Item
class Room:
    def __init__(self, name, description, items, exits):
        self.name = name
        self.description = description
        self.items = [Item(**item_data) for item_data in items]
        self.exits = exits
    def remove_item(self, item_name):
        for item in self.items:
            if item.name == item_name:
                self.items.remove(item)
                return item
        return None