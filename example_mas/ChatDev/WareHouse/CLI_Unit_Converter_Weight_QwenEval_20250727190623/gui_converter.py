'''
This module contains the GUI version of the unit converter using tkinter.
'''
import tkinter as tk
from tkinter import messagebox
from converter import Converter
class GUIConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("Unit Converter")
        self.converter = Converter()
        # Add a label with supported units
        supported_units_label = tk.Label(root, text="Supported Units: kg, g, lb, oz")
        supported_units_label.grid(row=0, column=0, columnspan=2, pady=10)
        self.value_label = tk.Label(root, text="Value:")
        self.value_label.grid(row=1, column=0, padx=10, pady=10)
        self.value_entry = tk.Entry(root)
        self.value_entry.grid(row=1, column=1, padx=10, pady=10)
        self.source_label = tk.Label(root, text="Source Unit:")
        self.source_label.grid(row=2, column=0, padx=10, pady=10)
        self.source_entry = tk.Entry(root)
        self.source_entry.grid(row=2, column=1, padx=10, pady=10)
        self.target_label = tk.Label(root, text="Target Unit:")
        self.target_label.grid(row=3, column=0, padx=10, pady=10)
        self.target_entry = tk.Entry(root)
        self.target_entry.grid(row=3, column=1, padx=10, pady=10)
        self.convert_button = tk.Button(root, text="Convert", command=self.convert_and_display)
        self.convert_button.grid(row=4, column=0, columnspan=2, pady=10)
        self.result_label = tk.Label(root, text="")
        self.result_label.grid(row=5, column=0, columnspan=2, pady=10)
    def convert_and_display(self):
        try:
            value = float(self.value_entry.get())
            source_unit = self.source_entry.get().lower()
            target_unit = self.target_entry.get().lower()
            result = self.converter.convert(value, source_unit, target_unit)
            self.result_label.config(text=f"{value} {source_unit} is equal to {result} {target_unit}")
        except ValueError as e:
            messagebox.showerror("Error", str(e))
    def run(self):
        self.root.mainloop()