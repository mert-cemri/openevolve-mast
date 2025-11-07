```markdown
# CSV Unique Value Extractor

A Command Line Interface (CLI) program to read a CSV file, specify a column name, and print all unique values from that column. This program is designed to handle CSV files with headers.

## Main Functions

- **Read CSV File**: The program reads a CSV file using the standard Python library `csv`.
- **Extract Unique Values**: It allows the user to specify a column name and extracts all unique values from that column.
- **Error Handling**: The program handles errors such as file not found, column not found, and general exceptions during file reading.

## Quick Install

This program uses Python's standard library, so no external packages are required. However, ensure that you have Python installed on your system.

### Python Installation

1. **Check Python Installation**: Ensure Python is installed by running `python --version` in your terminal. The program requires Python version 3.6 or higher.
2. **Install Python**: If Python is not installed, download and install it from [Python's official website](https://www.python.org/downloads/).

## How to Use

1. **Prepare Your CSV File**: Ensure your CSV file is properly formatted with headers. Place the file in a known directory.

2. **Run the Program**: Open your terminal or command prompt and navigate to the directory where `main.py` is located.

3. **Execute the Command**:
   ```bash
   python main.py <file_path> <column_name>
   ```
   - Replace `<file_path>` with the path to your CSV file.
   - Replace `<column_name>` with the name of the column from which you want to extract unique values.

4. **View Results**: The program will print all unique values from the specified column. If the column is not found, or if there are no unique values, an appropriate message will be displayed.

## Example Usage

Suppose you have a CSV file named `data.csv` with a column named `Category`. To extract unique values from the `Category` column, you would run:

```bash
python main.py data.csv Category
```

## Error Messages

- **File Not Found**: If the specified file path is incorrect, the program will display: `Error: File '<file_path>' not found.`
- **Column Not Found**: If the specified column does not exist in the CSV file, the program will display: `Error: Column '<column_name>' not found in the CSV file.`
- **General Error**: For any other issues during file reading, an error message will be displayed with details.

## Conclusion

This CLI program is a simple yet powerful tool for extracting unique values from a specified column in a CSV file. It is designed to be user-friendly and robust, handling common errors gracefully. Enjoy using the CSV Unique Value Extractor!
```