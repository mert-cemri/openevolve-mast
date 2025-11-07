# YAML File Validator

## Quick Overview

The YAML File Validator is a command-line tool designed to check the syntax of YAML files. It reads a YAML file from a specified path and reports whether the file is valid or not. If the file contains errors, the tool will provide detailed error messages, including line numbers where the issues occur.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Steps to Install

1. **Clone the Repository** (if not already done):

   ```bash
   git clone https://github.com/ChatDev/YAML-File-Validator.git
   cd YAML-File-Validator
   ```

2. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   This command installs the required Python packages, including `PyYAML`, which is used for parsing YAML files.

## Usage

### Command-Line Interface (CLI)

The YAML File Validator is primarily designed to be used via the command line. Here's how you can use it:

1. **Run the Validator**:

   ```bash
   python main.py <path_to_your_yaml_file>
   ```

   Replace `<path_to_your_yaml_file>` with the actual path to your YAML file.

2. **Example**:

   ```bash
   python main.py example.yaml
   ```

   If the YAML file is valid, you will see:

   ```
   Success: The YAML file is valid.
   ```

   If the YAML file contains errors, you will see something like:

   ```
   Error: The YAML file is invalid.
   Line 5, Column 10: expected <block end>, but found '<scalar>'
   ```

### Graphical User Interface (GUI)

While the primary interface is the CLI, a simple GUI is also provided for users who prefer a graphical interface.

1. **Run the GUI**:

   ```bash
   python gui_interface.py
   ```

2. **Usage**:

   - A window will appear with a "Browse" button.
   - Click "Browse" to select a YAML file.
   - The result of the validation will be displayed in the window.

## Main Functions

### CLI Interface

- **Argument Parsing**: The CLI interface uses `argparse` to handle command-line arguments, specifically the path to the YAML file.
- **Validation**: The `YAMLValidator` class is responsible for reading the file and checking its syntax using `PyYAML`.
- **Error Reporting**: If errors are found, they are formatted to include line numbers and detailed error messages.

### GUI Interface

- **File Selection**: Users can select a YAML file using a file dialog.
- **Validation**: Similar to the CLI, the GUI uses the `YAMLValidator` class to check the file's syntax.
- **Result Display**: The result of the validation is displayed in the GUI window, with error messages shown in a message box if the file is invalid.

### YAML Validation

- **Reading Files**: The `utils.read_file` function reads the content of the YAML file.
- **Syntax Checking**: The `YAMLValidator.validate_file` method uses `yaml.safe_load` to parse the file and catch any syntax errors.
- **Error Formatting**: If an error occurs, `utils.format_error_message` formats the error message to include line numbers and a description of the problem.

## Conclusion

The YAML File Validator is a simple yet powerful tool for ensuring that your YAML files are syntactically correct. Whether you prefer using the command line or a graphical interface, this tool provides a straightforward way to validate your YAML files and receive detailed feedback on any issues.

If you encounter any problems or have suggestions for improvements, please feel free to reach out to our support team or contribute to the project on GitHub.

---

This manual should provide a comprehensive guide for users to understand and use the YAML File Validator effectively.