'''
Contains the GUI logic for the application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from code_counter import CodeCounter
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Code Line Counter")
        self.counter = CodeCounter()
        self.label = tk.Label(self.root, text="Select a directory to count lines of code:")
        self.label.pack(pady=10)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)
        self.result_text = tk.Text(self.root, height=15, width=50)
        self.result_text.pack(pady=10)
    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            results = self.counter.count_lines(directory)
            self.display_results(results)
    def display_results(self, results):
        self.result_text.delete(1.0, tk.END)
        for ext, count in results.items():
            self.result_text.insert(tk.END, f"{ext}: {count} lines\n")
    def run(self):
        self.root.mainloop()