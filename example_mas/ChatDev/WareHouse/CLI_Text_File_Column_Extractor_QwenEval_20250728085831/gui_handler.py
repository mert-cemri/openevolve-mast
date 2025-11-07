'''
Provides a graphical user interface for the user to interact with the program.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from file_reader import read_file
from column_extractor import extract_columns
from output_handler import output_data
def run_gui():
    root = tk.Tk()
    root.title("Column Extractor")
    file_path_var = tk.StringVar()
    columns_var = tk.StringVar()
    delimiter_var = tk.StringVar(value=',')
    output_path_var = tk.StringVar()
    def browse_file():
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt *.csv")])
        file_path_var.set(file_path)
    def browse_output():
        output_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        output_path_var.set(output_path)
    def extract_columns_gui():
        file_path = file_path_var.get()
        columns = columns_var.get()
        delimiter = delimiter_var.get()
        output_path = output_path_var.get()
        if not file_path or not columns:
            messagebox.showerror("Error", "Please provide a file path and columns to extract.")
            return
        try:
            data = read_file(file_path, delimiter)
            extracted_data = extract_columns(data, columns, delimiter)
            output_data(extracted_data, output_path, delimiter)
            messagebox.showinfo("Success", "Columns extracted successfully.")
        except Exception as e:
            messagebox.showerror("Error", str(e))
    tk.Label(root, text="File Path:").grid(row=0, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=file_path_var, width=50).grid(row=0, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=browse_file).grid(row=0, column=2, padx=10, pady=10)
    tk.Label(root, text="Columns:").grid(row=1, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=columns_var, width=50).grid(row=1, column=1, padx=10, pady=10)
    tk.Label(root, text="Delimiter:").grid(row=2, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=delimiter_var, width=50).grid(row=2, column=1, padx=10, pady=10)
    tk.Label(root, text="Output Path:").grid(row=3, column=0, padx=10, pady=10)
    tk.Entry(root, textvariable=output_path_var, width=50).grid(row=3, column=1, padx=10, pady=10)
    tk.Button(root, text="Browse", command=browse_output).grid(row=3, column=2, padx=10, pady=10)
    tk.Button(root, text="Extract Columns", command=extract_columns_gui).grid(row=4, column=1, padx=1 column=10 column=10 column=1 column=1 column=10, column=10 column=10 column=1 column=1 column=1 column=10 column=10, pady=row=row=row=row=row=10, pady=row=10 column=10 column=10, pady=row=row=row=10 column=10 column=10, pady=10 column=1 column=10, pady(row=10, pady=row=row=rowvariablevariable=row=row=10, pady=10, pady=10 column=10, pady=10, pady=row=row=10, pady=row=row(row=10, pady=10, pady(row=10 column=10, pady(row=10 column=10, pady=row(row=10, pady=row(row=10 column=10, pady=10 column=10 column=10, pady(row=10
``python_variable(row=10, padyvariablevariablevariablevariable(row=10