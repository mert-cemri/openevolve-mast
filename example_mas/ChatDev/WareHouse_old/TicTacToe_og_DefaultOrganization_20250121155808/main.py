'''
Main file to run the Tic-Tac-Toe game with a GUI using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
import os
class TicTacToeGame:
    '''
    Class to manage the Tic-Tac-Toe game logic.
    '''
    def __init__(self):
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
    def reset_game(self):
        '''
        Resets the game board and current player.
        '''
        self.board = [['' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X'
        self.winner = None
    def make_move(self, row, col):
        '''
        Makes a move on the board at the specified row and column.
        '''
        if self.board[row][col] == '' and not self.winner:
            self.board[row][col] = self.current_player
            if self.check_winner():
                self.winner = self.current_player
            else:
                self.switch_player()
    def check_winner(self):
        '''
        Checks if there is a winner on the board.
        '''
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != '':
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != '':
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != '':
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != '':
            return True
        return False
    def switch_player(self):
        '''
        Switches the current player.
        '''
        self.current_player = 'O' if self.current_player == 'X' else 'X'
class TicTacToeGUI:
    '''
    Class to manage the Tic-Tac-Toe game GUI.
    '''
    def __init__(self, master):
        self.master = master
        self.master.title("Tic-Tac-Toe")
        self.game = TicTacToeGame()
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        self.create_board()
    def create_board(self):
        '''
        Creates the game board with buttons.
        '''
        for row in range(3):
            for col in range(3):
                button = tk.Button(self.master, text='', font=('Arial', 24), width=5, height=2,
                                   command=lambda r=row, c=col: self.button_click(r, c))
                button.grid(row=row, column=col)
                self.buttons[row][col] = button
    def update_board(self):
        '''
        Updates the board with the current game state.
        '''
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].config(text=self.game.board[row][col])
    def button_click(self, row, col):
        '''
        Handles button click events.
        '''
        self.game.make_move(row, col)
        self.update_board()
        if self.game.winner:
            messagebox.showinfo("Game Over", f"Player {self.game.winner} wins!")
            self.game.reset_game()
            self.update_board()
        elif all(all(cell != '' for cell in row) for row in self.game.board):
            messagebox.showinfo("Game Over", "It's a draw!")
            self.game.reset_game()
            self.update_board()
if __name__ == "__main__":
    # Check if running in a headless environment
    if os.environ.get('DISPLAY', '') == '':
        print("No display found. Please ensure you are running this on a system with a graphical display.")
    else:
        root = tk.Tk()
        app = TicTacToeGUI(root)
        root.mainloop()