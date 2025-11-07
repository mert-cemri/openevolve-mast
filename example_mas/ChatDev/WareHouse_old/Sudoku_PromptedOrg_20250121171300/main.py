'''
Main entry point for the Sudoku application.
'''
from sudoku_game import SudokuGame
def main():
    game = SudokuGame()
    game.start()
if __name__ == "__main__":
    main()