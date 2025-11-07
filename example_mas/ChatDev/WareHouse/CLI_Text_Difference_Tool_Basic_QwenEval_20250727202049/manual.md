# ChatDev Text Difference Tool

A simple Command Line Interface (CLI) tool to compare two text files and highlight the differences between them. This tool is designed to be easy to use and understand, providing a straightforward way to identify changes between two text files.

## Quick Install

To install the ChatDev Text Difference Tool, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Navigate to the directory containing the source code and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Note: Currently, there are no external dependencies for this tool, so the `requirements.txt` file might be empty. However, it's a good practice to include it for future updates.

## 🤔 What is this?

The ChatDev Text Difference Tool is a simple CLI application that takes two text file paths as input and highlights the lines that are different between the two files. This tool is particularly useful for developers, writers, and anyone who needs to compare text files for changes.

## 📖 Documentation

### Main Functions

1. **File Reading**: The `FileReader` class is responsible for reading the contents of the input files. It handles file not found errors and other exceptions that might occur during file reading.

2. **Text Comparison**: The `TextDiff` class compares the contents of the two files line by line. It identifies the lines that are different and returns a list of tuples containing the line number and the content of the lines from both files.

3. **CLI Interface**: The `CLIInterface` class handles command-line interactions. It reads the file paths from the command line arguments, uses the `FileReader` and `TextDiff` classes to compare the files, and displays the differences.

4. **GUI Interface**: The `GUIInterface` class provides a graphical user interface for the tool. It allows users to select the files using a file dialog, compare the files, and view the differences in a text area.

### How to Use

#### Command Line Interface

To use the ChatDev Text Difference Tool from the command line, navigate to the directory containing the `main.py` file and run the following command:

```bash
python main.py <file1_path> <file2_path>
```

Replace `<file1_path>` and `<file2_path>` with the paths to the two text files you want to compare.

Example:

```bash
python main.py file1.txt file2.txt
```

The tool will display the differences between the two files, highlighting the lines that are different.

#### Graphical User Interface

To use the ChatDev Text Difference Tool with the graphical user interface, navigate to the directory containing the `gui_interface.py` file and run the following command:

```bash
python gui_interface.py
```

A window will appear, allowing you to select the files using the "Browse" buttons, compare the files using the "Compare" button, and view the differences in the text area.

### Example

Suppose you have two text files, `file1.txt` and `file2.txt`, with the following contents:

**file1.txt**
```
Hello, World!
This is a test file.
Goodbye, World!
```

**file2.txt**
```
Hello, World!
This is a modified test file.
Goodbye, World!
```

Running the ChatDev Text Difference Tool with these files will produce the following output:

```
Differences found:
Line 2:
  File 1: This is a test file.
  File 2: This is a modified test file.
```

This output highlights the line that is different between the two files.

## Conclusion

The ChatDev Text Difference Tool is a simple and effective way to compare two text files and identify the differences between them. Whether you're a developer, writer, or anyone who needs to compare text files, this tool can help you quickly and easily identify changes.