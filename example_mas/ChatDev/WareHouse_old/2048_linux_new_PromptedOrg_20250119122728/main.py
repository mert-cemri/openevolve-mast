'''
This file contains the implementation of a simple 2048 game that can be played in the Linux Terminal. The game is text-based and uses a 4x4 grid. The player can input commands to move the tiles up, down, left, or right. The game ends when no more moves are possible.
'''
import random
class Game2048:
    def __init__(self):
        self.grid_size = 4
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0
        self.reset_game()
    def reset_game(self):
        self.grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        self.score = 0
        self.add_new_tile()
        self.add_new_tile()
    def add_new_tile(self):
        empty_cells = [(i, j) for i in range(self.grid_size) for j in range(self.grid_size) if self.grid[i][j] == 0]
        if empty_cells:
            i, j = random.choice(empty_cells)
            self.grid[i][j] = random.choice([2, 4])
    def compress(self, grid):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            pos = 0
            for j in range(self.grid_size):
                if grid[i][j] != 0:
                    new_grid[i][pos] = grid[i][j]
                    pos += 1
        return new_grid
    def merge(self, grid):
        for i in range(self.grid_size):
            for j in range(self.grid_size - 1):
                if grid[i][j] == grid[i][j + 1] and grid[i][j] != 0:
                    grid[i][j] *= 2
                    grid[i][j + 1] = 0
                    self.score += grid[i][j]
        return grid
    def move(self, direction):
        original_grid = [row[:] for row in self.grid]  # Copy the current grid
        if direction == 'w':
            self.grid = self.transpose(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.merge(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.transpose(self.grid)
        elif direction == 's':
            self.grid = self.transpose(self.grid)
            self.grid = self.reverse(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.merge(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.reverse(self.grid)
            self.grid = self.transpose(self.grid)
        elif direction == 'a':
            self.grid = self.compress(self.grid)
            self.grid = self.merge(self.grid)
            self.grid = self.compress(self.grid)
        elif direction == 'd':
            self.grid = self.reverse(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.merge(self.grid)
            self.grid = self.compress(self.grid)
            self.grid = self.reverse(self.grid)
        else:
            return False
        if self.grid != original_grid:  # Only add a new tile if the grid has changed
            self.add_new_tile()
            return True
        return False
    def reverse(self, grid):
        new_grid = []
        for i in range(self.grid_size):
            new_grid.append(list(reversed(grid[i])))
        return new_grid
    def transpose(self, grid):
        new_grid = [[0] * self.grid_size for _ in range(self.grid_size)]
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                new_grid[i][j] = grid[j][i]
        return new_grid
    def can_move(self):
        for i in range(self.grid_size):
            for j in range(self.grid_size):
                if self.grid[i][j] == 0:
                    return True
                if j < self.grid_size - 1 and self.grid[i][j] == self.grid[i][j + 1]:
                    return True
                if i < self.grid_size - 1 and self.grid[i][j] == self.grid[i + 1][j]:
                    return True
        return False
    def is_game_over(self):
        return not self.can_move()
    def print_grid(self):
        for row in self.grid:
            print('+----' * self.grid_size + '+')
            print(''.join(f'|{str(num).center(4)}' if num != 0 else '|    ' for num in row) + '|')
        print('+----' * self.grid_size + '+')
        print(f'Score: {self.score}')
def main():
    game = Game2048()
    game.print_grid()
    while not game.is_game_over():
        move = input("Enter move (w/a/s/d): ").strip().lower()
        if move in ['w', 'a', 's', 'd']:
            if game.move(move):
                game.print_grid()
            else:
                print("Invalid move! Please try again.")
        else:
            print("Invalid input! Please enter 'w', 'a', 's', or 'd'.")
    print("Game Over! Your final score is:", game.score)
if __name__ == "__main__":
    main()