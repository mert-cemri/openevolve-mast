'''
Optional GUI using tkinter for visual representation.
'''
import tkinter as tk
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Adventure Game")
    def create_gui(self):
        label = tk.Label(self.root, text="Adventure Game GUI")
        label.pack()
        self.root.mainloop()