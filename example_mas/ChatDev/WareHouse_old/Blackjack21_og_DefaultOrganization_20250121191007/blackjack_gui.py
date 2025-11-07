'''
Handles the graphical user interface for the Blackjack game.
'''
import tkinter as tk
from blackjack_game import BlackjackGame
class BlackjackGUI:
    def __init__(self, game):
        self.game = game
        self.root = None
        self.info_label = None  # Ensure info_label is initialized
        self.create_widgets()
    def create_widgets(self):
        if self.root is None:
            try:
                self.root = tk.Tk()
                self.root.title("Blackjack")
            except tk.TclError as e:
                print("Error: Unable to create GUI. Ensure you have a display environment set up.")
                return
        self.info_label = tk.Label(self.root, text="Welcome to Blackjack!")
        self.info_label.pack()
        self.hit_button = tk.Button(self.root, text="Hit", command=lambda: self.handle_action('hit'))
        self.hit_button.pack(side=tk.LEFT)
        self.stand_button = tk.Button(self.root, text="Stand", command=lambda: self.handle_action('stand'))
        self.stand_button.pack(side=tk.LEFT)
        self.double_down_button = tk.Button(self.root, text="Double Down", command=lambda: self.handle_action('double_down'))
        self.double_down_button.pack(side=tk.LEFT)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
    def update_display(self):
        if self.info_label:  # Check if info_label is initialized
            player_value = self.game.player.hand.calculate_value()
            dealer_value = self.game.dealer.hand.calculate_value()
            self.info_label.config(text=f"Player: {player_value}, Dealer: {dealer_value}")
    def handle_action(self, action):
        self.game.player_turn(action)
        self.update_display()
        if action == 'stand' or action == 'double_down' or self.game.player.hand.is_bust():
            self.game.dealer_turn()
            result = self.game.determine_winner()
            self.result_label.config(text=result)
    def run(self):
        self.game.start_game()
        self.update_display()
        if self.root:
            self.root.mainloop()