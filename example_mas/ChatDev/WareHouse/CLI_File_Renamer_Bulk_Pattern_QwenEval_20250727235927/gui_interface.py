'''
Handles the graphical user interface for the File Renamer application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_renamer import FileRenamer
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Renamer")
        self.directory = ""
        self.create_widgets()
    def create_widgets(self):
        self.directory_label = tk.Label(self.root, text="Directory:")
        self.directory_label.grid(row=0, column=0, padx=10, pady=10)
        self.directory_entry = tk.Entry(self.root, width=50)
        self.directory_entry.grid(row=0, column=1, padx=10, pady=10)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_directory)
        self.browse_button.grid(row=0, column=2, padx=10, pady=10)
        self.prefix_label = tk.Label(self.root, text="Prefix:")
        self.prefix_label.grid(row=1, column=0, padx=10, pady=10)
        self.prefix_entry = tk.Entry(self.root, width=50)
        self.prefix_entry.grid(row=1, column=1, padx=10, pady=10)
        self.replace_label = tk.Label(self.root, text="Replace (old, new):")
        self.replace_label.grid(row=2, column=0, padx=10, pady=10)
        self.replace_old_entry = tk.Entry(self.root, width=25)
        self.replace_old_entry.grid(row=2, column=1, padx=10, pady=10)
        self.replace_new_entry = tk.Entry(self.root, width=25)
        self.replace_new_entry.grid(row=2, column=2, padx=10, pady=10)
        self.sequential_label = tk.Label(self.root, text="Sequential Start:")
        self.sequential_label.grid(row=3, column=0, padx=10, pady=10)
        self.sequential_entry = tk.Entry(self.root, width=50)
        self.sequential_entry.grid(row=3, column=1, padx=10, pady=10)
        self.rename_button = tk.Button(self.root, text="Rename", command=self.on_rename)
        self.rename_button.grid(row=4, column=1, padx=10, pady=10)
    def browse_directory(self):
        self.directory = filedialog.askdirectory()
        self.directory_entry.delete(0, tk.END)
        self.directory_entry.insert(0, self.directory)
    def on_rename(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a directory.")
            return
        try:
            renamer = FileRenamer(self.directory)
            prefix = self.prefix_entry.get()
            if prefix:
                renamer.add_prefix(prefix)
            replace_old = self.replace_old_entry.get()
            replace_new = self.replace_new_entry.get()
            if replace_old and replace_new:
                renamer.replace_substring(replace_old, replace_new)
            sequential_start = self.sequential_entry.get()
            if sequential_start:  # Check if sequential_entry is not empty
                try:
                    sequential_start = int(sequential_start)
                    renamer.add_sequential_numbers(sequential_start)
                except ValueError:
                    messagebox.showerror("Error", "Sequential start must be an integer.")
                    return
            messagebox.showinfo("Success", "Files have been renamed successfully.")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.root.mainloop()