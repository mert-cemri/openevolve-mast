'''
GUI class to handle the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = None
    def setup_gui(self):
        try:
            self.root = tk.Tk()
            self.root.title("Monopoly Go!")
            self.info_label = tk.Label(self.root, text="Welcome to Monopoly Go!")
            self.info_label.pack()
        except tk.TclError:
            print("GUI cannot be initialized. Running in non-GUI mode.")
    def update_display(self, player):
        if self.root:
            self.info_label.config(text=f"{player.name}'s turn. Money: ${player.money}")
            self.root.update()
        else:
            print(f"{player.name}'s turn. Money: ${player.money}")
    def prompt_buy_property(self, player, property):
        if self.root:
            return messagebox.askyesno("Buy Property", f"{player.name}, do you want to buy {property.name} for ${property.cost}?")
        else:
            response = input(f"{player.name}, do you want to buy {property.name} for ${property.cost}? (yes/no): ")
            return response.lower() == 'yes'
    def display_winner(self, players):
        winner = max(players, key=lambda p: p.money)
        if self.root:
            messagebox.showinfo("Game Over", f"Game Over! {winner.name} wins with ${winner.money}!")
            self.root.quit()
        else:
            print(f"Game Over! {winner.name} wins with ${winner.money}!")