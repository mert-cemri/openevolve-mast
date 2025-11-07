'''
FILENAME: main.py
LANGUAGE: Python
DOCSTRING: This file contains the implementation of a tic-tac-toe game using tkinter for the GUI.
It includes the game logic and user interface to allow two players to play the game.
'''
import tkinter as tk
from tkinter import messagebox
class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, position):
        if self.board[position] == ' ' and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.switch_player()
            return True
        return False
    def check_winner(self):
        win_conditions = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in win_conditions:
            if self.board[a] == self.board[b] == self.board[c] != ' ':
                return True
        return ' ' not in self.board
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = []
        self.create_board()
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text=' ', font=('Arial', 24), width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    def on_button_click(self, position):
        if self.game.make_move(position):
            self.update_button(position)
            if self.game.winner:
                self.display_winner(f"Player {self.game.winner} wins!")
            elif ' ' not in self.game.board:
                self.display_winner("It's a draw!")
    def update_button(self, position):
        self.buttons[position].config(text=self.game.current_player)
    def display_winner(self, message):
        messagebox.showinfo("Game Over", message)
        self.restart_game()
    def restart_game(self):
        self.game.reset_game()
        for button in self.buttons:
            button.config(text=' ')
if __name__ == "__main__":
    try:
        root = tk.Tk()
        gui = TicTacToeGUI(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you are running this on a system with a graphical display.")
        print(e)