'''
Contains the FileRenamerGUI class which creates the GUI for the application.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_renamer import FileRenamer
class FileRenamerGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Renamer")
        self.directory = ""
        self.file_renamer = FileRenamer()
        # GUI Components
        self.directory_label = tk.Label(self.root, text="No directory selected")
        self.directory_label.pack()
        self.select_button = tk.Button(self.root, text="Select Directory", command=self.select_directory)
        self.select_button.pack()
        self.prefix_entry = tk.Entry(self.root)
        self.prefix_entry.pack()
        self.prefix_entry.insert(0, "Enter prefix")
        self.replace_entry_old = tk.Entry(self.root)
        self.replace_entry_old.pack()
        self.replace_entry_old.insert(0, "Enter old substring")
        self.replace_entry_new = tk.Entry(self.root)
        self.replace_entry_new.pack()
        self.replace_entry_new.insert(0, "Enter new substring")
        self.start_number_entry = tk.Entry(self.root)
        self.start_number_entry.pack()
        self.start_number_entry.insert(0, "Enter start number")
        self.rename_button = tk.Button(self.root, text="Rename Files", command=self.rename_files)
        self.rename_button.pack()
    def select_directory(self):
        self.directory = filedialog.askdirectory()
        self.directory_label.config(text=self.directory)
    def rename_files(self):
        if not self.directory:
            messagebox.showerror("Error", "Please select a directory")
            return
        prefix = self.prefix_entry.get()
        old_substring = self.replace_entry_old.get()
        new_substring = self.replace_entry_new.get()
        try:
            start_number = int(self.start_number_entry.get())
        except ValueError:
            messagebox.showerror("Error", "Start number must be an integer")
            return
        if prefix:
            self.file_renamer.add_prefix(self.directory, prefix)
        if old_substring and new_substring:
            self.file_renamer.replace_substring(self.directory, old_substring, new_substring)
        if start_number > 0:
            self.file_renamer.add_sequential_numbers(self.directory, start_number)
        messagebox.showinfo("Success", "Files renamed successfully")
    def run(self):
        self.root.mainloop()