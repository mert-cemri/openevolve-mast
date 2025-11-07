'''
GUI implementation for the Line Number Utility application.
Uses tkinter for the graphical user interface.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from line_number_utility import LineNumberUtility
class App:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Line Number Utility")
        self.root.geometry("400x200")
        self.input_file = None
        self.output_file = None
        self.create_widgets()
    def create_widgets(self):
        self.input_label = tk.Label(self.root, text="Input File:")
        self.input_label.pack()
        self.input_entry = tk.Entry(self.root, width=50)
        self.input_entry.pack()
        self.input_button = tk.Button(self.root, text="Browse", command=self.browse_input)
        self.input_button.pack()
        self.output_label = tk.Label(self.root, text="Output File (optional):")
        self.output_label.pack()
        self.output_entry = tk.Entry(self.root, width=50)
        self.output_entry.pack()
        self.output_button = tk.Button(self.root, text="Browse", command=self.browse_output)
        self.output_button.pack()
        self.process_button = tk.Button(self.root, text="Process", command=self.process_file)
        self.process_button.pack()
    def browse_input(self):
        self.input_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        self.input_entry.delete(0, tk.END)
        self.input_entry.insert(0, self.input_file)
    def browse_output(self):
        self.output_file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        self.output_entry.delete(0, tk.END)
        self.output_entry.insert(0, self.output_file)
    def process_file(self):
        if not self.input_file:
            messagebox.showerror("Error", "Please select an input file.")
            return
        try:
            utility = LineNumberUtility(self.input_file, self.output_file)
            utility.process_file()
            messagebox.showinfo("Success", "File processed successfully.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")
    def run(self):
        self.root.mainloop()