'''
This is the main module to run the tic-tac-toe game with a graphical user interface.
'''
import tkinter as tk
from game import Game
class TicTacToeGUI:
    def __init__(self, root):
        '''Initialize the GUI and game logic.'''
        self.root = root
        self.root.title("Tic-Tac-Toe")
        self.game = Game()
        self.buttons = []
        self.create_board()
    def create_board(self):
        '''Create the game board with buttons.'''
        for i in range(9):
            button = tk.Button(self.root, text=' ', font='Arial 20', width=5, height=2,
                               command=lambda i=i: self.on_button_click(i))
            button.grid(row=i//3, column=i%3)
            self.buttons.append(button)
        restart_button = tk.Button(self.root, text='Restart', font='Arial 15', command=self.reset_game)
        restart_button.grid(row=4, column=0, columnspan=3)
    def on_button_click(self, position):
        '''Handle button click events.'''
        result = self.game.make_move(position)
        self.update_board()
        if result:
            self.show_result(result)
    def update_board(self):
        '''Update the board display based on the game state.'''
        for i, button in enumerate(self.buttons):
            button.config(text=self.game.board[i])
    def show_result(self, result):
        '''Display the result of the game.'''
        self.result_label = tk.Label(self.root, text=result, font='Arial 15')
        self.result_label.grid(row=3, column=0, columnspan=3)
        for button in self.buttons:
            button.config(state='disabled')
    def reset_game(self):
        '''Reset the game state and clear the result label.'''
        self.game = Game()
        for button in self.buttons:
            button.config(text=' ', state='normal')
        if hasattr(self, 'result_label'):
            self.result_label.destroy()
def main():
    '''Run the GUI application.'''
    root = tk.Tk()
    app = TicTacToeGUI(root)
    root.mainloop()
if __name__ == "__main__":
    main()