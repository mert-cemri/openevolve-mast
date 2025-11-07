'''
This is the main entry point for the puzzle game application. It initializes the game logic and the GUI.
'''
from game import Game
from gui import GameGUI
def main():
    # Initialize the game logic
    game = Game()
    # Initialize the GUI and pass the game logic to it
    gui = GameGUI(game)
    # Start the GUI main loop
    gui.run()
if __name__ == "__main__":
    main()