# Duplicate Line Remover CLI Tool

Welcome to the Duplicate Line Remover CLI Tool! This tool is designed to help you remove duplicate lines from a text file while preserving the order of the first occurrence. You can choose to output the results to a new file or print them directly to the standard output.

## Main Functions

- **Remove Duplicate Lines**: The tool reads a text file, removes any duplicate lines, and retains the order of the first occurrence of each line.
- **Output Options**: You can specify an output file to save the results or print them directly to the console.

## Installation

### Prerequisites

- **Python Version**: Ensure you have Python 3.6 or higher installed on your system.

### Installing Dependencies

To install the necessary dependencies, you can use the following command:

```bash
pip install -r requirements.txt
```

This command will ensure that your environment is set up with the required Python version.

## Usage

### Running the Tool

To use the Duplicate Line Remover CLI Tool, you need to run the `main.py` script with the appropriate arguments.

#### Basic Command

```bash
python main.py <input_file>
```

- `<input_file>`: Path to the input text file from which you want to remove duplicate lines.

#### Optional Output File

If you want to save the output to a file, use the `-o` or `--output` option:

```bash
python main.py <input_file> -o <output_file>
```

- `<output_file>`: Path to the output text file where the results will be saved.

### Example

To remove duplicate lines from a file named `example.txt` and print the results to the console, use:

```bash
python main.py example.txt
```

To save the results to a file named `output.txt`, use:

```bash
python main.py example.txt -o output.txt
```

## Error Handling

- **File Not Found**: If the specified input file does not exist, the tool will return an error message indicating that the file was not found.
- **I/O Errors**: Any input/output errors encountered during file operations will be reported with a descriptive error message.

## Conclusion

The Duplicate Line Remover CLI Tool is a simple yet powerful utility for cleaning up text files by removing duplicate lines. Whether you need to process logs, data files, or any other text-based documents, this tool provides a straightforward solution. Enjoy using the tool, and feel free to reach out for support if needed!