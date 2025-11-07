'''
Defines the SudokuCreator class to generate a new Sudoku puzzle.
'''
import random
class SudokuCreator:
    def __init__(self, board):
        self.board = board
    def create_puzzle(self):
        # Fill the diagonal 3x3 boxes
        for i in range(0, 9, 3):
            self.fill_box(i, i)
        # Fill remaining blocks
        self.fill_remaining(0, 3)
        # Remove some numbers to create the puzzle
        self.remove_numbers()
    def fill_box(self, row, col):
        nums = list(range(1, 10))
        random.shuffle(nums)
        for i in range(3):
            for j in range(3):
                self.board.grid[row + i][col + j] = nums.pop()
    def fill_remaining(self, i, j):
        if j >= 9 and i < 8:
            i += 1
            j = 0
        if i >= 9 and j >= 9:
            return True
        if i < 3:
            if j < 3:
                j = 3
        elif i < 9 - 3:
            if j == int(i / 3) * 3:
                j += 3
        else:
            if j == 6:
                i += 1
                j = 0
                if i >= 9:
                    return True
        for num in range(1, 10):
            if self.board.is_valid_move(i, j, num):
                self.board.grid[i][j] = num
                if self.fill_remaining(i, j + 1):
                    return True
                self.board.grid[i][j] = 0
        return False
    def remove_numbers(self):
        count = random.randint(20, 30)  # Number of cells to remove
        while count != 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.board.grid[i][j] != 0:
                self.board.grid[i][j] = 0
                count -= 1