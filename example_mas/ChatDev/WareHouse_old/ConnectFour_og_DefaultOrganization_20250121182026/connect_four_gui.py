'''
Manages the graphical user interface for Connect Four using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
class ConnectFourGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = []
        self.create_board()
    def create_board(self):
        for col in range(self.game.columns):
            button = tk.Button(self.root, text=str(col+1), command=lambda c=col: self.handle_click(c))
            button.grid(row=0, column=col)
            self.buttons.append(button)
        self.labels = [[tk.Label(self.root, text='', width=4, height=2, borderwidth=2, relief="groove") 
                        for _ in range(self.game.columns)] for _ in range(self.game.rows)]
        for row in range(self.game.rows):
            for col in range(self.game.columns):
                self.labels[row][col].grid(row=row+1, column=col)
    def update_board(self):
        for row in range(self.game.rows):
            for col in range(self.game.columns):
                disc = self.game.board[row][col]
                if disc == 'R':
                    self.labels[row][col]['bg'] = 'red'
                elif disc == 'Y':
                    self.labels[row][col]['bg'] = 'yellow'
                else:
                    self.labels[row][col]['bg'] = 'white'
    def handle_click(self, column):
        move = self.game.make_move(column)
        if move is None:
            # Display a message if the column is full
            messagebox.showinfo("Invalid Move", "This column is full. Choose another column.")
            return
        row, col = move
        self.update_board()
        if self.game.check_winner(row, col):
            self.show_winner(f"Player {self.game.current_player} wins!")
        elif self.game.is_draw():
            self.show_winner("It's a draw!")
        else:
            self.game.current_player = 'Y' if self.game.current_player == 'R' else 'R'
    def show_winner(self, message):
        for button in self.buttons:
            button.config(state=tk.DISABLED)
        winner_label = tk.Label(self.root, text=message, font=('Helvetica', 16))
        winner_label.grid(row=self.game.rows+1, columnspan=self.game.columns)
        # Add a restart button
        restart_button = tk.Button(self.root, text="Restart Game", command=self.restart_game)
        restart_button.grid(row=self.game.rows+2, columnspan=self.game.columns)
    def restart_game(self):
        self.game.reset_game()
        self.update_board()
        for button in self.buttons:
            button.config(state=tk.NORMAL)
        # Remove winner label and restart button
        for widget in self.root.grid_slaves():
            if int(widget.grid_info()["row"]) > self.game.rows:
                widget.grid_forget()