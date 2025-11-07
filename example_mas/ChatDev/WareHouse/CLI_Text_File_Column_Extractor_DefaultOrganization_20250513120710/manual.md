```markdown
# CSV Column Extractor CLI

A command-line interface (CLI) program to extract specific columns from a CSV or space-delimited text file. Users can specify column numbers or headers to extract the desired data efficiently.

## Quick Install

This program does not require any external dependencies beyond Python itself. Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

## 🤔 What is this?

The CSV Column Extractor CLI is a simple yet powerful tool designed to help users extract specific columns from CSV or space-delimited text files. Whether you need to extract data based on column numbers or headers, this tool provides a straightforward solution.

### Main Features

- **Extract by Column Numbers:** Specify the column numbers you want to extract.
- **Extract by Headers:** Specify the column headers to extract data by name.
- **Support for CSV and Space-Delimited Files:** Automatically detects the file type based on the extension and processes accordingly.

## 📖 How to Use

### Running the Program

1. **Open your terminal or command prompt.**

2. **Navigate to the directory containing the program files.**

3. **Run the program using the following command:**

   ```bash
   python main.py <filepath> <columns>
   ```

   - `<filepath>`: Path to the CSV or space-delimited text file.
   - `<columns>`: Comma-separated list of column numbers or headers to extract.

### Examples

- **Extract by Column Numbers:**

  If you want to extract the first and third columns from a CSV file named `data.csv`, use:

  ```bash
  python main.py data.csv 0,2
  ```

- **Extract by Headers:**

  If you want to extract columns with headers `Name` and `Age` from a CSV file named `data.csv`, use:

  ```bash
  python main.py data.csv Name,Age
  ```

### Error Handling

- If the specified file does not exist or cannot be read, the program will output an error message.
- If the specified columns do not exist in the file, an error message will be displayed.

## Additional Information

- **File Types Supported:** The program supports both CSV files and space-delimited text files. It automatically detects the file type based on the file extension.
- **No External Dependencies:** This program is built using Python's standard library, ensuring ease of use and installation.

For any issues or further assistance, please contact our support team.

```
