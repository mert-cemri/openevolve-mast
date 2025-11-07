'''
Board class to represent the Gomoku game board.
'''
class Board:
    def __init__(self, size):
        self.size = size
        self.grid = [[" " for _ in range(size)] for _ in range(size)]
    def place_stone(self, row, col, stone):
        if self.is_valid_move(row, col):
            self.grid[row][col] = stone
            return True
        return False
    def is_valid_move(self, row, col):
        return 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == " "
    def print_board(self):
        for row in self.grid:
            print(" ".join(row))
        print()
    def check_winner(self, stone):
        # Check horizontal, vertical, and diagonal lines for a win
        for row in range(self.size):
            for col in range(self.size):
                if self.check_line(row, col, stone, 1, 0) or \
                   self.check_line(row, col, stone, 0, 1) or \
                   self.check_line(row, col, stone, 1, 1) or \
                   self.check_line(row, col, stone, 1, -1):
                    return True
        return False
    def check_line(self, row, col, stone, delta_row, delta_col):
        count = 0
        for _ in range(5):
            if 0 <= row < self.size and 0 <= col < self.size and self.grid[row][col] == stone:
                count += 1
                row += delta_row
                col += delta_col
            else:
                break
        # Check if exactly 5 stones and not part of a longer sequence
        if count == 5:
            # Check the previous and next positions in the line
            prev_row, prev_col = row - 5 * delta_row, col - 5 * delta_col
            next_row, next_col = row, col
            if (not (0 <= prev_row < self.size and 0 <= prev_col < self.size) or self.grid[prev_row][prev_col] != stone) and \
               (not (0 <= next_row < self.size and 0 <= next_col < self.size) or self.grid[next_row][next_col] != stone):
                return True
        return False
    def is_full(self):
        return all(self.grid[row][col] != " " for row in range(self.size) for col in range(self.size))