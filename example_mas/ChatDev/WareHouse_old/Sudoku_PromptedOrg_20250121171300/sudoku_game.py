'''
Defines the SudokuGame class to manage the game flow and user interactions.
'''
from sudoku_grid import SudokuGrid
from sudoku_solver import SudokuSolver
class SudokuGame:
    def __init__(self):
        self.grid = SudokuGrid()
        self.solver = SudokuSolver(self.grid)
    def start(self):
        print("Welcome to Sudoku!")
        self.input_initial_values()
        self.grid.print_grid()
        while not self.grid.is_complete():
            self.input_value()
            self.grid.print_grid()
            if self.grid.is_complete():
                print("Congratulations! You have completed the puzzle.")
                break
    def input_initial_values(self):
        print("Enter initial values for the Sudoku puzzle. Type 'done' when finished.")
        while True:
            try:
                user_input = input("Enter row (0-8), column (0-8), and number (1-9) separated by spaces, or 'done': ")
                if user_input.lower() == 'done':
                    break
                row, col, num = map(int, user_input.split())
                if not self.grid.set_value(row, col, num):
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input. Please enter numbers only or 'done'.")
    def input_value(self):
        try:
            row = int(input("Enter row (0-8): "))
            col = int(input("Enter column (0-8): "))
            num = int(input("Enter number (1-9): "))
            if not self.grid.set_value(row, col, num):
                print("Invalid move. Try again.")
            else:
                self.grid.print_grid()
                if self.check_for_mistakes():
                    print("Please correct the mistakes.")
        except ValueError:
            print("Invalid input. Please enter numbers only.")
    def check_for_mistakes(self):
        for i in range(9):
            for j in range(9):
                num = self.grid.get_value(i, j)
                if num != 0 and not self.grid.is_valid_move(i, j, num):
                    print(f"Mistake found at row {i}, column {j}.")
                    return True
        return False