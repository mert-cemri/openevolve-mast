'''
Manages the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
import os
class GUI:
    def __init__(self, game):
        # Check if running in a headless environment
        if not os.environ.get('DISPLAY'):
            print("Warning: No display environment available for GUI. Running in non-GUI mode.")
            self.headless_mode = True
            self.root = None  # Initialize root as None in headless mode
        else:
            self.headless_mode = False
            self.root = tk.Tk()
            self.root.title("Monopoly Go!")
            self.info_label = tk.Label(self.root, text="", justify=tk.LEFT)
            self.info_label.pack()
            self.action_button = tk.Button(self.root, text="Roll Dice", command=self.on_action_button_click)
            self.action_button.pack()
        self.game = game
        self.current_player = None
    def update_display(self):
        if self.headless_mode:
            return
        info = f"Current Player: {self.game.players[self.game.current_player_index].name}\n"
        for player in self.game.players:
            info += f"{player.name}: ${player.money}, Properties: {[p.name for p in player.properties]}\n"
        self.info_label.config(text=info)
        self.root.update()
    def prompt_player_action(self, player):
        if self.headless_mode:
            return
        self.current_player = player
        self.action_button.config(state=tk.NORMAL)
    def on_action_button_click(self):
        if self.headless_mode:
            return
        if self.current_player:
            self.action_button.config(state=tk.DISABLED)
            self.game.take_turn(self.current_player)
            self.update_display()
            messagebox.showinfo("Turn Complete", f"{self.current_player.name}'s turn is complete.")
            self.current_player = None