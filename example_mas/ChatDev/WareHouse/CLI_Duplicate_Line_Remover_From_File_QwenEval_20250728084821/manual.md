# Duplicate Line Remover CLI Tool

## Overview

The Duplicate Line Remover CLI Tool is a Python-based application designed to remove duplicate lines from a text file while preserving the order of the first occurrence. It supports both command-line interface (CLI) and graphical user interface (GUI) modes for user convenience.

## Quick Install

To install the Duplicate Line Remover CLI Tool, you need to have Python installed on your system. You can download Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository and install the required dependencies:

```bash
git clone https://github.com/ChatDev/DuplicateLineRemover.git
cd DuplicateLineRemover
pip install -r requirements.txt
```

Alternatively, you can install the tool directly from PyPI:

```bash
pip install duplicate-line-remover
```

## 🤔 What is this?

The Duplicate Line Remover CLI Tool is a utility that helps users clean up text files by removing duplicate lines. This can be particularly useful for data preprocessing, log file analysis, and other text processing tasks.

## 📖 Documentation

### Main Functions

1. **Remove Duplicate Lines**: The core functionality of the tool is to remove duplicate lines from a text file while preserving the order of the first occurrence.
2. **Command-Line Interface (CLI)**: Users can interact with the tool via the command line, specifying input and output files.
3. **Graphical User Interface (GUI)**: For users who prefer a graphical interface, the tool provides a simple GUI to select input and output files and execute the removal process.

### How to Use

#### Command-Line Interface (CLI)

To use the tool via the command line, navigate to the directory containing the `main.py` file and run the following command:

```bash
python main.py -i <input_file> [-o <output_file>]
```

- `<input_file>`: The path to the input text file from which duplicate lines will be removed.
- `<output_file>` (optional): The path to the output text file where the result will be saved. If not specified, the result will be printed to standard output.

**Example:**

```bash
python main.py -i input.txt -o output.txt
```

This command will read `input.txt`, remove duplicate lines, and save the result to `output.txt`.

#### Graphical User Interface (GUI)

To use the tool via the GUI, run the following command:

```bash
python gui.py
```

This will open a window where you can:

1. Select the input file by clicking the "Browse" button next to the "Input File" field.
2. Optionally, select the output file by clicking the "Browse" button next to the "Output File" field.
3. Click the "Submit" button to execute the removal process.

### Environment Dependencies

The tool requires Python 3.6 or higher. The following dependencies are listed in the `requirements.txt` file:

- `argparse`: For parsing command-line arguments (included in Python's standard library).
- `tkinter`: For creating the graphical user interface (included in Python's standard library).

These dependencies are automatically installed when you run `pip install -r requirements.txt` or `pip install duplicate-line-remover`.

## 🛠️ Troubleshooting

If you encounter any issues while using the tool, please check the following:

- Ensure that the input file path is correct and that the file exists.
- Verify that you have the necessary permissions to read the input file and write to the output file.
- Check the console or GUI for any error messages that may provide additional information.

If you need further assistance, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to install, understand, and use the Duplicate Line Remover CLI Tool effectively.