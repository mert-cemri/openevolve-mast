# Log File Analyzer User Manual

## Overview

The Log File Analyzer is a command-line tool designed to analyze log files and count the number of lines containing a specified pattern. This tool is particularly useful for system administrators, developers, and IT professionals who need to quickly identify and analyze specific events or errors in log files.

## Main Functions

- **Pattern Search:** The tool searches for a specified pattern within the log file and counts the number of lines that contain this pattern.
- **User-Friendly CLI:** The tool provides a simple and intuitive command-line interface for easy usage.
- **Error Handling:** The tool includes robust error handling to manage common issues such as file not found or permission errors.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download Python from [here](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/LogFileAnalyzer.git
   cd LogFileAnalyzer
   ```

2. **Install Dependencies:**

   The Log File Analyzer does not require any external dependencies. However, ensure that Python is correctly installed and added to your system's PATH.

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: In this case, `requirements.txt` is empty as no external dependencies are required.)*

## Usage

### Command-Line Interface (CLI)

1. **Run the Tool:**

   Use the following command to run the Log File Analyzer from the command line:

   ```bash
   python main.py <log_file> <pattern>
   ```

   Replace `<log_file>` with the path to your log file and `<pattern>` with the pattern you want to search for.

2. **Example:**

   ```bash
   python main.py access.log ERROR
   ```

   This command will search for the pattern "ERROR" in the `access.log` file and display the number of lines containing this pattern.

### Graphical User Interface (GUI)

The Log File Analyzer also includes a graphical user interface (GUI) for users who prefer a more visual approach.

1. **Run the GUI:**

   Use the following command to start the GUI:

   ```bash
   python gui_interface.py
   ```

2. **Using the GUI:**

   - **Browse for Log File:** Click the "Browse" button to select the log file you want to analyze.
   - **Enter Pattern:** Enter the pattern you want to search for in the "Pattern" field.
   - **Analyze Log:** Click the "Analyze" button to start the analysis. The result will be displayed in a message box.

## Troubleshooting

### Common Issues

- **File Not Found:** Ensure that the path to the log file is correct and that the file exists.
- **Permission Denied:** Ensure that you have the necessary permissions to read the log file.
- **Pattern Not Found:** If no lines contain the specified pattern, the tool will display a count of 0.

### Contact Support

If you encounter any issues or have questions about the Log File Analyzer, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## Conclusion

The Log File Analyzer is a powerful tool for analyzing log files and identifying specific patterns. With its user-friendly CLI and GUI interfaces, it is easy to use and can be a valuable asset for anyone working with log files.

---

This manual provides a comprehensive guide on how to install, use, and troubleshoot the Log File Analyzer. It covers both the command-line and graphical interfaces, ensuring that users can choose the method that best suits their needs.