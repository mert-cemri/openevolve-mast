# Column Extractor CLI

A command-line interface (CLI) program designed to extract specific columns from a CSV or space-delimited text file. Users can specify either column numbers or headers to extract the desired data.

## Main Functions

- **File Reading**: Reads data from a specified CSV or space-delimited text file.
- **Column Extraction by Number**: Extracts columns based on specified column numbers.
- **Column Extraction by Header**: Extracts columns based on specified column headers.
- **Flexible Delimiter Handling**: Automatically detects and handles CSV or space-delimited files.

## Quick Install

To use the Column Extractor CLI, ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/).

### Environment Setup

1. **Clone the Repository**: 
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: 
   This program does not require any external Python packages, so no additional dependencies need to be installed.

## How to Use

1. **Navigate to the Project Directory**:
   Open your terminal and navigate to the directory where the project files are located.

2. **Run the Program**:
   Use the following command to run the program:
   ```bash
   python main.py <file_path> <columns>
   ```
   - `<file_path>`: Path to the input file (CSV or space-delimited text).
   - `<columns>`: Comma-separated list of column numbers or headers to extract.

### Examples

- **Extracting by Column Numbers**:
  ```bash
  python main.py data.csv 0,2,4
  ```
  This command extracts columns 0, 2, and 4 from `data.csv`.

- **Extracting by Column Headers**:
  ```bash
  python main.py data.csv Name,Age,Email
  ```
  This command extracts columns with headers "Name", "Age", and "Email" from `data.csv`.

## Error Handling

- If the specified file path is incorrect or the file cannot be read, an error message will be displayed.
- If specified column headers do not exist in the file, an error message will list the missing headers.

## Documentation

For further details on the implementation and code structure, please refer to the source code files:

- `main.py`: Handles command-line interactions and orchestrates the extraction process.
- `file_handler.py`: Contains functions for reading and parsing files.
- `column_extractor.py`: Contains functions for extracting columns by number or header.

Feel free to explore and modify the code to suit your specific needs. If you encounter any issues or have questions, please reach out to our support team.