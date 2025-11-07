'''
Board class to represent and manage the Connect Four game board.
'''
class Board:
    def __init__(self):
        self.rows = 6
        self.columns = 7
        self.grid = [[" " for _ in range(self.columns)] for _ in range(self.rows)]
    def display(self):
        for row in self.grid:
            print("|" + "|".join(row) + "|")
        print(" " + " ".join(str(i) for i in range(self.columns)))
    def place_disc(self, column, disc):
        if column < 0 or column >= self.columns or self.grid[0][column] != " ":
            print("Invalid move. Try again.")
            return False
        for row in reversed(self.grid):
            if row[column] == " ":
                row[column] = disc
                return True
        return False
    def check_line(self, disc):
        # Check horizontal, vertical, and diagonal lines for a win
        # Horizontal check
        for row in range(self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row][col + i] == disc for i in range(4)):
                    return True
        # Vertical check
        for col in range(self.columns):
            for row in range(self.rows - 3):
                if all(self.grid[row + i][col] == disc for i in range(4)):
                    return True
        # Diagonal (bottom-left to top-right) check
        for row in range(self.rows - 3):
            for col in range(self.columns - 3):
                if all(self.grid[row + i][col + i] == disc for i in range(4)):
                    return True
        # Diagonal (top-left to bottom-right) check
        for row in range(3, self.rows):
            for col in range(self.columns - 3):
                if all(self.grid[row - i][col + i] == disc for i in range(4)):
                    return True
        return False
    def is_full(self):
        return all(self.grid[0][col] != " " for col in range(self.columns))