```markdown
# CLI Text File Sorter

A simple command-line interface (CLI) application to sort the lines of a text file alphabetically or reverse-alphabetically and output the result to a new file or standard output.

## Quick Install

This application is built using Python's standard library and does not require any external dependencies. Ensure you have Python installed on your system.

## 🤔 What is this?

The CLI Text File Sorter is a tool designed to help users sort the lines of a text file. It can sort the lines in either alphabetical or reverse-alphabetical order and save the sorted lines to a new file. This tool is useful for organizing text data quickly and efficiently.

## Main Functions

- **Sort Lines Alphabetically**: Sorts the lines of a given text file in alphabetical order.
- **Sort Lines Reverse-Alphabetically**: Sorts the lines of a given text file in reverse-alphabetical order.
- **Output to File**: Saves the sorted lines to a specified output file.

## How to Use

### Running the Application

1. **Open your terminal or command prompt.**

2. **Navigate to the directory containing the application files** (`main.py` and `sorter.py`).

3. **Run the application using the following command:**

   ```bash
   python main.py <input_file> <output_file> [reverse]
   ```

   - `<input_file>`: The path to the text file you want to sort.
   - `<output_file>`: The path where you want to save the sorted lines.
   - `[reverse]`: Optional. Include this argument if you want to sort the lines in reverse-alphabetical order.

### Example Usage

- **Sort lines alphabetically**:

  ```bash
  python main.py input.txt output.txt
  ```

- **Sort lines reverse-alphabetically**:

  ```bash
  python main.py input.txt output.txt reverse
  ```

### Error Handling

If the application encounters an error (e.g., file not found, permission issues), it will print an error message and exit.

## 📖 Documentation

For further details on the implementation, refer to the source code files:

- **`main.py`**: Handles command-line arguments and calls the sorting function.
- **`sorter.py`**: Contains functions for reading, writing, and sorting lines in a text file.

This application leverages Python's built-in capabilities to provide a lightweight and efficient solution for text file sorting tasks.
```