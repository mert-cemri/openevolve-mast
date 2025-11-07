'''
This module contains the Board class, which manages the tic-tac-toe board state and rendering.
'''
import tkinter as tk
from tkinter import messagebox
class Board:
    def __init__(self):
        self.grid = [[" " for _ in range(3)] for _ in range(3)]
        self.window = None
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
    def create_window(self, players, switch_player_callback):
        try:
            self.window = tk.Tk()
            self.window.title("Tic-Tac-Toe")
            for row in range(3):
                for col in range(3):
                    button = tk.Button(self.window, text=" ", font='Arial 20', width=5, height=2,
                                       command=lambda r=row, c=col: self.make_move(r, c, players, switch_player_callback))
                    button.grid(row=row, column=col)
                    self.buttons[row][col] = button
            self.window.mainloop()
        except tk.TclError as e:
            print(f"Error: {e}. Ensure you have a display available or use a virtual display.")
    def make_move(self, row, col, players, switch_player_callback):
        current_player = players[self.current_player_index]
        if self.grid[row][col] == " ":
            self.grid[row][col] = current_player.symbol
            self.buttons[row][col].config(text=current_player.symbol)
            if self.has_winner():
                messagebox.showinfo("Game Over", f"Player {current_player.symbol} wins!")
                self.window.quit()
            elif self.is_full():
                messagebox.showinfo("Game Over", "It's a draw!")
                self.window.quit()
            else:
                switch_player_callback()
        else:
            messagebox.showwarning("Invalid Move", "This cell is already taken!")
    def is_full(self):
        return all(cell != " " for row in self.grid for cell in row)
    def has_winner(self):
        lines = self.grid + [list(col) for col in zip(*self.grid)]  # Rows and columns
        lines.append([self.grid[i][i] for i in range(3)])  # Diagonal
        lines.append([self.grid[i][2 - i] for i in range(3)])  # Anti-diagonal
        return any(line[0] == line[1] == line[2] != " " for line in lines)