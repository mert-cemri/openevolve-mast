'''
This is the main file that initializes and runs the temperature converter CLI tool.
'''
import sys
from converter import TemperatureConverter
def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <value> <source_unit> <target_unit>")
        print("Example: python main.py 100 C F")
        return
    try:
        value = float(sys.argv[1])
        source = sys.argv[2].upper()
        target = sys.argv[3].upper()
        converter = TemperatureConverter()
        if source == target:
            result = value
        elif source == 'C' and target == 'F':
            result = converter.celsius_to_fahrenheit(value)
        elif source == 'C' and target == 'K':
            result = converter.celsius_to_kelvin(value)
        elif source == 'F' and target == 'C':
            result = converter.fahrenheit_to_celsius(value)
        elif source == 'F' and target == 'K':
            result = converter.fahrenheit_to_kelvin(value)
        elif source == 'K' and target == 'C':
            result = converter.kelvin_to_celsius(value)
        elif source == 'K' and target == 'F':
            result = converter.kelvin_to_fahrenheit(value)
        else:
            print("Invalid source or target unit. Use 'C', 'F', or 'K'.")
            return
        print(f"Converted: {result:.2f} {target}")
    except ValueError:
        print("Invalid input. Please enter a numeric value.")
if __name__ == "__main__":
    main()