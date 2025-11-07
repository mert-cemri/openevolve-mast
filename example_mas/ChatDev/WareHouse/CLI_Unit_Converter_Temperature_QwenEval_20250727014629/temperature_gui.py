'''
Handles the GUI logic using tkinter.
'''
import tkinter as tk
from temperature_converter import TemperatureConverter
class TemperatureGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Temperature Converter")
        self.geometry("300x200")
        self.converter = TemperatureConverter()
        self.setup_ui()
    def setup_ui(self):
        self.label_value = tk.Label(self, text="Enter temperature:")
        self.label_value.pack()
        self.entry_value = tk.Entry(self)
        self.entry_value.pack()
        self.label_source = tk.Label(self, text="Source unit (C, F, K):")
        self.label_source.pack()
        self.entry_source = tk.Entry(self)
        self.entry_source.pack()
        self.label_target = tk.Label(self, text="Target unit (C, F, K):")
        self.label_target.pack()
        self.entry_target = tk.Entry(self)
        self.entry_target.pack()
        self.button_convert = tk.Button(self, text="Convert", command=self.convert_temperature)
        self.button_convert.pack()
        self.label_result = tk.Label(self, text="Result:")
        self.label_result.pack()
    def convert_temperature(self):
        try:
            value = float(self.entry_value.get())
            source_unit = self.entry_source.get().upper()
            target_unit = self.entry_target.get().upper()
            result = self.converter.convert(value, source_unit, target_unit)
            self.label_result.config(text=f"Result: {result:.2f} {target_unit}")
        except ValueError:
            self.label_result.config(text="Invalid input. Please enter a number.")