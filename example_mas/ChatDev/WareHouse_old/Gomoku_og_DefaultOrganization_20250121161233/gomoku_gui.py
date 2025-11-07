'''
Manages the graphical user interface for the Gomoku game.
'''
import tkinter as tk
from gomoku_game import GomokuGame
class GomokuGUI:
    def __init__(self, root):
        self.root = root
        self.game = GomokuGame()
        self.canvas = tk.Canvas(root, width=600, height=600, bg='white')
        self.canvas.pack()
        self.draw_board()
        self.canvas.bind("<Button-1>", self.on_click)
    def draw_board(self):
        size = self.game.board.size
        for i in range(size):
            self.canvas.create_line(20, 20 + i * 40, 580, 20 + i * 40)
            self.canvas.create_line(20 + i * 40, 20, 20 + i * 40, 580)
    def on_click(self, event):
        x, y = (event.x - 20) // 40, (event.y - 20) // 40
        if 0 <= x < self.game.board.size and 0 <= y < self.game.board.size:
            if self.game.board.place_stone(x, y, self.game.current_player):
                self.draw_stone(x, y, self.game.current_player)
                winner = self.game.board.check_winner()
                if winner:
                    self.show_winner(winner)
                elif self.game.board.check_draw():
                    self.show_draw()
                else:
                    self.game.switch_player()
    def draw_stone(self, x, y, player):
        color = 'black' if player == "Black" else 'white'
        self.canvas.create_oval(20 + x * 40 - 15, 20 + y * 40 - 15, 20 + x * 40 + 15, 20 + y * 40 + 15, fill=color)
    def show_winner(self, winner):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(300, 300, text=f"{winner} wins!", font=("Arial", 24), fill="red")
    def show_draw(self):
        self.canvas.unbind("<Button-1>")
        self.canvas.create_text(300, 300, text="It's a draw!", font=("Arial", 24), fill="blue")