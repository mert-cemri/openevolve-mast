'''
Defines the GUI class to manage the graphical user interface.
'''
import tkinter as tk
class GUI:
    def __init__(self, game):
        self.game = game
        self.root = tk.Tk()
        self.root.title("Interactive Storytelling Game")
        self.text = tk.Text(self.root, wrap='word', height=10, width=50)
        self.text.pack()
        self.choice_buttons = []
    def display_node(self, node):
        self.text.delete(1.0, tk.END)
        self.text.insert(tk.END, node.text)
        for button in self.choice_buttons:
            button.destroy()
        self.choice_buttons = []
        for choice in node.get_choices():
            button = tk.Button(self.root, text=choice, command=lambda c=choice: self.on_choice(c))
            button.pack()
            self.choice_buttons.append(button)
    def on_choice(self, choice):
        self.game.make_choice(choice)
    def run(self):
        self.root.mainloop()