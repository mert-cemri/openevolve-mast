# Column Extractor CLI Tool

## Overview

The Column Extractor CLI Tool is a powerful utility designed to extract specific columns from CSV or space-delimited text files. Users can specify columns either by their numerical position or by their header names. This tool is particularly useful for data preprocessing, analysis, and manipulation tasks.

## Features

- **Command Line Interface (CLI)**: Easy to use from the terminal.
- **CSV and Space-Delimited Files**: Supports both file formats.
- **Column Specification**: Users can specify columns by number or header name.
- **Custom Delimiters**: Users can specify custom delimiters for space-delimited files.
- **Output Options**: Extracted data can be printed to the console or written to a new file.

## Quick Install

To use the Column Extractor CLI Tool, you need to have Python installed on your system. You can install the required dependencies using `pip`.

1. **Install Python**: Make sure you have Python installed. You can download it from [python.org](https://www.python.org/downloads/).

2. **Install Dependencies**: Run the following command to install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file should contain:

   ```
   csv
   ```

   Note: The `csv` module is part of Python's standard library, so no additional installation is required for it.

## Usage

### Basic Usage

The basic usage of the Column Extractor CLI Tool is as follows:

```bash
python main.py <file_path> <columns> [--delimiter <delimiter>] [--output <output_path>]
```

- `<file_path>`: Path to the input file.
- `<columns>`: Column numbers or headers to extract (comma-separated).
- `--delimiter`: Delimiter for the input file (default: comma).
- `--output`: Path to the output file (default: stdout).

### Examples

1. **Extract Columns by Number**

   To extract columns 1 and 3 from a CSV file:

   ```bash
   python main.py data.csv 1,3
   ```

2. **Extract Columns by Header**

   To extract columns named "Name" and "Age" from a CSV file:

   ```bash
   python main.py data.csv Name,Age
   ```

3. **Specify Custom Delimiter**

   To extract columns 1 and 3 from a space-delimited file:

   ```bash
   python main.py data.txt 1,3 --delimiter ' '
   ```

4. **Output to a File**

   To extract columns 1 and 3 from a CSV file and save the output to a new file:

   ```bash
   python main.py data.csv 1,3 --output output.csv
   ```

### GUI Usage

In addition to the CLI, the Column Extractor also provides a graphical user interface (GUI) for users who prefer a more visual approach.

1. **Run the GUI**

   Simply run the following command:

   ```bash
   python main.py
   ```

2. **Use the GUI**

   - **File Path**: Browse and select the input file.
   - **Columns**: Enter the column numbers or headers to extract (comma-separated).
   - **Delimiter**: Specify the delimiter for the input file (default: comma).
   - **Output Path**: Browse and select the output file (optional).
   - **Extract Columns**: Click the "Extract Columns" button to perform the extraction.

## Troubleshooting

### Common Issues

1. **Column Not Found**

   - **Error Message**: `Header 'X' not found in the file.`
   - **Solution**: Ensure that the header name is correct and exists in the file.

2. **Column Number Out of Range**

   - **Error Message**: `Column number X is out of range.`
   - **Solution**: Ensure that the column number is within the range of the file's columns.

### Contact Support

If you encounter any issues or have questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## Conclusion

The Column Extractor CLI Tool is a versatile and user-friendly utility for extracting specific columns from CSV or space-delimited text files. Whether you prefer using the command line or the graphical user interface, this tool provides a seamless experience for your data manipulation needs.

---

This manual should provide a comprehensive guide for users to understand and use the Column Extractor CLI Tool effectively. Let me know if you need any further modifications or additional sections!