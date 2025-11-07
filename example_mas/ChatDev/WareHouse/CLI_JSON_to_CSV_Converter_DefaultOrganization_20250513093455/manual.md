```markdown
# JSON to CSV Converter CLI Tool

Welcome to the JSON to CSV Converter CLI Tool! This tool allows you to convert JSON files into CSV format with ease, handling nested JSON structures by flattening them or allowing you to specify fields for conversion.

## Main Functions

- **Convert JSON to CSV**: Convert JSON files into CSV format.
- **Handle Nested JSON**: Flatten nested JSON structures or specify fields to flatten.
- **List Handling**: Choose how to handle lists within JSON - either by appending indices or concatenating list elements.

## Installation

To use this tool, ensure you have Python 3.6 or higher installed on your system. You can check your Python version by running:

```bash
python --version
```

### Install Environment Dependencies

1. Clone the repository or download the source code.
2. Navigate to the directory containing the source code.
3. Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## How to Use

The tool is executed via the command line. Below are the steps to use the JSON to CSV Converter CLI Tool:

### Basic Usage

To convert a JSON file to a CSV file, use the following command:

```bash
python main.py <json_path> <csv_path>
```

- `<json_path>`: Path to the input JSON file.
- `<csv_path>`: Path to the output CSV file.

### Advanced Options

- **Specify Fields to Flatten**: If you want to flatten specific fields in the JSON, use the `--fields` option followed by the list of fields:

```bash
python main.py <json_path> <csv_path> --fields field1 field2
```

- **List Handling**: Choose how to handle lists within the JSON using the `--list_handling` option. Options are:
  - `index`: Append indices to list elements.
  - `concat`: Concatenate list elements into a single string.

Example:

```bash
python main.py <json_path> <csv_path> --list_handling concat
```

### Error Handling

If an error occurs during the conversion process, an error message will be displayed in the console. Ensure that the JSON file is correctly formatted and that the specified paths are accessible.

## Conclusion

This tool simplifies the process of converting JSON files to CSV format, providing flexibility in handling nested structures and lists. For any issues or further assistance, please refer to the documentation or contact support.

Happy converting!
```
