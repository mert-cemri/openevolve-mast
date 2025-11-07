'''
Contains the ConnectFourGUI class to handle the graphical user interface using tkinter.
'''
import tkinter as tk
from game import Game
class ConnectFourGUI:
    def __init__(self):
        self.game = Game()
        self.window = tk.Tk()
        self.window.title("Connect Four")
        self.canvas = tk.Canvas(self.window, width=700, height=600, bg="blue")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.handle_click)
        self.status_label = tk.Label(self.window, text="Player 1's turn", font=("Arial", 14))
        self.status_label.pack()
        self.draw_board()
    def draw_board(self):
        self.canvas.delete("all")
        for row in range(6):
            for col in range(7):
                x0 = col * 100 + 10
                y0 = row * 100 + 10
                x1 = x0 + 80
                y1 = y0 + 80
                color = "white"
                if self.game.board[row][col] == 1:
                    color = "red"
                elif self.game.board[row][col] == 2:
                    color = "yellow"
                self.canvas.create_oval(x0, y0, x1, y1, fill=color, outline="black")
    def handle_click(self, event):
        col = event.x // 100
        if self.game.winner is None and self.game.make_move(col):
            self.draw_board()
            if self.game.winner:
                self.update_status(f"Player {self.game.winner} wins!")
            elif self.game.is_draw():
                self.update_status("It's a draw!")
            else:
                self.update_status(f"Player {self.game.current_player}'s turn")
    def update_status(self, message):
        self.status_label.config(text=message)
    def run(self):
        self.window.mainloop()