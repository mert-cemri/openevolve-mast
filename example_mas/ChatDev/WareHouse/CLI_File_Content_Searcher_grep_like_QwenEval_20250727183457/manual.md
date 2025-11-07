# User Manual for ChatDev's CLI Search Application

## Overview

ChatDev's CLI Search Application is a powerful tool designed to search for a given string or pattern within all text files in a specified directory and its subdirectories. This tool is similar to the Unix `grep -r` command and can be used for various purposes, such as code searching, document analysis, and more.

## Main Functions

- **Search Functionality:** The application searches for a specified string or pattern in all text files within a given directory and its subdirectories.
- **Pattern Matching:** Supports regular expressions for pattern matching.
- **Error Handling:** Provides informative error messages for issues such as non-existent directories or unreadable files.
- **Output:** Displays matching lines along with the filenames where the matches were found.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- The application does not have any external dependencies, so no additional packages need to be installed.

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/search-cli.git
   cd search-cli
   ```

2. **Run the Application:**
   Since there are no external dependencies, you can directly run the application using Python.
   ```bash
   python main.py <directory> <pattern>
   ```

## Usage

### Command-Line Arguments

- **Directory:** The directory to search in. This can be an absolute or relative path.
- **Pattern:** The string or pattern to search for. Supports regular expressions.

### Example Usage

1. **Search for a Simple String:**
   ```bash
   python main.py /path/to/directory "example string"
   ```

2. **Search Using a Regular Expression:**
   ```bash
   python main.py /path/to/directory "\d{3}-\d{2}-\d{4}"  # Example: Searching for SSN patterns
   ```

3. **Search in the Current Directory:**
   ```bash
   python main.py . "search term"
   ```

### Output

The application will display the matching lines along with the filenames where the matches were found. If no matches are found, it will display a message indicating that no matching lines were found.

### Error Handling

- **Directory Not Found:** If the specified directory does not exist, the application will display an error message.
- **File Read Errors:** If a file cannot be read (e.g., due to permission issues), the application will display an error message for that specific file and continue searching the remaining files.

## Troubleshooting

- **Python Version:** Ensure that you are using Python 3.6 or higher. You can check your Python version by running `python --version`.
- **Permissions:** Ensure that you have the necessary permissions to read the files and directories you are searching.

## Conclusion

ChatDev's CLI Search Application is a versatile tool for searching text files within directories and subdirectories. With its support for regular expressions and informative error handling, it can be a valuable addition to your toolkit for various text searching tasks.

If you encounter any issues or have suggestions for improvements, please feel free to reach out to our support team or contribute to the project on GitHub.

---

This manual provides a comprehensive guide on how to use the ChatDev CLI Search Application, including installation, usage, and troubleshooting steps.