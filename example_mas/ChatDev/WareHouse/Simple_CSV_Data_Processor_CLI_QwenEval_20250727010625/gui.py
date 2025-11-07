'''
Handles the graphical user interface for the CSV Unique Values Finder application.
Allows the user to select a CSV file and specify a column name.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from csv_processor import CSVProcessor
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Unique Values Finder")
        self.file_path = None
        self.label = tk.Label(self.root, text="Select a CSV file and specify a column name:")
        self.label.pack(pady=10)
        self.file_button = tk.Button(self.root, text="Select File", command=self.select_file)
        self.file_button.pack(pady=5)
        self.column_label = tk.Label(self.root, text="Column Name:")
        self.column_label.pack(pady=5)
        self.column_entry = tk.Entry(self.root)
        self.column_entry.pack(pady=5)
        self.process_button = tk.Button(self.root, text="Process CSV", command=self.process_csv)
        self.process_button.pack(pady=10)
    def run(self):
        self.root.mainloop()
    def select_file(self):
        self.file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.file_path:
            messagebox.showinfo("File Selected", f"Selected file: {self.file_path}")
    def process_csv(self):
        if not self.file_path:
            messagebox.showerror("Error", "Please select a CSV file first.")
            return
        column_name = self.column_entry.get()
        if not column_name:
            messagebox.showerror("Error", "Please specify a column name.")
            return
        processor = CSVProcessor(self.file_path)
        try:
            unique_values = processor.get_unique_values(column_name)
            unique_values_str = "\n".join(unique_values)
            messagebox.showinfo("Unique Values", f"Unique values in column '{column_name}':\n{unique_values_str}")
        except KeyError:
            messagebox.showerror("Error", f"Column '{column_name}' not found in the CSV file.")