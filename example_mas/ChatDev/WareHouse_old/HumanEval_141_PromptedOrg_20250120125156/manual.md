# File Name Check Software Manual

## Introduction

The File Name Check software is a Python-based utility designed to validate file names based on specific criteria. It determines whether a given file name is valid by checking against a set of predefined rules. This tool is useful for developers and users who need to ensure that file names adhere to certain standards before processing or storing them.

## Main Functionality

The core functionality of the software is encapsulated in the `file_name_check` function. This function evaluates a file name string and returns 'Yes' if the file name is valid according to the following criteria:

1. The file name contains exactly one dot ('.').
2. The substring before the dot is not empty and starts with a letter from the Latin alphabet ('a'-'z' or 'A'-'Z').
3. The substring after the dot is one of the following extensions: ['txt', 'exe', 'dll'].
4. There are no more than three digits ('0'-'9') in the file name.

If any of these conditions are not met, the function returns 'No'.

## Installation

### Environment Setup

The File Name Check software does not require any external dependencies, making it straightforward to set up and use. You only need a Python environment to run the software.

### Steps to Install

1. **Ensure Python is Installed**: Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone or Download the Repository**: Obtain the software by cloning the repository or downloading the source code files.

3. **Navigate to the Directory**: Open a terminal or command prompt and navigate to the directory containing the `main.py` file.

## Usage

To use the File Name Check software, follow these steps:

1. **Open a Terminal**: Open a terminal or command prompt.

2. **Run the Script**: Execute the `main.py` script using Python. You can do this by typing the following command:

   ```bash
   python main.py
   ```

3. **Test the Function**: You can test the `file_name_check` function by modifying the example usage at the bottom of the `main.py` file or by calling the function with different file name strings.

   Example usage:

   ```python
   print(file_name_check("example.txt"))  # Expected output: 'Yes'
   print(file_name_check("1example.dll")) # Expected output: 'No'
   ```

## Conclusion

The File Name Check software is a simple yet effective tool for validating file names based on specific criteria. With no external dependencies required, it is easy to integrate into existing Python projects or use as a standalone utility. By following the installation and usage instructions, you can quickly start validating file names to ensure they meet the necessary standards.