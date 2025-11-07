'''
Board class to represent the game board, handle disc placements, and provide methods to check for a win or draw.
'''
class Board:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = [[' ' for _ in range(self.columns)] for _ in range(self.rows)]
    def display(self):
        for row in self.grid:
            print('|'.join(row))
            print('-' * (self.columns * 2 - 1))
    def place_disc(self, column, disc):
        if column < 0 or column >= self.columns or self.grid[0][column] != ' ':
            return False
        for row in reversed(self.grid):
            if row[column] == ' ':
                row[column] = disc
                return True
        return False
    def check_winner(self, disc):
        # Check horizontal, vertical, and diagonal lines for a win
        return (self.check_horizontal(disc) or
                self.check_vertical(disc) or
                self.check_diagonal(disc))
    def check_horizontal(self, disc):
        for row in self.grid:
            for col in range(self.columns - 3):
                if all(row[col + i] == disc for i in range(4)):
                    return True
        return False
    def check_vertical(self, disc):
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == disc for i in range(4)):
                    return True
        return False
    def check_diagonal(self, disc):
        # Check for diagonals with positive slope
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == disc for i in range(4)):
                    return True
        # Check for diagonals with negative slope
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row - i][col + i] == disc for i in range(4)):
                    return True
        return False
    def is_draw(self):
        return all(self.grid[0][col] != ' ' for col in range(self.columns))