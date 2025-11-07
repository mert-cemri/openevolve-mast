'''
Contains the GUI class and functions to manage the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
import os
# Removed pyvirtualdisplay import as it's not necessary for local GUI testing
class GUI:
    def __init__(self, game):
        # Removed virtual display setup for local GUI testing
        self.game = game
        self.root = tk.Tk()
        self.player_labels = []
        self.turn_label = None
    def setup_gui(self):
        self.root.title("Dou Dizhu")
        self.create_widgets()
        self.root.mainloop()
    def create_widgets(self):
        '''
        Create and place GUI components.
        '''
        self.turn_label = tk.Label(self.root, text="Welcome to Dou Dizhu!")
        self.turn_label.pack()
        for player in self.game.players:
            label = tk.Label(self.root, text=f"{player.name}: {player.hand}")
            label.pack()
            self.player_labels.append(label)
        play_button = tk.Button(self.root, text="Play Turn", command=self.play_turn)
        play_button.pack()
    def play_turn(self):
        '''
        Handle the play turn button click.
        '''
        # Placeholder for card selection logic
        cards_to_play = []  # This should be replaced with actual selected cards
        if self.game.play_turn(cards_to_play):
            self.update_display()
            winner = self.game.check_winner()
            if winner:
                messagebox.showinfo("Game Over", f"{winner.name} wins!")
                self.root.quit()
    def update_display(self):
        '''
        Logic to update the display after each turn.
        '''
        for i, player in enumerate(self.game.players):
            self.player_labels[i].config(text=f"{player.name}: {player.hand}")
        self.turn_label.config(text=f"{self.game.players[self.game.current_turn].name}'s turn")