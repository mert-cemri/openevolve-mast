# JSON Formatter CLI Application

This user manual provides detailed instructions on how to use the JSON Formatter CLI Application, a tool designed to display the contents of a JSON file in a human-readable, indented format. This application is implemented in Python and can be executed from the command line.

## Main Functions

The JSON Formatter CLI Application offers the following main functions:

- **Format JSON Files**: Reads a JSON file from a specified file path and outputs its contents in a formatted, human-readable string with indentation for better readability.

## Installation

### Prerequisites

Before you can use the JSON Formatter CLI Application, ensure that you have the following installed on your system:

- **Python 3.x**: The application is written in Python, so you need Python 3.x installed. You can download it from [python.org](https://www.python.org/downloads/).

### Quick Install

1. **Clone the Repository**: First, clone the repository containing the application code to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Application Directory**: Change your current directory to the directory where the application code is located.

   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies**: The application does not have any external dependencies beyond Python's standard library, so no additional installations are required.

## How to Use

### Running the Application

To use the JSON Formatter CLI Application, follow these steps:

1. **Open a Terminal**: Access your command-line interface (CLI) on your operating system.

2. **Run the Application**: Execute the `main.py` script with the path to the JSON file you wish to format. Use the following command:

   ```bash
   python main.py <path_to_json_file>
   ```

   Replace `<path_to_json_file>` with the actual path to your JSON file.

### Example Usage

Suppose you have a JSON file located at `/path/to/your/file.json`. To format this file, you would run:

```bash
python main.py /path/to/your/file.json
```

### Error Handling

- If the file path is incorrect or the file does not exist, the application will display an error message indicating that the file was not found.
- If the file is not a valid JSON, the application will notify you with an appropriate error message.

## Documentation

For further details on the application, please refer to the source code comments and docstrings within the `main.py` and `json_formatter.py` files. These provide additional insights into the implementation and functionality of the application.

## Support

If you encounter any issues or have questions about the application, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

---

Thank you for using the JSON Formatter CLI Application. We hope it meets your needs for formatting JSON files efficiently and effectively.