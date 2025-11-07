'''
This is the main file of the Gomoku game. It initializes the game and handles the user interface.
'''
import tkinter as tk
from game import Game
class GomokuGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Gomoku")
        self.game = Game()
        self.create_board()
    def create_board(self):
        self.board_frame = tk.Frame(self.master)
        self.board_frame.pack()
        self.buttons = []
        for row in range(self.game.board_size):
            row_buttons = []
            for col in range(self.game.board_size):
                button = tk.Button(self.board_frame, width=4, height=2, command=lambda r=row, c=col: self.make_move(r, c))
                button.grid(row=row, column=col)
                row_buttons.append(button)
            self.buttons.append(row_buttons)
    def make_move(self, row, col):
        if self.game.make_move(row, col):
            self.buttons[row][col].config(text=self.game.current_player)
            if self.game.check_winner(row, col):
                self.show_winner_message()
            elif self.game.is_board_full():
                self.show_draw_message()
            else:
                self.game.switch_player()
    def show_winner_message(self):
        winner = self.game.current_player
        message = f"{winner} wins!"
        tk.messagebox.showinfo("Game Over", message)
        self.reset_game()
    def show_draw_message(self):
        tk.messagebox.showinfo("Game Over", "It's a draw!")
        self.reset_game()
    def reset_game(self):
        self.game.reset()
        for row in self.buttons:
            for button in row:
                button.config(text="")
if __name__ == "__main__":
    root = tk.Tk()
    gomoku_gui = GomokuGUI(root)
    root.mainloop()