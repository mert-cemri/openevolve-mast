'''
Defines the DouDizhuGUI class for the game's graphical user interface.
'''
import tkinter as tk
from game import Game
import os
class DouDizhuGUI:
    def __init__(self):
        # Check if running in a headless environment and set up virtual display if necessary
        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':99.0'  # Use a virtual display number
        self.root = tk.Tk()
        self.root.title("Dou Dizhu Game")
        self.game = Game()
        self.setup_ui()
    def setup_ui(self):
        self.start_button = tk.Button(self.root, text="Start Game", command=self.start_game)
        self.start_button.pack()
        self.status_label = tk.Label(self.root, text="Welcome to Dou Dizhu!")
        self.status_label.pack()
    def start_game(self):
        self.game.start_game()
        self.update_status("Game started! It's Player 1's turn.")
    def update_status(self, message):
        self.status_label.config(text=message)
    def run(self):
        self.root.mainloop()