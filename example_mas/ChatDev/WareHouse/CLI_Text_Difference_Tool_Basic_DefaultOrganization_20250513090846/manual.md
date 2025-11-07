# CLI Text Difference Tool

A simple command-line interface (CLI) tool to compare two text files and highlight the lines that are different.

## Overview

The CLI Text Difference Tool is designed to help users quickly identify differences between two text files. It reads the files line by line and highlights any discrepancies, providing a clear and concise output of the differences.

## Quick Install

This tool does not require any external dependencies, making it easy to set up and use. Simply clone the repository and run the tool using Python.

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Ensure Python is Installed**

   Make sure you have Python installed on your system. This tool is compatible with Python 3.x.

## How to Use

The CLI Text Difference Tool is straightforward to use. It requires two text file paths as input and outputs the differences between them.

### Running the Tool

1. **Open a Terminal**

   Open a terminal or command prompt on your system.

2. **Execute the Tool**

   Run the tool using the following command:

   ```bash
   python main.py <file1> <file2>
   ```

   Replace `<file1>` and `<file2>` with the paths to the text files you want to compare.

### Example

Suppose you have two text files, `file1.txt` and `file2.txt`, and you want to compare them. You would run:

```bash
python main.py file1.txt file2.txt
```

### Output

The tool will output the differences line by line. For each differing line, it will show:

- The line number.
- The content of the line from each file that differs.

If the files are identical, it will output:

```
The files are identical.
```

## Documentation

For further details on the implementation and to contribute to the project, please refer to the source code files:

- `main.py`: The main application file that handles command-line arguments and outputs the differences.
- `file_comparator.py`: The module responsible for comparing the text files line by line.

## Support

For any issues or questions, please contact the development team through the repository's issue tracker.

---

This user manual provides all necessary information to install, run, and understand the CLI Text Difference Tool. Enjoy using the tool to efficiently compare your text files!