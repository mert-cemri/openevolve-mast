'''
Handles the graphical user interface for Minesweeper, including displaying the board and handling user interactions.
'''
import tkinter as tk
from tkinter import messagebox
class MinesweeperGUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Minesweeper")
        self.buttons = [[None for _ in range(game.size)] for _ in range(game.size)]
        self.create_board()
    def create_board(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                button = tk.Button(self.root, width=3, height=1, command=lambda r=row, c=col: self.cell_clicked(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def update_board(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.revealed[row][col]:
                    if self.game.board[row][col] == 'M':
                        self.buttons[row][col].config(text='M', bg='red')
                    else:
                        self.buttons[row][col].config(text=str(self.game.board[row][col]), bg='lightgrey')
    def cell_clicked(self, row, col):
        if self.game.uncover_cell(row, col):
            self.update_board()
            messagebox.showinfo("Game Over", "You hit a mine! Game Over.")
            self.root.quit()
        elif self.game.check_win():
            self.update_board()
            messagebox.showinfo("Congratulations", "You won!")
            self.root.quit()
        else:
            self.update_board()
    def run(self):
        try:
            self.root.mainloop()
        except tk.TclError as e:
            print(f"Error: {e}. Ensure you are running this in an environment with a display.")