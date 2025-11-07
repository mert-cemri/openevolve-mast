```markdown
# Log Analyzer CLI Tool

Analyze log files efficiently with our Command Line Interface (CLI) tool. This tool allows users to specify a log file and a pattern to search for, counting and displaying lines that contain the specified pattern.

## Quick Install

This tool is developed using Python and requires Python version 3.6 or higher. No external packages are needed as it uses standard libraries only.

### Installation Steps

1. **Ensure Python is Installed**: Make sure you have Python 3.6 or higher installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the repository containing the CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

3. **Verify Python Version**: Check your Python version to ensure compatibility.

   ```bash
   python --version
   ```

4. **Run the Tool**: Once you have navigated to the directory containing the tool, you can run it using the following command:

   ```bash
   python main.py <file_path> <pattern>
   ```

   Replace `<file_path>` with the path to your log file and `<pattern>` with the pattern you want to search for.

## 🤔 What is this?

The Log Analyzer CLI Tool is designed to help users quickly analyze log files by searching for specific patterns. It is particularly useful for system administrators and developers who need to monitor logs for errors, specific HTTP status codes, or any other patterns of interest.

### Main Functions

- **Pattern Search**: Specify a log file and a pattern to search for. The tool will count and display the number of lines containing the pattern.

- **Error Handling**: The tool provides clear error messages if the specified log file is not found or if any other error occurs during execution.

## 📖 Usage

To use the Log Analyzer CLI Tool, follow these steps:

1. **Prepare Your Log File**: Ensure you have the log file you want to analyze ready and accessible.

2. **Run the Command**: Use the command format provided in the installation steps to run the tool. For example:

   ```bash
   python main.py /path/to/logfile.log ERROR
   ```

   This command will search for the pattern "ERROR" in the specified log file and display the count of lines containing this pattern.

3. **View Results**: The tool will output the number of lines containing the specified pattern, helping you quickly assess the presence of the pattern in your log file.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

Happy Logging!
```
