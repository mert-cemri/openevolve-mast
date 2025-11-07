'''
Game class to manage the game loop, player input, and game state transitions.
'''
from player import Player
from map import Map
from ui import UI
class Game:
    def __init__(self):
        self.map = Map()
        self.player = Player(self.map.start_position)
        self.ui = UI(self.player)
    def run(self):
        while not self.map.is_exit_reached(self.player.position):
            self.ui.display()
            move = input("Enter move (W/A/S/D): ").strip().upper()
            if move in ['W', 'A', 'S', 'D']:
                self.player.move(move, self.map)
                self.map.check_encounters(self.player)
            else:
                print("Invalid input. Use W/A/S/D to move.")
        print("Congratulations! You've reached the exit.")