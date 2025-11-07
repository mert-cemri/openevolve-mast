'''
Contains the CodeCounterGUI class for the graphical user interface.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from code_counter import CodeCounter
class CodeCounterGUI:
    def __init__(self, master):
        self.master = master
        self.counter = CodeCounter()
        self.label = tk.Label(master, text="Select a directory to count lines of code:")
        self.label.pack(pady=10)
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)
        self.result_text = tk.Text(master, height=10, width=50)
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
        messagebox.showinfo("Results", "Line counting completed!")