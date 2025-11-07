```markdown
# CLI Utility for Adding Line Numbers to Text Files

This utility is a command-line interface (CLI) application designed to add line numbers to a text file. It can output the result to a new file or print it directly to the standard output.

## Main Functions

- **Read a Text File**: The utility reads the content of a specified text file.
- **Add Line Numbers**: It processes the content to prepend each line with its corresponding line number.
- **Output the Result**: The processed content can be saved to a new file or printed to the console.

## Quick Install

This project uses only Python's standard library modules, so there are no external dependencies to install. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**: Download or clone the repository to your local machine.

2. **Navigate to the Project Directory**: Open your terminal and navigate to the directory containing the project files.

3. **Run the Application**: Use the following command to run the application:

   ```bash
   python main.py <input_file> [-o <output_file>]
   ```

   - `<input_file>`: Path to the input text file you want to process.
   - `-o <output_file>`: (Optional) Path to the output text file. If not provided, the output will be printed to the standard output.

### Examples

- **Output to Standard Output**:

  To add line numbers to `example.txt` and print the result to the console:

  ```bash
  python main.py example.txt
  ```

- **Output to a New File**:

  To add line numbers to `example.txt` and save the result to `numbered_example.txt`:

  ```bash
  python main.py example.txt -o numbered_example.txt
  ```

## Error Handling

If an error occurs (e.g., file not found), the application will print an error message to the console.

## Documentation

For further details on the implementation and code structure, refer to the source code files:

- `main.py`: Contains the main application logic.
- `file_operations.py`: Contains functions for reading files, adding line numbers, and writing files.

This utility is a simple yet effective tool for adding line numbers to text files, enhancing readability and organization.
```