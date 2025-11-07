'''
Defines the SudokuGame class, which manages the game flow, including user input and checking the game state.
'''
from sudoku_board import SudokuBoard
from utils import print_board
class SudokuGame:
    def __init__(self):
        # Initialize with an empty board or a predefined puzzle
        self.board = SudokuBoard([
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ])
    def play(self):
        while not self.board.is_complete():
            print_board(self.board.board)
            try:
                user_input = input("Enter row, column, and number (1-9) separated by spaces: ").split()
                if len(user_input) != 3:
                    print("Invalid input format. Please enter exactly three numbers separated by spaces.")
                    continue
                row, col, num = map(int, user_input)
                if not (1 <= row <= 9 and 1 <= col <= 9 and 1 <= num <= 9):
                    print("Invalid input. Please enter numbers between 1 and 9.")
                    continue
                if not self.board.place_number(row - 1, col - 1, num):
                    print("Invalid move. Try again.")
            except ValueError:
                print("Invalid input format. Please enter valid numbers.")
        print("Congratulations! You've completed the Sudoku puzzle!")