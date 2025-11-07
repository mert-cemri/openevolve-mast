'''
Contains the MinesweeperGUI class which handles the graphical user interface.
'''
import tkinter as tk
from tkinter import messagebox
class MinesweeperGUI:
    def __init__(self, game):
        self.game = game
        try:
            self.root = tk.Tk()
            self.root.title("Minesweeper")
            self.buttons = [[None for _ in range(game.cols)] for _ in range(game.rows)]
            self.create_widgets()
        except tk.TclError as e:
            print("Error: Unable to start the GUI. Ensure a display environment is available.")
            print(e)
    def create_widgets(self):
        for r in range(self.game.rows):
            for c in range(self.game.cols):
                button = tk.Button(self.root, text=' ', width=3, command=lambda r=r, c=c: self.on_button_click(r, c))
                button.grid(row=r, column=c)
                self.buttons[r][c] = button
    def on_button_click(self, row, col):
        if not self.game.is_valid_move(row, col):
            return
        if not self.game.uncover_cell(row, col):
            self.show_mines()
            messagebox.showinfo("Game Over", "You hit a mine!")
            self.root.quit()
        else:
            self.buttons[row][col].config(text=self.game.get_board()[row][col], state='disabled')
    def show_mines(self):
        for r, c in self.game.mine_positions:
            self.buttons[r][c].config(text='*', bg='red')
    def run(self):
        try:
            self.root.mainloop()
        except tk.TclError as e:
            print("Error: Unable to start the GUI. Ensure a display environment is available.")
            print(e)