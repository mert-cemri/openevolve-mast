'''
Main file to run the Tic-Tac-Toe game with a GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class TicTacToeGame:
    def __init__(self):
        self.board = [' ' for _ in range(9)]  # 3x3 board
        self.current_player = 'X'
    def reset_game(self):
        self.board = [' ' for _ in range(9)]
        self.current_player = 'X'
    def make_move(self, position):
        if self.board[position] == ' ':
            self.board[position] = self.current_player
            return True
        return False
    def check_winner(self):
        # Winning combinations
        winning_combinations = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),  # rows
            (0, 3, 6), (1, 4, 7), (2, 5, 8),  # columns
            (0, 4, 8), (2, 4, 6)              # diagonals
        ]
        for (x, y, z) in winning_combinations:
            if self.board[x] == self.board[y] == self.board[z] != ' ':
                return self.board[x]
        if ' ' not in self.board:
            return 'Draw'
        return None
    def switch_player(self):
        self.current_player = 'O' if self.current_player == 'X' else 'X'
class TicTacToeGUI:
    def __init__(self, root):
        self.game = TicTacToeGame()
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.buttons = [tk.Button(root, text=' ', font='Arial 20', width=5, height=2,
                                  command=lambda i=i: self.button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            row, col = divmod(i, 3)
            button.grid(row=row, column=col)
        self.update_buttons()
    def update_buttons(self):
        for i, button in enumerate(self.buttons):
            button.config(text=self.game.board[i])
    def button_click(self, position):
        if self.game.make_move(position):
            self.update_buttons()
            winner = self.game.check_winner()
            if winner:
                self.show_winner(winner)
            else:
                self.game.switch_player()
    def show_winner(self, winner):
        if winner == 'Draw':
            messagebox.showinfo("Tic-Tac-Toe", "It's a draw!")
        else:
            messagebox.showinfo("Tic-Tac-Toe", f"Player {winner} wins!")
        self.game.reset_game()
        self.update_buttons()
if __name__ == "__main__":
    try:
        root = tk.Tk()
        gui = TicTacToeGUI(root)
        root.mainloop()
    except tk.TclError as e:
        print("Error: Unable to start the GUI. Ensure you have a display environment available.")
        print(e)