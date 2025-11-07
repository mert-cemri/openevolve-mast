'''
GameEngine class that manages the overall game state and flow.
This class handles the game loop, player movement, item collection, and command parsing.
'''
from room import Room
from player import Player
from command_parser import CommandParser
class GameEngine:
    def __init__(self, game_data):
        self.rooms = {room['name']: Room(room) for room in game_data['rooms']}
        self.player = Player(starting_room=game_data['start_room'])
        self.command_parser = CommandParser(self)
    def start(self):
        print("Welcome to the Adventure Game!")
        print("Type 'help' to see a list of commands.")
        while True:
            current_room = self.rooms[self.player.current_room]
            print(current_room.description)
            command = input("> ").strip().lower()
            if command == 'quit':
                print("Thanks for playing!")
                break
            self.command_parser.parse(command)
    def move_player(self, direction):
        current_room = self.rooms[self.player.current_room]
        if direction in current_room.choices:
            self.player.current_room = current_room.choices[direction]
            print(f"You move to the {self.player.current_room}.")
        else:
            print("You can't go that way.")
    def pick_up_item(self, item_name):
        current_room = self.rooms[self.player.current_room]
        if item_name in current_room.items:
            self.player.inventory.append(item_name)
            current_room.items.remove(item_name)
            print(f"You pick up the {item_name}.")
        else:
            print(f"There is no {item_name} here.")
    def show_help(self):
        print("Available commands:")
        print("  go <direction> - Move in a direction (north, south, east, west)")
        print("  take <item> - Pick up an item")
        print("  quit - Exit the game")
        print("  help - Show this help message")