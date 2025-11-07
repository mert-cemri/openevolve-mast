'''
Handle the Tic-Tac-Toe game user interface.
'''
import tkinter as tk
class TicTacToeGUI:
    def __init__(self, root, game):
        self.root = root
        self.game = game
        self.buttons = [tk.Button(root, text=' ', font='Arial 20', width=5, height=2,
                                  command=lambda i=i: self.button_click(i)) for i in range(9)]
        for i, button in enumerate(self.buttons):
            button.grid(row=i//3, column=i%3)
        self.status_label = tk.Label(root, text="Player X's turn", font='Arial 15')
        self.status_label.grid(row=3, column=0, columnspan=3)
    def update_buttons(self):
        '''
        Update the button text based on the game state.
        '''
        for i, button in enumerate(self.buttons):
            button.config(text=self.game.board[i])
    def button_click(self, position):
        '''
        Handle button click events.
        '''
        self.game.make_move(position)
        self.update_buttons()
        if self.game.winner:
            self.show_winner(f"Player {self.game.winner} wins!")
        elif self.game.is_draw():
            self.show_winner("It's a draw!")
        else:
            self.status_label.config(text=f"Player {self.game.current_player}'s turn")
    def show_winner(self, message):
        '''
        Display the winner or draw message.
        '''
        self.status_label.config(text=message)
        for button in self.buttons:
            button.config(state='disabled')