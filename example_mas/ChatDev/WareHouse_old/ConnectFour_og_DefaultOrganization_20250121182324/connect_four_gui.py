'''
Manages the graphical user interface for Connect Four using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class ConnectFourGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = []
        self.create_board()
    def create_board(self):
        for col in range(self.game.columns):
            button = tk.Button(self.root, text=f"Drop {col+1}", command=lambda c=col: self.handle_click(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)
        self.labels = [[tk.Label(self.root, text=' ', width=4, height=2, bg='blue', relief='ridge') for _ in range(self.game.columns)] for _ in range(self.game.rows)]
        for r in range(self.game.rows):
            for c in range(self.game.columns):
                self.labels[r][c].grid(row=r+1, column=c)
    def update_board(self):
        for r in range(self.game.rows):
            for c in range(self.game.columns):
                disc = self.game.board[r][c]
                color = 'white' if disc == '' else ('red' if disc == 'R' else 'yellow')
                self.labels[r][c].config(bg=color)
    def handle_click(self, column):
        result = self.game.drop_disc(column)
        self.update_board()
        if result:
            self.show_message(result)
    def show_message(self, message):
        for button in self.buttons:
            button.config(state='disabled')
        messagebox.showinfo("Game Over", message)