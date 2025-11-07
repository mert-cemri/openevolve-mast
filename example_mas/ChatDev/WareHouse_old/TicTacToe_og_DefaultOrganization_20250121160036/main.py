'''
This file initializes the tic-tac-toe game with a GUI using tkinter.
It creates an instance of the TicTacToeGUI class to start the game.
'''
import tkinter as tk
from game_logic import TicTacToeGame
import os
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = TicTacToeGame()
        self.current_player = "X"
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.status_label = tk.Label(root, text="Player X's turn", font=('Arial', 14))
        self.status_label.pack(side="top")
        self.create_buttons()
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_board)
        self.reset_button.pack(side="bottom")
    def create_buttons(self):
        frame = tk.Frame(self.root)
        frame.pack()
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(frame, text="", font=('Arial', 20), width=5, height=2,
                                               command=lambda i=i, j=j: self.button_click(i, j))
                self.buttons[i][j].grid(row=i, column=j)
    def button_click(self, i, j):
        if self.buttons[i][j]["text"] == "":
            if not self.game.check_winner():
                self.buttons[i][j]["text"] = self.current_player
                self.game.make_move(i, j, self.current_player)
                if self.game.check_winner():
                    self.update_status(f"Player {self.current_player} wins!")
                elif self.game.is_draw():
                    self.update_status("It's a draw!")
                else:
                    self.current_player = "O" if self.current_player == "X" else "X"
                    self.update_status(f"Player {self.current_player}'s turn")
        else:
            self.update_status("Cell already occupied! Try a different move.")
    def update_status(self, message):
        self.status_label.config(text=message)
    def reset_board(self):
        self.game.reset_game()
        self.current_player = "X"
        self.update_status("Player X's turn")
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]["text"] = ""
if __name__ == "__main__":
    # Check if DISPLAY is set, if not, set it for headless environments
    if not os.environ.get('DISPLAY'):
        os.environ['DISPLAY'] = ':0'  # Change to :0 for local display
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()