'''
Contains custom widget classes for the application.
'''
import tkinter as tk
class CustomWidget(tk.Frame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.label = tk.Label(self, text="Custom Widget")
        self.label.pack()