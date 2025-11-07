'''
Game engine to manage the game loop and player interactions.
'''
from game_data_loader import GameDataLoader
from player import Player
from cli import CLI
class GameEngine:
    def __init__(self):
        self.rooms = {}
        self.player = Player()
        self.cli = CLI()
    def load_game_data(self, file_path):
        self.rooms = GameDataLoader.load(file_path)
    def start_game(self):
        self.cli.display_message("Welcome to the Adventure Game!")
        self.player.current_room = self.rooms.get('start')
        while True:
            self.cli.display_message(self.player.current_room.description)
            command = self.cli.get_command()
            self.process_command(command)
    def process_command(self, command):
        if command in self.player.current_room.choices:
            self.player.current_room = self.rooms.get(self.player.current_room.choices[command])
        else:
            available_commands = ', '.join(self.player.current_room.choices.keys())
            self.cli.display_message(f"Invalid command. Available commands are: {available_commands}. Try again.")