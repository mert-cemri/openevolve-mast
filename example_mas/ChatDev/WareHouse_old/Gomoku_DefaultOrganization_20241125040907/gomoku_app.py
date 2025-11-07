'''
This file contains the GomokuApp class which represents the graphical user interface of the Gomoku game.
'''
import tkinter as tk
class GomokuApp:
    def __init__(self, root):
        self.root = root
        self.game = Game()
        self.canvas = tk.Canvas(self.root, width=450, height=450)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(i * 30, 0, i * 30, 450)
            self.canvas.create_line(0, i * 30, 450, i * 30)
    def handle_click(self, event):
        x = event.x // 30
        y = event.y // 30
        if self.game.make_move(x, y):
            self.draw_piece(x, y)
            if self.game.check_winner(x, y):
                self.show_winner()
    def draw_piece(self, x, y):
        player = self.game.board[y][x]
        if player == 1:
            color = "black"
        else:
            color = "white"
        self.canvas.create_oval(x * 30 + 5, y * 30 + 5, x * 30 + 25, y * 30 + 25, fill=color)
    def show_winner(self):
        winner = "Black" if self.game.current_player == 2 else "White"
        self.canvas.create_text(225, 225, text=f"{winner} wins!", font=("Arial", 20), fill="red")