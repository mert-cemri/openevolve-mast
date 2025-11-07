'''
Player class to represent the player in the game.
'''
class Player:
    def __init__(self, start_room):
        self.current_room = start_room
        self.inventory = []
    def move(self, direction, rooms):
        if direction in self.current_room.exits:
            self.current_room = rooms[self.current_room.exits[direction]]
            print(f"You move to the {self.current_room.name}.")
        else:
            print("You can't go that way.")
    def take_item(self, item_name):
        item = self.current_room.remove_item(item_name)
        if item:
            self.inventory.append(item)
            print(f"You take the {item.name}.")
        else:
            print("There is no such item here.")
    def show_inventory(self):
        if self.inventory:
            print("You have the following items:")
            for item in self.inventory:
                print(f"- {item.name}: {item.description}")
        else:
            print("Your inventory is empty.")