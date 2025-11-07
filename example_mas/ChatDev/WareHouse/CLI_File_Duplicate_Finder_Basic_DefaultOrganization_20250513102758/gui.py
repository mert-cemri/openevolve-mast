'''
Contains the DuplicateFileFinderGUI class which implements the GUI for the application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from finder import DuplicateFileFinder
class DuplicateFileFinderGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Duplicate File Finder")
        self.finder = DuplicateFileFinder()
        self.directory_label = tk.Label(self.root, text="Select a directory:")
        self.directory_label.pack()
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.pack()
        self.result_text = tk.Text(self.root, wrap='word', height=15, width=50)
        self.result_text.pack()
    def browse_directory(self):
        '''Opens a dialog to select a directory and displays duplicates.'''
        directory = filedialog.askdirectory()
        if directory:
            duplicates = self.finder.find_duplicates(directory)
            self.display_duplicates(duplicates)
    def display_duplicates(self, duplicates):
        '''Displays the list of duplicate files found.'''
        self.result_text.delete(1.0, tk.END)
        if duplicates:
            for dup in duplicates:
                self.result_text.insert(tk.END, f"Duplicate: {dup[0]} and {dup[1]}\n")
        else:
            self.result_text.insert(tk.END, "No duplicates found.")
    def run(self):
        '''Runs the main loop of the GUI application.'''
        self.root.mainloop()