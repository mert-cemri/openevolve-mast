'''
Manages the graphical user interface for the Blackjack game using tkinter.
'''
import tkinter as tk
from blackjack_game import BlackjackGame
class BlackjackGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Blackjack Game")
        self.setup_ui()
    def setup_ui(self):
        self.player_label = tk.Label(self.root, text="Player's Hand: ")
        self.player_label.pack()
        self.dealer_label = tk.Label(self.root, text="Dealer's Hand: ")
        self.dealer_label.pack()
        self.hit_button = tk.Button(self.root, text="Hit", command=self.hit)
        self.hit_button.pack()
        self.stand_button = tk.Button(self.root, text="Stand", command=self.stand)
        self.stand_button.pack()
        self.double_down_button = tk.Button(self.root, text="Double Down", command=self.double_down)
        self.double_down_button.pack()
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack()
        self.new_game_button = tk.Button(self.root, text="New Game", command=self.start_new_game)
        self.new_game_button.pack()
        self.update_display()
    def update_display(self):
        player_hand = ', '.join(f'{card.rank} of {card.suit}' for card in self.game.player_hand.cards)
        dealer_hand = ', '.join(f'{card.rank} of {card.suit}' for card in self.game.dealer_hand.cards)
        self.player_label.config(text=f"Player's Hand: {player_hand} (Value: {self.game.player_hand.calculate_value()})")
        self.dealer_label.config(text=f"Dealer's Hand: {dealer_hand} (Value: {self.game.dealer_hand.calculate_value()})")
    def hit(self):
        self.game.player_hit()
        self.update_display()
        if self.game.player_hand.is_bust():
            self.result_label.config(text="Player busts! Dealer wins!")
    def stand(self):
        self.game.player_stand()
        self.update_display()
        self.result_label.config(text=self.game.determine_winner())
    def double_down(self):
        self.game.player_double_down()
        self.update_display()
        self.result_label.config(text=self.game.determine_winner())
        self.hit_button.config(state=tk.DISABLED)
        self.stand_button.config(state=tk.DISABLED)
    def start_new_game(self):
        self.game.start_new_game()
        self.update_display()
        self.result_label.config(text="")
        self.hit_button.config(state=tk.NORMAL)
        self.stand_button.config(state=tk.NORMAL)
    def run(self):
        self.root.mainloop()