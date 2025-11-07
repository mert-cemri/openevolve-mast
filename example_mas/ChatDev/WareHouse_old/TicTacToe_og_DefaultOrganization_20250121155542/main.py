'''
Main file for the Tic-Tac-Toe game application. Initializes the game logic and GUI.
'''
import tkinter as tk
from tkinter import messagebox
class TicTacToeGame:
    def __init__(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def reset_game(self):
        self.board = ['' for _ in range(9)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, position):
        if self.board[position] == '' and self.winner is None:
            self.board[position] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.switch_player()
            return True
        return False
    def check_winner(self):
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for a, b, c in winning_combinations:
            if self.board[a] == self.board[b] == self.board[c] != '':
                return True
        return False  # Only return True if there is a winner
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
class TicTacToeGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic Tac Toe")
        self.game = TicTacToeGame()
        self.buttons = []
        self.create_board()
    def create_board(self):
        for i in range(9):
            button = tk.Button(self.root, text='', font='Arial 20', width=5, height=2,
                               command=lambda i=i: self.button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
    def update_board(self):
        for i, button in enumerate(self.buttons):
            button.config(text=self.game.board[i])
    def button_click(self, position):
        if self.game.make_move(position):
            self.update_board()
            if self.game.winner:
                self.show_winner(f"Player {self.game.winner} wins!")
            elif '' not in self.game.board:
                self.show_winner("It's a draw!")
    def show_winner(self, message):
        messagebox.showinfo("Game Over", message)
        self.game.reset_game()
        self.update_board()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        gui = TicTacToeGUI(root)
        root.mainloop()
    except tk.TclError:
        print("Error: Unable to initialize the GUI. Please ensure you are running this script in an environment with a graphical display.")