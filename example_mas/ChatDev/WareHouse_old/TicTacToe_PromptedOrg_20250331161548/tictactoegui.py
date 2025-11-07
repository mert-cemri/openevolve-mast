'''
Handles the graphical user interface for the Tic-Tac-Toe game using tkinter.
'''
import tkinter as tk
from tictactoe_game import TicTacToeGame
import os
class TicTacToeGUI:
    def __init__(self):
        # Check if running in a headless environment and set a virtual display if necessary
        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':0'
        self.game = TicTacToeGame()
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_widgets()
    def create_widgets(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_button_click(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)
            if self.game.winner:
                self.show_winner(self.game.winner)
            elif self.game.is_full():
                self.show_winner("No one")
    def show_winner(self, winner):
        winner_text = f"{winner} wins!" if winner != "No one" else "It's a draw!"
        result_label = tk.Label(self.root, text=winner_text, font=('Arial', 18))
        result_label.grid(row=3, column=0, columnspan=3)
        restart_button = tk.Button(self.root, text='Restart', command=self.restart_game)
        restart_button.grid(row=4, column=0, columnspan=3)
        # Disable all buttons
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(state='disabled')
    def restart_game(self):
        self.game.reset()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text='', state='normal')
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.destroy()
    def run(self):
        self.root.mainloop()