'''
Handles the game logic, user interaction, and gameplay loop.
'''
from sudoku import Sudoku
class Game:
    def __init__(self, sudoku):
        self.sudoku = sudoku
    def play(self):
        while not self.sudoku.is_completed():
            self.sudoku.display()
            try:
                row = int(input("Enter row (1-9): ")) - 1
                col = int(input("Enter column (1-9): ")) - 1
                num = int(input("Enter number (1-9): "))
                if row not in range(9) or col not in range(9) or num not in range(1, 10):
                    print("Invalid input. Please enter numbers within the correct range.")
                    continue
                if not self.sudoku.is_editable_cell(row, col):
                    print("Cannot modify initial puzzle cells. Choose another cell.")
                    continue
                if self.sudoku.grid[row][col] != 0:
                    print("Cell already filled. Choose another cell.")
                    continue
                if self.sudoku.is_valid_move(row, col, num):
                    self.sudoku.grid[row][col] = num
                else:
                    print("Invalid move. Number conflicts with existing numbers.")
            except ValueError:
                print("Invalid input. Please enter numeric values only.")
        self.sudoku.display()
        print("Congratulations! You completed the Sudoku puzzle!")