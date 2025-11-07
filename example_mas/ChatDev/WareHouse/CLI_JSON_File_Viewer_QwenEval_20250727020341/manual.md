# JSON Viewer CLI Application

## Introduction

The JSON Viewer CLI Application is a simple yet powerful tool designed to help developers and users view the contents of JSON files in a human-readable, indented format. This tool is particularly useful for debugging, data inspection, and quick reviews of JSON data.

## Main Functions

- **Read JSON File**: The application reads a JSON file from a specified file path.
- **Format JSON Data**: It formats the JSON data into a human-readable, indented string.
- **Print to Standard Output**: The formatted JSON is printed to the standard output, making it easy to view directly in the terminal.

## Quick Install

The JSON Viewer CLI Application is written in Python and does not require any external dependencies beyond the standard library. You can install it by cloning the repository and running the application directly.

### Prerequisites

- Python 3.6 or higher

### Installation Steps

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/ChatDev/json-viewer-cli.git
   cd json-viewer-cli
   ```

2. **Run the Application**:
   You can run the application directly from the command line. No installation is necessary beyond cloning the repository.

## Usage

### Command Line Interface

The application is designed to be used via the command line. It takes a single argument, which is the path to the JSON file you want to view.

#### Basic Usage

```bash
python main.py <file_path>
```

- **`<file_path>`**: The path to the JSON file you want to view.

#### Example

Suppose you have a JSON file named `data.json` in the current directory. You can view its contents by running:

```bash
python main.py data.json
```

The application will read the `data.json` file, format its contents, and print the formatted JSON to the terminal.

### Error Handling

- **Incorrect Number of Arguments**: If you do not provide the correct number of arguments, the application will print a usage message and exit.
  ```bash
  Usage: python main.py <file_path>
  ```

- **File Not Found**: If the specified file does not exist or cannot be read, the application will print an error message and exit.
  ```bash
  Failed to load file: [Error Message]
  ```

## Conclusion

The JSON Viewer CLI Application is a simple yet effective tool for viewing JSON files in a human-readable format. Its ease of use and lack of external dependencies make it a great choice for quick inspections and debugging tasks. If you have any questions or need further assistance, feel free to reach out to our support team.

---

This manual should provide a comprehensive guide for users to understand and use the JSON Viewer CLI Application effectively.