'''
Game class to manage the game state and logic for the 2048 game.
'''
from grid import Grid
class Game:
    def __init__(self):
        self.grid = Grid()
        self.score = 0
    def start(self):
        self.grid.add_random_tile()
        self.grid.add_random_tile()
        self.display()
        while not self.grid.is_game_over():
            move = input("Enter move (w/a/s/d): ").strip().lower()
            if move in ['w', 'a', 's', 'd']:
                moved, score = self.grid.move(move)
                if moved:
                    self.score += score
                    self.grid.add_random_tile()
                    self.display()
                else:
                    print("Invalid move. Try again.")
            else:
                print("Invalid input. Use 'w', 'a', 's', 'd' to move.")
    def display(self):
        print(f"Score: {self.score}")
        self.grid.display()