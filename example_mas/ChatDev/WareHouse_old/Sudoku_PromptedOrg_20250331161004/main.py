'''
Main entry point for the Sudoku game. Initializes and starts the game loop.
'''
from sudoku_game import SudokuGame
def main():
    game = SudokuGame()
    game.play()
if __name__ == "__main__":
    main()