'''
Utility class to add line numbers to a text file.
Handles reading, processing, and writing the file.
'''
class LineNumberUtility:
    def __init__(self, input_file, output_file=None):
        self.input_file = input_file
        self.output_file = output_file
    def add_line_numbers(self):
        try:
            with open(self.input_file, 'r', encoding='utf-8') as file:
                lines = file.readlines()
        except FileNotFoundError:
            print(f"Error: The file {self.input_file} does not exist.")
            return None
        except IOError:
            print(f"Error: An error occurred while reading the file {self.input_file}.")
            return None
        numbered_lines = [f"{i+1}: {line}" for i, line in enumerate(lines)]
        return ''.join(numbered_lines)
    def write_to_file(self, content):
        try:
            with open(self.output_file, 'w', encoding='utf-8') as file:
                file.write(content)
            print(f"Line numbers added successfully. Output saved to {self.output_file}.")
        except IOError:
            print(f"Error: An error occurred while writing to the file {self.output_file}.")
    def print_to_stdout(self, content):
        print("Line numbers added successfully. Output:")
        print(content)
    def process_file(self):
        content = self.add_line_numbers()
        if content is None:
            return
        if self.output_file:
            self.write_to_file(content)
        else:
            self.print_to_stdout(content)