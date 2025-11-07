'''
GUI module for the JSON viewer application using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
import json
class JsonViewer:
    '''
    A class to create and manage the GUI window for viewing JSON files.
    '''
    def __init__(self, master):
        '''
        Initializes the GUI components.
        :param master: The root window.
        '''
        self.master = master
        self.master.title("JSON Viewer")
        self.text = tk.Text(self.master, wrap='word')
        self.text.pack(expand=1, fill='both')
        self.menu = tk.Menu(self.master)
        self.master.config(menu=self.menu)
        self.file_menu = tk.Menu(self.menu, tearoff=0)
        self.menu.add_cascade(label="File", menu=self.file_menu)
        self.file_menu.add_command(label="Open", command=self.open_file)
        self.file_menu.add_separator()
        self.file_menu.add_command(label="Exit", command=self.master.quit)
    def open_file(self):
        '''
        Opens a file dialog to select a JSON file.
        '''
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.display_json(file_path)
    def display_json(self, file_path):
        '''
        Displays the formatted JSON in a text widget.
        :param file_path: Path to the JSON file.
        '''
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)
            formatted_json = json.dumps(data, indent=4)
            self.text.delete(1.0, tk.END)
            self.text.insert(tk.END, formatted_json)
        except Exception as e:
            messagebox.showerror("Error", f"Error reading or formatting JSON file: {e}")