'''
This module serves as the entry point for the Sudoku solver application.
It coordinates the input, solving, and output processes.
'''
import argparse
from input_handler import InputHandler
from sudoku_solver import SudokuSolver
from output_handler import OutputHandler
def main():
    parser = argparse.ArgumentParser(description="Sudoku Solver")
    parser.add_argument("source", help="Input source (filename or 'direct' for manual input)")
    args = parser.parse_args()
    try:
        if args.source.lower() == 'direct':
            print("Enter the Sudoku grid row by row, using 0 for empty cells. Separate numbers with spaces.")
            board = []
            for i in range(9):
                while True:
                    try:
                        row = list(map(int, input(f"Row {i+1}: ").split()))
                        if len(row) != 9:
                            raise ValueError("Each row must contain exactly 9 numbers.")
                        board.append(row)
                        break
                    except ValueError as ve:
                        print(f"Input error: {ve}. Please enter a valid row with 9 integers.")
        else:
            input_handler = InputHandler(args.source)
            board = input_handler.read_board()
        solver = SudokuSolver(board)
        solved_board = solver.solve()
        if solved_board:
            output_handler = OutputHandler(solved_board)
            output_handler.print_board()
        else:
            print("No solution exists")
    except ValueError as ve:
        print(f"Input error: {ve}")
    except FileNotFoundError:
        print(f"File not found: {args.source}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
if __name__ == "__main__":
    main()