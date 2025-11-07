'''
This is the main file for the Gomoku game.
'''
import tkinter as tk
from game import Game
class GomokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gomoku")
        self.geometry("400x400")
        self.game = Game()
        self.create_board()
    def create_board(self):
        self.board = tk.Canvas(self, width=400, height=400)
        self.board.pack()
        self.board.bind("<Button-1>", self.on_click)
    def on_click(self, event):
        row = event.y // 40
        col = event.x // 40
        self.game.make_move(row, col)
        self.draw_board()
    def draw_board(self):
        self.board.delete("all")
        self.game.draw_board(self.board)
if __name__ == "__main__":
    app = GomokuApp()
    app.mainloop()