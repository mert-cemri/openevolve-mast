'''
This module contains the CLI version of the unit converter.
'''
import sys
from converter import Converter
class CLIConverter:
    def __init__(self):
        self.converter = Converter()
    def run(self):
        '''
        Run the CLI unit converter.
        This method reads command line arguments, performs the conversion,
        and prints the result.
        Raises:
        ValueError: If the input value is not a number or if the conversion is not supported.
        '''
        if len(sys.argv) != 4:
            print("Usage: python main.py <value> <source_unit> <target_unit>")
            sys.exit(1)
        try:
            value = float(sys.argv[1])
        except ValueError:
            print("Value must be a number.")
            sys.exit(1)
        source_unit = sys.argv[2].lower()
        target_unit = sys.argv[3].lower()
        try:
            result = self.converter.convert(value, source_unit, target_unit)
            print(f"{value} {source_unit} is equal to {result} {target_unit}")
        except ValueError as e:
            print(e)
            sys.exit(1)