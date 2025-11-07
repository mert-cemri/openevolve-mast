'''
Main entry point for the Connect Four game application.
'''
import tkinter as tk
from connect_four_game import ConnectFourGame
from connect_four_gui import ConnectFourGUI
def main():
    # Initialize the main window
    root = tk.Tk()
    root.title("Connect Four")
    # Initialize the game logic
    game = ConnectFourGame()
    # Initialize the GUI
    gui = ConnectFourGUI(root, game)
    # Start the GUI event loop
    root.mainloop()
if __name__ == "__main__":
    main()