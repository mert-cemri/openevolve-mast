# Lines of Code Counter CLI Program

## Quick Overview

The Lines of Code Counter is a command-line interface (CLI) program designed to count the total lines of code in a specified directory, categorized by file extension. It can also be run with a graphical user interface (GUI) for those who prefer a visual approach. The program ignores comments and blank lines to provide an accurate count of actual code.

## Main Functions

### CLI Mode

- **Count Lines of Code:** The program traverses the specified directory and counts lines of code for each file extension, ignoring comments and blank lines.
- **Output:** The results are displayed in the console, showing the number of lines for each file extension.

### GUI Mode

- **Select Directory:** Users can select a directory through a file dialog.
- **Count Lines of Code:** The program counts lines of code for each file extension in the selected directory, ignoring comments and blank lines.
- **Display Results:** The results are shown in a message box.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- No third-party dependencies are required for this project.

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/lines-of-code-counter.git
   cd lines-of-code-counter
   ```

2. **Install Python:**

   Ensure Python is installed by running:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from the [official website](https://www.python.org/downloads/).

3. **Verify Installation:**

   Run the following command to verify that the program is installed correctly:

   ```bash
   python main.py -h
   ```

   This should display the help message for the CLI program.

## Usage

### CLI Mode

1. **Count Lines of Code in a Directory:**

   ```bash
   python main.py -d /path/to/directory
   ```

   Replace `/path/to/directory` with the path to the directory you want to analyze.

2. **Example:**

   ```bash
   python main.py -d ./example_project
   ```

   This will count the lines of code in the `example_project` directory and display the results in the console.

### GUI Mode

1. **Run the GUI:**

   ```bash
   python main.py -g
   ```

2. **Select Directory:**

   - A window will appear with a "Select Directory" button.
   - Click the button to choose the directory you want to analyze.

3. **View Results:**

   - After selecting the directory, the program will count the lines of code and display the results in a message box.

## Supported File Extensions

The program currently supports the following file extensions:

- `.py` (Python)
- `.js` (JavaScript)
- `.c` (C)
- `.cpp` (C++)
- `.h` (C/C++ Header)

If you need to add support for additional file extensions, you can modify the `is_comment_line` function in `utils.py` to handle the specific comment syntax for those extensions.

## Troubleshooting

### Common Issues

- **File Encoding Errors:**

  If you encounter encoding errors while reading files, ensure that the files are encoded in UTF-8. You can modify the `encoding` parameter in the `open` function in `cli.py` if needed.

- **Permission Errors:**

  If you encounter permission errors while accessing files or directories, ensure that you have the necessary permissions to read the files.

### Contact Support

If you encounter any issues or have questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## Conclusion

The Lines of Code Counter is a powerful tool for developers and project managers to quickly assess the size and complexity of their codebases. Whether you prefer using the command line or a graphical interface, this program provides an easy and efficient way to count lines of code while ignoring comments and blank lines. Happy coding!

---

This manual should provide a comprehensive guide for users to understand and use the Lines of Code Counter CLI program effectively.