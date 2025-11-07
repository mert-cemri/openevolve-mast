```markdown
# Log File Analyzer CLI

A command-line interface (CLI) program to analyze log files for specific patterns. This tool allows users to specify a log file and a pattern (e.g., "ERROR", "404") and outputs the count and lines containing the pattern.

## Quick Install

To use the Log File Analyzer CLI, ensure you have Python installed on your system. The program requires Python version 3.6 or higher.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Install Python Dependencies:**

   The program does not require any external dependencies. However, ensure you have Python 3.6 or higher installed. You can check your Python version with:

   ```bash
   python --version
   ```

   If you need to install Python, follow the instructions on the [official Python website](https://www.python.org/downloads/).

## 🤔 What is this?

The Log File Analyzer CLI is a simple yet powerful tool designed to help users quickly analyze log files. It searches for a specified pattern within the log file and provides a count of lines containing that pattern, along with the actual lines.

## 📖 How to Use

1. **Run the Program:**

   Execute the program using the following command:

   ```bash
   python main.py <file_path> <pattern>
   ```

   Replace `<file_path>` with the path to your log file and `<pattern>` with the string pattern you want to search for.

2. **Example Usage:**

   For example, to search for the pattern "ERROR" in a log file located at `/var/log/system.log`, use:

   ```bash
   python main.py /var/log/system.log ERROR
   ```

3. **Output:**

   The program will output the total number of lines containing the specified pattern and display each matching line.

   ```
   Total lines containing pattern 'ERROR': 5
   [Matching line 1]
   [Matching line 2]
   ...
   ```

## Troubleshooting

- **File Not Found Error:** Ensure the file path is correct and the file exists.
- **Permission Error:** Ensure you have the necessary permissions to read the log file.

For further assistance, please contact our support team.

```
