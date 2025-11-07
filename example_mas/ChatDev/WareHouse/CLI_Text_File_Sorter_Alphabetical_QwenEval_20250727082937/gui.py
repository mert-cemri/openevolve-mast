'''
Handles graphical user interface interactions using tkinter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from sorter import Sorter
from file_handler import FileHandler
class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text File Sorter")
        self.root.geometry("400x200")
        self.input_file_path = tk.StringVar()
        self.output_file_path = tk.StringVar()
        self.reverse_sort = tk.BooleanVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self.root, text="Input File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.input_file_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_input_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self.root, text="Output File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self.root, textvariable=self.output_file_path, width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self.root, text="Browse", command=self.browse_output_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Checkbutton(self.root, text="Reverse Sort", variable=self.reverse_sort).grid(row=2, column=0, columnspan=3, pady=10)
        tk.Button(self.root, text="Sort", command=self.sort_file).grid(row=3, column=0, columnspan=3, pady=10)
    def browse_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text Files", "*.txt")])
        self.input_file_path.set(file_path)
    def browse_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        self.output_file_path.set(file_path)
    def sort_file(self):
        input_file = self.input_file_path.get()
        output_file = self.output_file_path.get()
        reverse = self.reverse_sort.get()
        if not input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        if not output_file:
            messagebox.showerror("Error", "Please select an output file or choose 'stdout'.")
            return
        sorter = Sorter()
        file_handler = FileHandler()
        try:
            lines = file_handler.read_file(input_file)
            sorted_lines = sorter.sort(lines, reverse)
            if output_file.lower() == 'stdout':
                output_text = ''.join(sorted_lines)
                messagebox.showinfo("Sorted Lines", output_text)
            else:
                file_handler.write_file(output_file, sorted_lines)
                messagebox.showinfo("Success", f"Sorted lines written to {output_file}")
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file '{input_file}' does not exist.")
        except PermissionError:
            messagebox.showerror("Error", f"Permission denied when trying to read '{input_file}'.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")
    def run(self):
        self.root.mainloop()