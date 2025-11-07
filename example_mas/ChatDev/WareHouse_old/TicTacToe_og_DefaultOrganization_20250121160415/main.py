'''
Main file for the Tic-Tac-Toe game application using tkinter for GUI.
'''
import tkinter as tk
from tictactoe_game import TicTacToeGame
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
    def create_board(self):
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.root, text="", font=('Arial', 60), width=5, height=2,
                                   command=lambda r=row, c=col: self.on_button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def on_button_click(self, row, col):
        if self.game.make_move(row, col):
            self.update_board()
            winner = self.game.check_winner()
            if winner:
                self.show_winner(winner)
    def update_board(self):
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game.board[row][col])
    def show_winner(self, winner):
        if winner == "Draw":
            message = "It's a Draw!"
        else:
            message = f"Player {winner} wins!"
        result_label = tk.Label(self.root, text=message, font=('Arial', 24))
        result_label.grid(row=3, column=0, columnspan=3)
        reset_button = tk.Button(self.root, text="Play Again", command=self.reset_game)
        reset_button.grid(row=4, column=0, columnspan=3)
    def reset_game(self):
        self.game.reset_game()
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text="")
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > 2:
                widget.destroy()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        app = TicTacToeGUI(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you are running in an environment that supports GUI operations.")
        print(e)