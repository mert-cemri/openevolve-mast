# Text File Line Sorter CLI

Welcome to the Text File Line Sorter CLI, a command-line interface program designed to sort the lines of a text file alphabetically or in reverse alphabetical order. This tool is perfect for users who need to organize text data quickly and efficiently.

## Main Functions

The Text File Line Sorter CLI offers the following main functions:

- **Sort Alphabetically**: Sorts the lines of a text file in alphabetical order.
- **Sort Reverse-Alphabetically**: Sorts the lines of a text file in reverse alphabetical order.
- **Output Options**: Allows the sorted lines to be output to a new file or printed directly to the standard output (console).

## Installation

This program is written in Python and does not require any external dependencies. To run the program, ensure you have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

### Quick Install

No installation of additional packages is necessary. Simply clone the repository or download the source files to your local machine.

## How to Use

### Running the Program

1. **Open a Terminal**: Navigate to the directory where the source files (`main.py`, `sort_functions.py`, `file_functions.py`) are located.

2. **Execute the Program**: Use the following command to run the program:

   ```bash
   python main.py <input_file> [-o <output_file>] [-r]
   ```

   - `<input_file>`: The path to the text file you want to sort.
   - `-o <output_file>` (optional): The path to the output text file where the sorted lines will be saved. If not provided, the sorted lines will be printed to the console.
   - `-r` (optional): Include this flag to sort the lines in reverse alphabetical order.

### Examples

- **Sort Alphabetically and Print to Console**:

  ```bash
  python main.py example.txt
  ```

- **Sort Alphabetically and Save to a File**:

  ```bash
  python main.py example.txt -o sorted_example.txt
  ```

- **Sort Reverse-Alphabetically and Print to Console**:

  ```bash
  python main.py example.txt -r
  ```

- **Sort Reverse-Alphabetically and Save to a File**:

  ```bash
  python main.py example.txt -o sorted_example.txt -r
  ```

## Error Handling

If an error occurs (e.g., file not found, permission issues), the program will print an error message to the console. Ensure that the file paths are correct and that you have the necessary permissions to read from and write to the specified files.

## Conclusion

The Text File Line Sorter CLI is a simple yet powerful tool for organizing text data. Whether you need to sort lines alphabetically or in reverse order, this program provides a straightforward solution. Enjoy using the Text File Line Sorter CLI for your text processing needs!