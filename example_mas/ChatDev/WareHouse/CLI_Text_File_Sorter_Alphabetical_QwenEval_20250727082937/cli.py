'''
Handles command-line interface interactions.
'''
import sys
from sorter import Sorter
from file_handler import FileHandler
class CLI:
    def __init__(self, args):
        self.args = args
    def run(self):
        if len(self.args) < 3:
            print("Usage: python main.py <input_file> <output_file> [reverse]")
            print("Use 'stdout' as <output_file> to print to standard output.")
            sys.exit(1)
        input_file = self.args[1]
        output_file = self.args[2]
        reverse = len(self.args) > 3 and self.args[3].lower() == 'reverse'
        sorter = Sorter()
        file_handler = FileHandler()
        try:
            lines = file_handler.read_file(input_file)
            sorted_lines = sorter.sort(lines, reverse)
            if output_file.lower() == 'stdout':
                for line in sorted_lines:
                    print(line, end='')
            else:
                file_handler.write_file(output_file, sorted_lines)
                print(f"Sorted lines written to {output_file}")
        except FileNotFoundError:
            print(f"Error: The file '{input_file}' does not exist.")
            sys.exit(1)
        except PermissionError:
            print(f"Error: Permission denied when trying to read '{input_file}'.")
            sys.exit(1)
        except Exception as e:
            print(f"An error occurred: {e}")
            sys.exit(1)