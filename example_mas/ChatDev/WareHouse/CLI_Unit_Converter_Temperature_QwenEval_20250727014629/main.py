'''
Main entry point for the Temperature Conversion Tool.
Handles command-line arguments and performs temperature conversion.
'''
import argparse
from temperature_converter import TemperatureConverter
def main():
    parser = argparse.ArgumentParser(description="Convert temperatures between Celsius, Fahrenheit, and Kelvin.")
    parser.add_argument("value", type=float, help="The temperature value to convert.")
    parser.add_argument("source_unit", type=str, choices=['C', 'F', 'K'], help="The source unit (C, F, K).")
    parser.add_argument("target_unit", type=str, choices=['C', 'F', 'K'], help="The target unit (C, F, K).")
    args = parser.parse_args()
    converter = TemperatureConverter()
    result = converter.convert(args.value, args.source_unit, args.target_unit)
    print(f"Result: {result:.2f} {args.target_unit}")
if __name__ == "__main__":
    main()