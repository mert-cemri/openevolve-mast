'''
Defines the GUI class for the file joiner application using Tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_joiner import FileJoiner
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Joiner")
        self.file_joiner = FileJoiner()
        # Create and place widgets
        self.create_widgets()
    def create_widgets(self):
        # File selection
        self.file_label = tk.Label(self.root, text="Select the first part of the file:")
        self.file_label.pack(pady=5)
        self.file_entry = tk.Entry(self.root, width=50)
        self.file_entry.pack(pady=5)
        self.browse_button = tk.Button(self.root, text="Browse", command=self.browse_file)
        self.browse_button.pack(pady=5)
        # Output file name
        self.output_label = tk.Label(self.root, text="Enter the output file name:")
        self.output_label.pack(pady=5)
        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack(pady=5)
        # Join button
        self.join_button = tk.Button(self.root, text="Join", command=self.join_action)
        self.join_button.pack(pady=20)
    def browse_file(self):
        file_path = filedialog.askopenfilename(title="Select the first part of the file")
        self.file_entry.delete(0, tk.END)
        self.file_entry.insert(0, file_path)
    def join_action(self):
        first_part_name = self.file_entry.get()
        output_file_name = self.output_entry.get()
        if not first_part_name or not output_file_name:
            messagebox.showerror("Error", "Please provide both the first part file and the output file name.")
            return
        try:
            self.file_joiner.join_files(first_part_name, output_file_name)
            messagebox.showinfo("Success", "Files joined successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        self.root.mainloop()