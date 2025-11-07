'''
Provides a graphical user interface for the HTML stripping application using Tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from html_stripper import HTMLStripper
class GUI:
    def create_gui(self):
        '''
        Create the GUI window and handle user interactions.
        '''
        self.root = tk.Tk()
        self.root.title("HTML Stripper")
        self.input_text = tk.Text(self.root, height=10, width=50)
        self.input_text.pack()
        self.strip_button = tk.Button(self.root, text="Strip HTML", command=self.strip_html)
        self.strip_button.pack()
        self.output_text = tk.Text(self.root, height=10, width=50)
        self.output_text.pack()
        self.root.mainloop()
    def strip_html(self):
        '''
        Strip HTML tags from the input text and display the result.
        '''
        html_content = self.input_text.get("1.0", tk.END)
        stripped_content = HTMLStripper.strip_tags(html_content)
        self.output_text.delete("1.0", tk.END)
        self.output_text.insert(tk.END, stripped_content)