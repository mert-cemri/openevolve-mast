'''
Module to handle the graphical user interface for the JSON to CSV converter.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from converter import convert_json_to_csv
class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("JSON to CSV Converter")
        self.geometry("400x250")
        self.input_path = tk.StringVar()
        self.output_path = tk.StringVar()
        self.fields = tk.StringVar()
        self.create_widgets()
    def create_widgets(self):
        tk.Label(self, text="Input JSON File:").grid(row=0, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.input_path, width=40).grid(row=0, column=1, padx=10, pady=10)
        tk.Button(self, text="Browse", command=self.select_input_file).grid(row=0, column=2, padx=10, pady=10)
        tk.Label(self, text="Output CSV File:").grid(row=1, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.output_path, width=40).grid(row=1, column=1, padx=10, pady=10)
        tk.Button(self, text="Browse", command=self.select_output_file).grid(row=1, column=2, padx=10, pady=10)
        tk.Label(self, text="Fields (comma-separated):").grid(row=2, column=0, padx=10, pady=10)
        tk.Entry(self, textvariable=self.fields, width=40).grid(row=2, column=1, padx=10, pady=10)
        tk.Button(self, text="Convert", command=self.convert).grid(row=3, column=1, pady=20)
    def select_input_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("JSON files", "*.json")])
        if file_path:
            self.input_path.set(file_path)
    def select_output_file(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files", "*.csv")])
        if file_path:
            self.output_path.set(file_path)
    def convert(self):
        input_path = self.input_path.get()
        output_path = self.output_path.get()
        fields = self.fields.get().split(',') if self.fields.get() else None
        if not input_path or not output_path:
            messagebox.showerror("Error", "Input and output file paths are required.")
            return
        try:
            convert_json_to_csv(input_path, output_path, fields)
            messagebox.showinfo("Success", "Conversion completed successfully.")
        except FileNotFoundError:
            messagebox.showerror("Error", f"The file {input_path} does not exist.")
        except json.JSONDecodeError:
            messagebox.showerror("Error", f"The file {input_path} is not a valid JSON file.")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {str(e)}")