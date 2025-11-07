'''
Graphical user interface for generating a Markdown table from a CSV file.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from csv_parser import CSVParser
from markdown_generator import MarkdownGenerator
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("CSV to Markdown Table Generator")
        self.root.geometry("400x200")
        self.csv_file_path = tk.StringVar()
        self.md_file_path = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="CSV File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.csv_file_path, width=30).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_csv).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Markdown File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.md_file_path, width=30).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_md).grid(row=1, column=2, padx=10, pady=10)
        tk.Button(self.root, text="Generate", command=self.generate).grid(row=2, column=1, pady=20)
    def browse_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])
        self.csv_file_path.set(file_path)
    def browse_md(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".md", filetypes=[("Markdown files", "*.md")])
        self.md_file_path.set(file_path)
    def generate(self):
        csv_file_path = self.csv_file_path.get()
        md_file_path = self.md_file_path.get()
        if not csv_file_path or not md_file_path:
            messagebox.showerror("Error", "Please select both CSV and Markdown files.")
            return
        try:
            csv_parser = CSVParser()
            data = csv_parser.parse_csv(csv_file_path)
            md_generator = MarkdownGenerator()
            markdown_table = md_generator.generate_table(data)
            with open(md_file_path, 'w', encoding='utf-8') as f:
                f.write(markdown_table)
            messagebox.showinfo("Success", "Markdown table generated successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file {csv_file_path} does not exist.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        self.root.mainloop()