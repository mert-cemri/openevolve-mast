'''
Gomoku GUI implementation using tkinter.
'''
import tkinter as tk
import tkinter.messagebox
from gomoku import GomokuGame
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku Game")
        self.game = GomokuGame()
        self.canvas = tk.Canvas(self.master, width=600, height=600, bg='white')
        self.canvas.pack()
        self.status_label = tk.Label(self.master, text="Current Player: Black", font=("Arial", 14))
        self.status_label.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(self.game.size):
            self.canvas.create_line(40, 40 + i * 40, 40 + (self.game.size - 1) * 40, 40 + i * 40)
            self.canvas.create_line(40 + i * 40, 40, 40 + i * 40, 40 + (self.game.size - 1) * 40)
    def handle_click(self, event):
        x, y = (event.x - 20) // 40, (event.y - 20) // 40
        if 0 <= x < self.game.size and 0 <= y < self.game.size:
            result = self.game.make_move(x, y)
            if result:
                self.status_label.config(text=result)
                self.prompt_new_game()
            else:
                self.update_status()
            self.draw_board()
            self.draw_pieces()
    def draw_pieces(self):
        for x in range(self.game.size):
            for y in range(self.game.size):
                if self.game.board[x][y] == 'Black':
                    self.canvas.create_oval(40 + x * 40 - 15, 40 + y * 40 - 15, 40 + x * 40 + 15, 40 + y * 40 + 15, fill='black')
                elif self.game.board[x][y] == 'White':
                    self.canvas.create_oval(40 + x * 40 - 15, 40 + y * 40 - 15, 40 + x * 40 + 15, 40 + y * 40 + 15, fill='white')
    def update_status(self):
        self.status_label.config(text=f"Current Player: {self.game.current_player}")
    def prompt_new_game(self):
        response = tk.messagebox.askyesno("Game Over", "Do you want to start a new game?")
        if response:
            self.game.reset_game()
            self.update_status()
            self.draw_board()
            self.draw_pieces()