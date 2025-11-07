'''
Module to handle the CLI interface for the unit converter.
'''
from converter import Converter
class CLIConverter:
    def __init__(self):
        self.converter = Converter()
    def run(self):
        while True:
            try:
                value = float(input("Enter the value to convert (or type 'exit' to quit): "))
                source_unit = input("Enter the source unit (meters, feet, inches, cm): ").strip().lower()
                target_unit = input("Enter the target unit (meters, feet, inches, cm): ").strip().lower()
                result = self.converter.convert(value, source_unit, target_unit)
                print(f"{value} {source_unit} is {result} {target_unit}.")
            except ValueError as e:
                print(f"Error: {e}")
            except KeyboardInterrupt:
                print("\nExiting CLI mode.")
                break