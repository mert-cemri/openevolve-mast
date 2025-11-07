'''
Provides a graphical interface for the File Splitter application.
Allows users to select a file and specify the chunk size to split the file.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_splitter import FileSplitter
import os
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Splitter")
        self.root.geometry("400x200")
        self.file_path = tk.StringVar()
        self.chunk_size = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        """
        Creates and places the widgets in the GUI.
        """
        tk.Label(self.root, text="File Path:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Chunk Size (MB):").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.chunk_size, width=10).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Split File", command=self.on_split_button_click).grid(row=2, column=1, pady=20)
    def browse_file(self):
        """
        Opens a file dialog to select a file and sets the file path.
        """
        file_path = filedialog.askopenfilename()
        self.file_path.set(file_path)
    def on_split_button_click(self):
        """
        Handles the logic when the 'Split File' button is clicked.
        """
        file_path = self.file_path.get()
        chunk_size_mb = self.chunk_size.get()
        if not file_path or not chunk_size_mb:
            messagebox.showerror("Error", "Please provide both file path and chunk size.")
            return
        try:
            chunk_size = int(chunk_size_mb) * 1024 * 1024  # Convert MB to bytes
            if chunk_size <= 0:
                raise ValueError("Chunk size must be a positive integer.")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid chunk size: {e}")
            return
        if not os.path.isfile(file_path):
            messagebox.showerror("Error", f"The file '{file_path}' does not exist.")
            return
        splitter = FileSplitter()
        splitter.split_file(file_path, chunk_size)
        messagebox.showinfo("Success", "File has been split successfully.")
    def run(self):
        """
        Starts the GUI event loop.
        """
        self.root.mainloop()