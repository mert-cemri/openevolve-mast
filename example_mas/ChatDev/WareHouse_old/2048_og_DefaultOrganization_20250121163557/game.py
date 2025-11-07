'''
Game logic for the 2048 game, including state management and tile operations.
'''
import random
from grid import Grid
class Game:
    def __init__(self):
        self.grid = Grid()
        self.score = 0
        self.reset_game()
    def reset_game(self):
        self.grid.reset()
        self.add_random_tile()
        self.add_random_tile()
    def move(self, direction):
        if self.grid.move(direction, self):
            self.add_random_tile()
        if self.is_game_over():
            print("Game Over!")
    def add_random_tile(self):
        empty_cells = self.grid.get_empty_cells()
        if empty_cells:
            row, col = random.choice(empty_cells)
            self.grid.set_tile(row, col, 2 if random.random() < 0.9 else 4)
    def is_game_over(self):
        return not self.grid.can_move()