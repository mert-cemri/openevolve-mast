# CLI YAML Validator

A command-line application for validating the syntax of YAML files.

## Overview

The CLI YAML Validator is a simple yet powerful tool designed to help developers and users ensure that their YAML files are syntactically correct. By providing a file path to the application, users can quickly verify the validity of their YAML files and receive detailed error messages, including line numbers, if any issues are detected.

## Features

- **Syntax Validation**: Checks the syntax of YAML files to ensure they are correctly formatted.
- **Error Reporting**: Provides detailed error messages with line and column numbers if syntax errors are found.
- **User-Friendly**: Simple command-line interface for easy use.

## Installation

To use the CLI YAML Validator, you need to have Python installed on your system. Additionally, you need to install the required dependencies.

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Dependencies

The application requires the `PyYAML` library. You can install it using pip:

```bash
pip install PyYAML
```

Alternatively, you can use the `requirements.txt` file to install dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Once the environment is set up, you can use the CLI YAML Validator to check your YAML files.

### Running the Validator

To validate a YAML file, use the following command:

```bash
python main.py <file_path>
```

Replace `<file_path>` with the path to the YAML file you want to validate.

### Example

To validate a file named `example.yaml`, run:

```bash
python main.py example.yaml
```

### Output

- If the YAML file is valid, you will see the message:
  ```
  YAML syntax is valid.
  ```

- If there is a syntax error, you will receive a detailed error message, such as:
  ```
  Error in YAML file at line 3, column 5: expected <block end>, but found '-'
  ```

## Conclusion

The CLI YAML Validator is a straightforward tool that helps you ensure the integrity of your YAML files. By following the installation and usage instructions, you can quickly validate your files and address any syntax issues efficiently.

For further assistance or to report issues, please contact our support team.