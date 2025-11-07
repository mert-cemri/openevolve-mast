'''
Module to handle the GUI interface for the unit converter.
'''
import tkinter as tk
from converter import Converter
class GUIConverter:
    def __init__(self):
        self.converter = Converter()
        self.root = tk.Tk()
        self.root.title("Unit Converter")
    def setup_ui(self):
        self.value_label = tk.Label(self.root, text="Value:")
        self.value_label.grid(row=0, column=0, padx=10, pady=10)
        self.value_entry = tk.Entry(self.root)
        self.value_entry.grid(row=0, column=1, padx=10, pady=10)
        self.source_label = tk.Label(self.root, text="Source Unit:")
        self.source_label.grid(row=1, column=0, padx=10, pady=10)
        self.source_entry = tk.Entry(self.root)
        self.source_entry.grid(row=1, column=1, padx=10, pady=10)
        self.target_label = tk.Label(self.root, text="Target Unit:")
        self.target_label.grid(row=2, column=0, padx=10, pady=10)
        self.target_entry = tk.Entry(self.root)
        self.target_entry.grid(row=2, column=1, padx=10, pady=10)
        self.convert_button = tk.Button(self.root, text="Convert", command=self.convert_and_display)
        self.convert_button.grid(row=3, column=0, columnspan=2, pady=10)
        self.result_label = tk.Label(self.root, text="")
        self.result_label.grid(row=4, column=0, columnspan=2, pady=10)
        self.root.mainloop()
    def convert_and_display(self):
        try:
            value = float(self.value_entry.get())
            source_unit = self.source_entry.get().strip().lower()
            target_unit = self.target_entry.get().strip().lower()
            result = self.converter.convert(value, source_unit, target_unit)
            self.result_label.config(text=f"{value} {source_unit} is {result} {target_unit}.")
        except ValueError as e:
            self.result_label.config(text=f"Error: {e}")
        except Exception as e:
            self.result_label.config(text=f"Unexpected error: {e}")