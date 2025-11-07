'''
Manages the graphical user interface.
'''
import tkinter as tk
import os
class GUI:
    def __init__(self, game):
        self.game = game
        # Check if the DISPLAY environment variable is set
        if not os.environ.get('DISPLAY'):
            print("Warning: No display found. Running in non-GUI mode.")
            self.root = None
            return
        self.root = tk.Tk()
        self.root.title("Monopoly Go!")
        self.info_label = tk.Label(self.root, text="")
        self.info_label.pack()
        self.action_button = tk.Button(self.root, text="Roll Dice", command=self.roll_dice)
        self.action_button.pack()
    def update_display(self):
        if self.root is None:
            return
        current_player = self.game.players[self.game.current_player_index]
        info = f"{current_player.name}'s turn. Position: {current_player.position}, Money: ${current_player.money}"
        self.info_label.config(text=info)
        self.root.update()
    def prompt_player_action(self, player):
        self.update_display()
    def roll_dice(self):
        current_player = self.game.players[self.game.current_player_index]
        self.game.roll_dice_and_move(current_player)
    def start(self):
        if self.root is not None:
            self.root.mainloop()