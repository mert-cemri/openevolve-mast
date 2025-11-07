'''
Game class to manage the 2048 game logic.
'''
from grid import Grid
class Game:
    def __init__(self):
        self.grid = Grid()
        self.won = False
    def reset(self):
        self.grid = Grid()
        self.grid.add_random_tile()
        self.grid.add_random_tile()
    def move(self, direction):
        if self.grid.can_move(direction):
            previous_grid = str(self.grid)  # Capture the grid state before the move
            self.grid.move(direction)
            if str(self.grid) != previous_grid:  # Check if the grid state has changed
                self.grid.add_random_tile()
            if self.grid.has_2048():
                self.won = True
    def is_game_over(self):
        return not self.grid.can_move_any() and not self.won
    def is_won(self):
        return self.won
    def __str__(self):
        return str(self.grid)