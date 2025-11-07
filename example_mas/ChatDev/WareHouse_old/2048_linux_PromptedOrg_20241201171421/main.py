'''
This is the main file for the 2048 game. It initializes the game and manages the game loop.
'''
import random
class Game2048:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()
    def spawn_tile(self):
        empty_cells = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if not empty_cells:
            return
        i, j = random.choice(empty_cells)
        self.grid[i][j] = 2 if random.random() < 0.9 else 4
    def move(self, direction):
        def compress(row):
            new_row = [i for i in row if i != 0]
            new_row += [0] * (4 - len(new_row))
            return new_row
        def merge(row):
            for i in range(3):
                if row[i] == row[i + 1] and row[i] != 0:
                    row[i] *= 2
                    row[i + 1] = 0
                    self.score += row[i]
            return row
        def move_left(grid):
            new_grid = []
            for row in grid:
                new_row = compress(row)
                new_row = merge(new_row)
                new_row = compress(new_row)
                new_grid.append(new_row)
            return new_grid
        def rotate_90_clockwise(grid):
            return [list(row) for row in zip(*grid[::-1])]
        moves = {
            'w': lambda grid: rotate_90_clockwise(move_left(rotate_90_clockwise(rotate_90_clockwise(grid)))),
            's': lambda grid: rotate_90_clockwise(rotate_90_clockwise(rotate_90_clockwise(move_left(rotate_90_clockwise(grid))))),
            'a': move_left,
            'd': lambda grid: rotate_90_clockwise(rotate_90_clockwise(move_left(rotate_90_clockwise(rotate_90_clockwise(grid)))))
        }
        if direction in moves:
            new_grid = moves[direction](self.grid)
            if new_grid != self.grid:
                self.grid = new_grid
                self.spawn_tile()
    def is_game_over(self):
        if any(0 in row for row in self.grid):
            return False
        for i in range(4):
            for j in range(4):
                if i < 3 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j < 3 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True
    def print_grid(self):
        for row in self.grid:
            print('+----' * 4 + '+')
            print(''.join(f'|{num:^4}' if num != 0 else '|    ' for num in row) + '|')
        print('+----' * 4 + '+')
        print(f'Score: {self.score}\n')
def get_user_input():
    valid_inputs = ['w', 'a', 's', 'd']
    while True:
        user_input = input("Enter move (w/a/s/d): ").strip().lower()
        if user_input in valid_inputs:
            return user_input
        print("Invalid input. Please enter 'w', 'a', 's', or 'd'.")
def play_game():
    game = Game2048()
    while not game.is_game_over():
        game.print_grid()
        move = get_user_input()
        game.move(move)
    game.print_grid()
    print("Game Over!")
if __name__ == "__main__":
    play_game()