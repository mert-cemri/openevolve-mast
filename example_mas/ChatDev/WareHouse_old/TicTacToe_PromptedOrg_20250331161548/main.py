'''
Main entry point for the Tic-Tac-Toe game. Initializes the game and starts the GUI.
'''
from tictactoe_gui import TicTacToeGUI
def main():
    game = TicTacToeGUI()
    game.run()
if __name__ == "__main__":
    main()