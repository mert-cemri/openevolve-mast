'''
Defines the BlackjackGUI class managing the GUI components.
'''
import tkinter as tk
from blackjack_game import BlackjackGame
import os
# Removed pyvirtualdisplay import as it's not necessary for non-headless environments
class BlackjackGUI:
    def __init__(self):
        # Removed virtual display setup for simplicity
        self.game = BlackjackGame()
        self.root = tk.Tk()
        self.root.title("Blackjack Game")
        self.create_widgets()
        self.update_display()
    def create_widgets(self):
        self.hit_button = tk.Button(self.root, text="Hit", command=self.handle_hit)
        self.hit_button.pack(side=tk.LEFT)
        self.stand_button = tk.Button(self.root, text="Stand", command=self.handle_stand)
        self.stand_button.pack(side=tk.LEFT)
        self.double_down_button = tk.Button(self.root, text="Double Down", command=self.handle_double_down)
        self.double_down_button.pack(side=tk.LEFT)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def update_display(self):
        player_value = self.game.player_hand.get_value()
        dealer_value = self.game.dealer_hand.get_value()
        self.result_label.config(text=f"Player: {player_value} Dealer: {dealer_value}")
    def handle_hit(self):
        self.game.hit()
        self.update_display()
        if self.game.game_over:
            self.result_label.config(text=self.game.check_winner())
    def handle_stand(self):
        self.game.stand()
        self.update_display()
        if self.game.game_over:
            self.result_label.config(text=self.game.check_winner())
    def handle_double_down(self):
        self.game.double_down()
        self.update_display()
        if self.game.game_over:
            self.result_label.config(text=self.game.check_winner())
    def run(self):
        initial_bet = 10  # Example initial bet
        self.game.start_new_round(initial_bet)
        self.update_display()  # Ensure the display is updated at the start
        self.root.mainloop()
    def __del__(self):
        # Removed virtual display stop as it's no longer used
        pass