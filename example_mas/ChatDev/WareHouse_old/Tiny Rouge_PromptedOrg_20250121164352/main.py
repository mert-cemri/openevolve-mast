'''
Main game file to initialize and run the game loop.
'''
from player import Player
from game_map import Map
class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player(self.map.start_position)
        self.is_running = True
    def start_game(self):
        self.map.generate_map()
        while self.is_running:
            self.render()
            self.process_input()
            self.update_game_state()
    def process_input(self):
        command = input("Enter command (W/A/S/D): ").upper()
        if command in ['W', 'A', 'S', 'D']:
            self.player.move(command, self.map)
    def update_game_state(self):
        obj = self.map.get_object_at(self.player.position)
        if obj:
            self.player.interact_with_object(obj)
    def render(self):
        self.map.display(self.player.position)
if __name__ == "__main__":
    game = Game()
    game.start_game()