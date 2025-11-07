'''
Minesweeper game implementation using Python and tkinter for GUI.
'''
import tkinter as tk
from tkinter import messagebox
import random
class MinesweeperGame:
    def __init__(self, size=9, mines=10):
        self.size = size
        self.mines = mines
        self.grid = [[0 for _ in range(size)] for _ in range(size)]
        self.revealed = [[False for _ in range(size)] for _ in range(size)]
        self.flags = [[False for _ in range(size)] for _ in range(size)]
        self.game_over = False
        self.initialize_game()
    def initialize_game(self):
        self.place_mines()
        self.calculate_adjacent_mines()
    def place_mines(self):
        mines_placed = 0
        while mines_placed < self.mines:
            row = random.randint(0, self.size - 1)
            col = random.randint(0, self.size - 1)
            if self.grid[row][col] != -1:
                self.grid[row][col] = -1
                mines_placed += 1
    def calculate_adjacent_mines(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] == -1:
                    continue
                count = 0
                for i in range(max(0, row - 1), min(self.size, row + 2)):
                    for j in range(max(0, col - 1), min(self.size, col + 2)):
                        if self.grid[i][j] == -1:
                            count += 1
                self.grid[row][col] = count
    def uncover_cell(self, row, col):
        if self.game_over or self.revealed[row][col] or self.flags[row][col]:
            return
        self.revealed[row][col] = True
        if self.grid[row][col] == -1:
            self.game_over = True
        elif self.grid[row][col] == 0:
            for i in range(max(0, row - 1), min(self.size, row + 2)):
                for j in range(max(0, col - 1), min(self.size, col + 2)):
                    if not self.revealed[i][j]:
                        self.uncover_cell(i, j)
    def check_win(self):
        for row in range(self.size):
            for col in range(self.size):
                if self.grid[row][col] != -1 and not self.revealed[row][col]:
                    return False
        return True
class MinesweeperGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = [[None for _ in range(game.size)] for _ in range(game.size)]
        self.create_widgets()
    def create_widgets(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                button = tk.Button(self.root, width=2, height=1, command=lambda r=row, c=col: self.on_cell_click(r, c))
                button.grid(row=row, column=col)
                button.bind('<Button-3>', lambda event, r=row, c=col: self.toggle_flag(r, c))
                self.buttons[row][col] = button
        self.update_display()
    def update_display(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.revealed[row][col]:
                    if self.game.grid[row][col] == -1:
                        self.buttons[row][col].config(text='*', state='disabled')
                    else:
                        self.buttons[row][col].config(text=str(self.game.grid[row][col]), state='disabled')
                elif self.game.flags[row][col]:
                    self.buttons[row][col].config(text='F', state='normal')
                else:
                    self.buttons[row][col].config(text='', state='normal')
    def on_cell_click(self, row, col):
        self.game.uncover_cell(row, col)
        self.update_display()
        if self.game.game_over:
            self.show_game_over()
        elif self.game.check_win():
            self.show_win()
    def toggle_flag(self, row, col):
        if not self.game.revealed[row][col]:
            self.game.flags[row][col] = not self.game.flags[row][col]
            self.update_display()
    def show_game_over(self):
        for row in range(self.game.size):
            for col in range(self.game.size):
                if self.game.grid[row][col] == -1:
                    self.buttons[row][col].config(text='*')
        messagebox.showinfo("Game Over", "You hit a mine! Game Over.")
    def show_win(self):
        messagebox.showinfo("Congratulations", "You win!")
def main():
    try:
        root = tk.Tk()
        root.title("Minesweeper")
        game = MinesweeperGame()
        gui = MinesweeperGUI(root, game)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to initialize the GUI. Please ensure you are running this in a graphical environment.")
if __name__ == "__main__":
    main()