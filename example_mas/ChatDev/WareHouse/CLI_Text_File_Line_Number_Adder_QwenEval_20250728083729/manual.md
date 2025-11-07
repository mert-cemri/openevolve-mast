# Line Number Utility User Manual

## Overview

The Line Number Utility is a command-line interface (CLI) tool designed to add line numbers to a text file. It can output the result either to a new file or directly to the standard output (console). This utility is particularly useful for developers, writers, and anyone who needs to add line numbers to their text files for better readability or reference.

## Main Functions

- **Add Line Numbers**: The primary function of the utility is to read a text file, add line numbers to each line, and then output the result.
- **Output Options**: Users can choose to save the output to a new file or display it directly in the console.
- **Error Handling**: The utility includes error handling for common issues such as file not found or read/write errors.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository**: If you have `git` installed, you can clone the repository using the following command:
   ```bash
   git clone https://github.com/ChatDev/line-number-utility.git
   cd line-number-utility
   ```

2. **Install Dependencies**: This utility does not require any external dependencies. However, if you want to ensure that all dependencies are listed, you can create a `requirements.txt` file with the following content:
   ```bash
   echo "" > requirements.txt
   ```
   Then, install the dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

The utility is accessed via the command line. Here are the basic commands and options:

#### Basic Command

To add line numbers to a file and display the output in the console, use the following command:
```bash
python main.py input.txt
```

#### Output to a New File

To add line numbers to a file and save the output to a new file, use the `-o` or `--output_file` option:
```bash
python main.py input.txt -o output.txt
```

### Example Scenarios

1. **Display Line Numbers in Console**
   ```bash
   python main.py example.txt
   ```
   This command will read `example.txt`, add line numbers to each line, and display the result in the console.

2. **Save Line Numbers to a New File**
   ```bash
   python main.py example.txt -o numbered_example.txt
   ```
   This command will read `example.txt`, add line numbers to each line, and save the result to `numbered_example.txt`.

## Troubleshooting

### Common Errors

- **FileNotFoundError**: This error occurs if the input file does not exist. Ensure that the file path is correct.
- **IOError**: This error occurs if there is an issue reading the input file or writing to the output file. Check file permissions and paths.

### Solutions

- **Check File Paths**: Ensure that the file paths provided are correct and that the files exist.
- **Permissions**: Ensure that you have the necessary permissions to read the input file and write to the output file.

## Conclusion

The Line Number Utility is a simple yet powerful tool for adding line numbers to text files. By following the installation and usage instructions provided in this manual, you should be able to use the utility effectively. If you encounter any issues, refer to the troubleshooting section or contact the support team for assistance.

---

This manual provides a comprehensive guide for users to understand and use the Line Number Utility effectively. It covers the main functions, installation steps, usage instructions, and troubleshooting tips.