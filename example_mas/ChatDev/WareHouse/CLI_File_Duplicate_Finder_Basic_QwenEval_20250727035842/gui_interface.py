'''
Module containing the GUIInterface class for handling the graphical user interface.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_hasher import FileHasher
from duplicate_finder import DuplicateFinder
class GUIInterface:
    def run(self):
        '''Start the GUI application.'''
        root = tk.Tk()
        root.title("Duplicate File Finder")
        root.geometry("400x200")
        self.label = tk.Label(root, text="Select a directory to scan for duplicates.")
        self.label.pack(pady=20)
        self.button = tk.Button(root, text="Browse", command=self.browse_directory)
        self.button.pack(pady=10)
        root.mainloop()
    def browse_directory(self):
        '''Open a file dialog to select a directory.'''
        directory = filedialog.askdirectory()
        if directory:
            self.scan_directory(directory)
    def scan_directory(self, directory):
        '''Scan the selected directory for duplicate files.'''
        file_hasher = FileHasher()
        file_hashes = file_hasher.hash_directory(directory)
        duplicate_finder = DuplicateFinder(file_hashes)
        duplicates = duplicate_finder.find_duplicates()
        if duplicates:
            message = "Duplicate files found:\n"
            for hash_value, paths in duplicates.items():
                message += f"Hash: {hash_value}\n"
                for path in paths:
                    message += f"  {path}\n"
        else:
            message = "No duplicate files found."
        messagebox.showinfo("Results", message)