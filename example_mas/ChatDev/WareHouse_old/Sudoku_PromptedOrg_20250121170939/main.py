'''
Main module to run the Sudoku application.
'''
from sudoku_board import SudokuBoard
from sudoku_solver import SudokuSolver
from sudoku_game import SudokuGame
from sudoku_creator import SudokuCreator
def main():
    board = SudokuBoard()
    creator = SudokuCreator(board)
    creator.create_puzzle()
    solver = SudokuSolver(board)
    game = SudokuGame(board)
    game.start_game()
if __name__ == "__main__":
    main()