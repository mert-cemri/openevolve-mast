'''
This module implements a simple 2048 game playable from the Linux Terminal.
'''
import random
import os
class Game2048:
    def __init__(self):
        self.grid = [[0] * 4 for _ in range(4)]
        self.score = 0
        self.spawn_tile()
        self.spawn_tile()
    def spawn_tile(self):
        empty_tiles = [(i, j) for i in range(4) for j in range(4) if self.grid[i][j] == 0]
        if empty_tiles:
            i, j = random.choice(empty_tiles)
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
        def rotate(grid):
            return [list(row) for row in zip(*grid[::-1])]
        if direction == 'w':
            self.grid = rotate(rotate(rotate(move_left(rotate(self.grid)))))
        elif direction == 's':
            self.grid = rotate(move_left(rotate(rotate(rotate(self.grid)))))
        elif direction == 'a':
            self.grid = move_left(self.grid)
        elif direction == 'd':
            self.grid = rotate(rotate(move_left(rotate(rotate(self.grid)))))
        self.spawn_tile()
    def is_game_over(self):
        for i in range(4):
            for j in range(4):
                if self.grid[i][j] == 0:
                    return False
                if i < 3 and self.grid[i][j] == self.grid[i + 1][j]:
                    return False
                if j < 3 and self.grid[i][j] == self.grid[i][j + 1]:
                    return False
        return True
    def print_grid(self):
        os.system('clear')
        print(f"Score: {self.score}")
        for row in self.grid:
            print('+----' * 4 + '+')
            print(''.join(f'|{str(num).center(4)}' if num != 0 else '|    ' for num in row) + '|')
        print('+----' * 4 + '+')
def main():
    game = Game2048()
    while not game.is_game_over():
        game.print_grid()
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            game.move(move)
        else:
            print("Invalid move! Please enter 'w', 'a', 's', or 'd'.")
    game.print_grid()
    print("Game Over!")
if __name__ == "__main__":
    main()