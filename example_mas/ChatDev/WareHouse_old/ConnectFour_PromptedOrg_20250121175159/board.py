'''
This module contains the Board class, which represents the Connect Four board and handles disc placement and win condition checks.
'''
class Board:
    ROWS = 6
    COLUMNS = 7
    def __init__(self):
        self.grid = [[" " for _ in range(self.COLUMNS)] for _ in range(self.ROWS)]
    def display(self):
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(str(i) for i in range(self.COLUMNS)))
    def place_disc(self, column, symbol):
        for row in reversed(self.grid):
            if row[column] == " ":
                row[column] = symbol
                return True
        return False
    def check_winner(self, symbol):
        # Check horizontal
        for row in self.grid:
            for col in range(self.COLUMNS - 3):
                if all(row[col + i] == symbol for i in range(4)):
                    return True
        # Check vertical
        for col in range(self.COLUMNS):
            for row in range(self.ROWS - 3):
                if all(self.grid[row + i][col] == symbol for i in range(4)):
                    return True
        # Check diagonal (positive slope)
        for row in range(self.ROWS - 3):
            for col in range(self.COLUMNS - 3):
                if all(self.grid[row + i][col + i] == symbol for i in range(4)):
                    return True
        # Check diagonal (negative slope)
        for row in range(3, self.ROWS):
            for col in range(self.COLUMNS - 3):
                if all(self.grid[row - i][col + i] == symbol for i in range(4)):
                    return True
        return False
    def is_full(self):
        return all(self.grid[0][col] != " " for col in range(self.COLUMNS))