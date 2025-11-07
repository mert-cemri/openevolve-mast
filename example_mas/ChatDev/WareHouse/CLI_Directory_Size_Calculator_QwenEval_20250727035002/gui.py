'''
Contains the GUI class for the graphical user interface using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from directory_size_calculator import DirectorySizeCalculator
class GUI:
    def __init__(self):
        '''
        Initialize the GUI components.
        '''
        self.root = tk.Tk()
        self.root.title("Directory Size Calculator")
        self.root.geometry("400x200")
        self.label = tk.Label(self.root, text="Select a directory to calculate its size:")
        self.label.pack(pady=10)
        self.button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.button.pack(pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.pack(pady=10)
    def browse_directory(self):
        '''
        Open a file dialog to select a directory and calculate its size.
        '''
        directory = filedialog.askdirectory()
        if not directory:
            messagebox.showwarning("No Directory Selected", "Please select a directory.")
            return
        try:
            calculator = DirectorySizeCalculator(directory)
            size = calculator.calculate_size()
            formatted_size = calculator.format_size(size)
            self.result_label.config(text=f"Total size of {directory}: {formatted_size}")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def run(self):
        '''
        Start the GUI event loop.
        '''
        self.root.mainloop()