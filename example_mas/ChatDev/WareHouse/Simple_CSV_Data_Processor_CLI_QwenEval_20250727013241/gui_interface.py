'''
Module to handle the graphical user interface for the CSV Unique Values Finder.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from csv_reader import CSVReader
from unique_values_finder import UniqueValuesFinder
class GUIInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV Unique Values Finder")
        self.filename = None
        self.column_name = None
        self.create_widgets()
    def create_widgets(self):
        self.label = tk.Label(self.root, text="Select a CSV file and specify a column name:")
        self.label.pack(pady=10)
        self.select_button = tk.Button(self.root, text="Select CSV File", command=self.select_file)
        self.select_button.pack(pady=5)
        self.column_label = tk.Label(self.root, text="Column Name:")
        self.column_label.pack(pady=5)
        self.column_entry = tk.Entry(self.root)
        self.column_entry.pack(pady=5)
        self.find_button = tk.Button(self.root, text="Find Unique Values", command=self.find_unique_values)
        self.find_button.pack(pady=10)
    def select_file(self):
        self.filename = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        if self.filename:
            messagebox.showinfo("File Selected", f"Selected file: {self.filename}")
    def find_unique_values(self):
        if not self.filename:
            messagebox.showwarning("No File Selected", "Please select a CSV file first.")
            return
        self.column_name = self.column_entry.get()
        if not self.column_name:
            messagebox.showwarning("No Column Name", "Please specify a column name.")
            return
        csv_reader = CSVReader(self.filename)
        csv_reader.read_csv()
        column_values = csv_reader.get_column_values(self.column_name)
        if not column_values:
            messagebox.showwarning("Column Not Found", f"Column '{self.column_name}' not found in the CSV file.")
            return
        unique_values_finder = UniqueValuesFinder(column_values)
        unique_values = unique_values_finder.find_unique_values()
        result = "\n".join(unique_values)
        messagebox.showinfo(f"Unique Values in '{self.column_name}'", f"Unique values:\n{result}")
    def run(self):
        self.root.mainloop()