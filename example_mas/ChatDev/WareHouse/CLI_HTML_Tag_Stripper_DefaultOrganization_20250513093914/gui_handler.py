'''
Handles graphical user interface operations for the HTML stripping application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from html_stripper import HTMLStripper
import os
class GUIHandler:
    def __init__(self):
        '''
        Initializes the GUI components.
        '''
        if not os.environ.get('DISPLAY'):
            print("No display environment detected. Please run in CLI mode or set up a display environment.")
            return
        self.root = tk.Tk()
        self.root.title("HTML Stripper")
        self.create_widgets()
    def create_widgets(self):
        '''
        Creates and places GUI widgets.
        '''
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.pack()
        self.strip_button = tk.Button(self.root, text="Strip HTML", command=self.strip_html)
        self.strip_button.pack()
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()
    def strip_html(self):
        '''
        Strips HTML tags from the input text and displays the result.
        '''
        input_content = self.input_text.get("1.0", tk.END)
        stripped_content = HTMLStripper.strip_html_tags(input_content)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, stripped_content)
    def run(self):
        '''
        Starts the GUI event loop.
        '''
        if hasattr(self, 'root'):
            self.root.mainloop()