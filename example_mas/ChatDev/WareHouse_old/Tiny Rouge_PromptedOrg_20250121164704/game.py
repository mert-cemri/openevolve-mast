'''
Game class to manage the overall game state and loop.
'''
from map import Map
from player import Player
class Game:
    def __init__(self):
        self.map = Map(80, 80)
        self.player = Player(self.map.start_position)
        self.is_running = True
    def run(self):
        while self.is_running:
            self.map.display(self.player.position)
            command = input("Enter command (W/A/S/D): ").strip().upper()
            if command in ['W', 'A', 'S', 'D']:
                self.player.move(command, self.map)
                if self.map.is_door(self.player.position):
                    print("You've reached the door! Moving to the next level.")
                    self.is_running = False
                elif self.map.is_monster(self.player.position):
                    self.player.fight(self.map.get_monster(self.player.position))
                elif self.map.is_treasure(self.player.position):
                    self.player.collect_treasure(self.map.get_treasure(self.player.position))
            else:
                print("Invalid command.")