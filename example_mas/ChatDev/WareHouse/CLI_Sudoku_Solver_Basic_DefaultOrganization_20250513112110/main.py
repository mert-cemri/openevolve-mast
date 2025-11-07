'''
Main entry point for the CLI Sudoku solver application. Handles input and output through the command line.
'''
from sudoku_solver import SudokuSolver
def read_sudoku():
    board = []
    print("Enter the Sudoku puzzle row by row, use 0 for empty cells:")
    for _ in range(9):
        row = list(map(int, input().strip().split()))
        if len(row) != 9:
            raise ValueError("Each row must have exactly 9 numbers.")
        board.append(row)
    return board
def print_sudoku(board):
    for row in board:
        print(" ".join(map(str, row)))
def main():
    board = read_sudoku()
    solver = SudokuSolver()
    if solver.solve(board):
        print("Solved Sudoku:")
        print_sudoku(board)
    else:
        print("No solution exists")
if __name__ == "__main__":
    main()