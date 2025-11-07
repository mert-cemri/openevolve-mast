# Text File Sorter CLI and GUI Application

## Overview

The Text File Sorter is a versatile application designed to sort the lines of a text file either alphabetically or in reverse alphabetical order. It supports both command-line interface (CLI) and graphical user interface (GUI) interactions, making it accessible to users with different preferences.

## Main Functions

- **CLI Mode**: Sorts lines of a text file based on command-line arguments and outputs the result to a new file or standard output.
- **GUI Mode**: Provides a user-friendly interface to select input and output files, choose sorting order, and execute the sorting process.

## Quick Install

To install the Text File Sorter, clone the repository and install the required dependencies:

```bash
git clone https://github.com/ChatDev/text-file-sorter.git
cd text-file-sorter
pip install -r requirements.txt
```

**Note**: No third-party dependencies are required for this project, as indicated in the `requirements.txt` file.

## 🤔 What is this?

The Text File Sorter is a simple yet powerful tool for sorting text files. It can be used in various scenarios, such as organizing data, preparing files for analysis, or simply cleaning up text files.

## 📖 Documentation

### CLI Mode

#### Usage

To use the CLI mode, run the following command:

```bash
python main.py <input_file> <output_file> [reverse]
```

- `<input_file>`: The path to the input text file.
- `<output_file>`: The path to the output text file. Use `stdout` to print the sorted lines to standard output.
- `[reverse]`: (Optional) If specified, the lines will be sorted in reverse alphabetical order.

#### Example

To sort a file named `input.txt` and save the sorted lines to `output.txt`:

```bash
python main.py input.txt output.txt
```

To sort the same file in reverse order and print the result to the console:

```bash
python main.py input.txt stdout reverse
```

### GUI Mode

#### Usage

To use the GUI mode, simply run the application without any command-line arguments:

```bash
python main.py
```

#### Steps

1. **Select Input File**: Click the "Browse" button next to the "Input File" field to select the text file you want to sort.
2. **Select Output File**: Click the "Browse" button next to the "Output File" field to select the destination file for the sorted lines. Alternatively, enter `stdout` to print the result to the console.
3. **Choose Sorting Order**: Check the "Reverse Sort" checkbox if you want to sort the lines in reverse alphabetical order.
4. **Sort**: Click the "Sort" button to execute the sorting process.

#### Example

1. Open the application by running `python main.py`.
2. Select `input.txt` as the input file.
3. Select `output.txt` as the output file.
4. Uncheck the "Reverse Sort" checkbox.
5. Click the "Sort" button to sort the file alphabetically and save the result to `output.txt`.

## Troubleshooting

- **FileNotFoundError**: Ensure that the input file exists and is accessible.
- **PermissionError**: Verify that you have the necessary permissions to read the input file and write to the output file.
- **General Errors**: Check the error message for more details and ensure that you are using the application correctly.

## Support

For any questions or issues, please contact our support team at support@chatdev.com. We are here to help you get the most out of the Text File Sorter.

---

This manual provides a comprehensive guide to using the Text File Sorter application, covering both CLI and GUI modes, installation, and troubleshooting.