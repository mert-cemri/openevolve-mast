'''
CommandParser class that parses and executes player commands.
This class interprets the player's input and calls the appropriate methods in the GameEngine.
'''
class CommandParser:
    def __init__(self, game_engine):
        self.game_engine = game_engine
        self.commands = {
            'go': self.game_engine.move_player,
            'take': self.game_engine.pick_up_item,
            'help': self.game_engine.show_help,
        }
    def parse(self, command):
        parts = command.split()
        if not parts:
            print("Invalid command.")
            return
        action = parts[0]
        if action in self.commands:
            if len(parts) > 1:
                self.commands[action](parts[1])
            else:
                self.commands[action]()
        else:
            print("Unknown command.")