'''
GameEngine class to manage the game loop and process player commands.
'''
from player import Player
from room import Room
class GameEngine:
    def __init__(self, game_data):
        self.rooms = {room_data['name']: Room(**room_data) for room_data in game_data['rooms']}
        self.player = Player(self.rooms[game_data['start_room']])
    def start(self):
        print("Welcome to the Adventure Game!")
        while True:
            print(self.player.current_room.description)
            command = input("> ").strip().lower()
            if command in ["quit", "exit"]:
                print("Thanks for playing!")
                break
            self.process_command(command)
    def process_command(self, command):
        if command.startswith("go "):
            direction = command.split(" ", 1)[1]
            self.player.move(direction, self.rooms)
        elif command.startswith("take "):
            item_name = command.split(" ", 1)[1]
            self.player.take_item(item_name)
        elif command.startswith("inventory"):
            self.player.show_inventory()
        else:
            print("Unknown command.")