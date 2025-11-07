'''
This is the main file for the Gomoku game.
'''
import tkinter as tk
from tkinter import messagebox
from game import Game
class GomokuApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Gomoku")
        self.geometry("400x400")
        self.game = Game()
        self.create_board()
    def create_board(self):
        self.board_frame = tk.Frame(self)
        self.board_frame.pack()
        self.buttons = []
        for i in range(15):
            row = []
            for j in range(15):
                button = tk.Button(self.board_frame, width=2, height=1, command=lambda i=i, j=j: self.make_move(i, j))
                button.grid(row=i, column=j)
                row.append(button)
            self.buttons.append(row)
    def make_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)
            if self.game.check_winner(row, col):
                self.show_winner_message(self.game.current_player)
                self.reset_game()
            else:
                self.game.switch_player()
        else:
            messagebox.showerror("Invalid Move", "Selected position is already occupied.")
    def show_winner_message(self, winner):
        messagebox.showinfo("Game Over", f"{winner} wins!")
    def reset_game(self):
        self.game.reset()
        for row in self.buttons:
            for button in row:
                button.config(text="")
if __name__ == "__main__":
    app = GomokuApp()
    app.mainloop()