'''
Defines the GUI class to manage the graphical user interface.
'''
import tkinter as tk
import os
class GUI:
    def __init__(self, game):
        self.game = game
        # Check if running in a headless environment and set up a virtual display if necessary
        if not os.environ.get('DISPLAY'):
            os.environ['DISPLAY'] = ':0'  # Set a default display if none is set
        self.root = tk.Tk()
        self.root.title("Interactive Storytelling Game")
        self.text_area = tk.Text(self.root, wrap='word', height=15, width=50)
        self.text_area.pack(pady=10)
        self.choice_buttons = []
        for i in range(3):  # Assuming a maximum of 3 choices
            button = tk.Button(self.root, text="", command=lambda i=i: self.make_choice(i))
            button.pack(fill='x', pady=5)
            self.choice_buttons.append(button)
    def run(self):
        self.root.mainloop()
    def update_display(self, segment):
        text, choices = segment.display()
        self.text_area.delete(1.0, tk.END)
        self.text_area.insert(tk.END, text)
        for i, choice in enumerate(choices):
            self.choice_buttons[i].config(text=choice.text, state=tk.NORMAL)
        for i in range(len(choices), len(self.choice_buttons)):
            self.choice_buttons[i].config(text="", state=tk.DISABLED)
    def make_choice(self, index):
        choice = self.game.segments[self.game.current_segment].choices[index]
        self.game.make_choice(choice)