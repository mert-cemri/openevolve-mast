'''
Game class to manage the game state and loop.
'''
from map import Map
from player import Player
class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player(self.map.start_position)
    def run(self):
        while not self.map.is_level_complete(self.player.position):
            self.map.display(self.player.position)
            command = input("Enter command (W/A/S/D): ").upper()
            if command in ['W', 'A', 'S', 'D']:
                self.player.move(command, self.map)
            else:
                print("Invalid command!")
        print("Level Complete! Proceeding to next level...")
        self.next_level()
    def next_level(self):
        # Logic for proceeding to the next level
        self.map = Map()  # Reset the map for a new level
        self.player.position = self.map.start_position  # Reset player position