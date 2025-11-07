```markdown
# JSON Viewer CLI Application

A simple command-line interface (CLI) application to view the contents of a JSON file in a human-readable, indented format.

## Introduction

The JSON Viewer CLI application allows users to easily view and format JSON files directly from the command line. It reads a JSON file, formats it with indentation for better readability, and prints the formatted JSON to the standard output. This tool is particularly useful for developers and data analysts who frequently work with JSON data.

## Main Functions

- **Format and Display JSON**: The application reads a JSON file from a specified file path, formats it with indentation, and prints it to the console.
- **Error Handling**: Provides clear error messages if the file is not found, is not a valid JSON, or if any other error occurs during processing.

## Installation

### Environment Setup

This application requires Python 3.6 or higher. No external dependencies are needed beyond the standard Python library.

1. **Ensure Python is Installed**: Verify that Python 3.6 or higher is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

2. **Clone the Repository**: Clone the project repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

3. **Navigate to the Project Directory**: Change into the project directory:

   ```bash
   cd <project-directory>
   ```

## Usage

### Running the CLI Application

1. **Open a Terminal**: Open your command-line interface (CLI) on your operating system.

2. **Execute the Application**: Run the application by providing the path to the JSON file you want to view. Use the following command:

   ```bash
   python main.py <path_to_json_file>
   ```

   Replace `<path_to_json_file>` with the actual path to your JSON file.

3. **View the Output**: The formatted JSON will be printed to the console. If there are any errors, such as the file not being found or being invalid JSON, an error message will be displayed.

### Example

To view a JSON file located at `/path/to/your/file.json`, use the following command:

```bash
python main.py /path/to/your/file.json
```

### Error Messages

- **File Not Found**: If the specified file path does not exist, you will see an error message like:

  ```
  Error: The file '/path/to/your/file.json' was not found.
  ```

- **Invalid JSON**: If the file is not a valid JSON, the error message will be:

  ```
  Error: The file '/path/to/your/file.json' is not a valid JSON file.
  ```

- **General Errors**: Any other errors will be displayed with a message indicating the issue.

## Conclusion

The JSON Viewer CLI application is a straightforward tool for formatting and viewing JSON files directly from the command line. With its simple setup and usage, it is an essential utility for anyone working with JSON data.

For further assistance or to report issues, please contact our support team.
```
