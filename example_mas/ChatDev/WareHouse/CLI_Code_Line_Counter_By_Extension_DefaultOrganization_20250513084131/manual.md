```markdown
# Code Line Counter

A CLI and GUI application for counting lines of code in a directory, categorized by file extension.

## Overview

The Code Line Counter is a versatile tool designed to help developers quickly assess the volume of code in a directory. It categorizes the line count by file extension and excludes comments and blank lines, providing a more accurate representation of the actual codebase size.

## Main Functions

- **CLI Mode**: Use the command line interface to count lines of code in a specified directory.
- **GUI Mode**: A user-friendly graphical interface to select directories and view results.

## Installation

### Prerequisites

- Python 3.x installed on your system.

### Quick Install

Since there are no external dependencies required for this project, you can directly run the application using Python. However, ensure you have Python installed and properly configured in your system's PATH.

## How to Use

### CLI Mode

1. **Navigate to the Project Directory**: Open your terminal and navigate to the directory where the project files (`main.py` and `code_counter.py`) are located.

2. **Run the Application**: Use the following command to execute the CLI application:
   ```bash
   python main.py <directory_path>
   ```
   Replace `<directory_path>` with the path to the directory you wish to analyze.

3. **View Results**: The application will output the number of lines of code for each file extension present in the directory.

### GUI Mode

1. **Run the GUI Application**: Execute the `gui.py` file using Python:
   ```bash
   python gui.py
   ```

2. **Select Directory**: Click the "Browse" button to open a file dialog and select the directory you want to analyze.

3. **View Results**: The results will be displayed in the text area, showing the line count for each file extension.

## Additional Information

- **Supported File Extensions**: The application currently supports `.py`, `.js`, `.c`, `.cpp`, and `.java` files.
- **Comment Handling**: The application intelligently ignores single-line and multi-line comments, as well as blank lines, to provide an accurate count of actual code lines.

Feel free to explore and modify the code to extend functionality or add support for additional file types as needed.

```