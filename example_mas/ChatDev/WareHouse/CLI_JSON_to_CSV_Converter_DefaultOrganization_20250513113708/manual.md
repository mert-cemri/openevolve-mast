```markdown
# JSON to CSV Converter CLI Tool

Welcome to the JSON to CSV Converter CLI Tool! This tool allows you to convert JSON files into CSV format, handling nested JSON structures by flattening them or allowing you to specify which fields to include in the output.

## Main Functions

- **Convert JSON to CSV**: The primary function of this tool is to convert JSON files to CSV format. It supports both flat and nested JSON structures.
- **Field Specification**: Users can specify which fields to include in the CSV output.
- **Nested JSON Handling**: The tool can flatten nested JSON structures or handle lists by concatenating elements or using indices.

## Quick Install

To use this tool, you need to have Python installed on your system. The minimum required version is Python 3.6.

### Installation Steps

1. **Clone the Repository**: First, clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Set Up Environment**: Ensure you have Python 3.6 or higher installed. You can check your Python version by running:
   ```bash
   python --version
   ```

3. **Install Dependencies**: Although there are no additional Python packages required beyond the standard library, ensure your environment meets the minimum Python version requirement specified in `requirements.txt`.
   ```bash
   # Check Python version
   python --version
   ```

## How to Use

### Command Line Interface

The tool is operated via the command line. Below is the basic usage:

```bash
python main.py <input_json_path> <output_csv_path> [--fields field1 field2 ...] [--list_handling concatenate|index]
```

- `<input_json_path>`: Path to the input JSON file.
- `<output_csv_path>`: Path to the output CSV file.
- `--fields`: Optional. Specify fields to include in the CSV. If not specified, all fields will be included.
- `--list_handling`: Optional. Specify how to handle lists within JSON. Options are `concatenate` (default) or `index`.

### Examples

1. **Basic Conversion**:
   ```bash
   python main.py data/input.json data/output.csv
   ```

2. **Specify Fields**:
   ```bash
   python main.py data/input.json data/output.csv --fields name age
   ```

3. **Handle Lists by Index**:
   ```bash
   python main.py data/input.json data/output.csv --list_handling index
   ```

### Error Handling

- If the input file is not found, you will receive an error message: "Error: The specified file was not found."
- If the input file is not a valid JSON, you will receive an error message: "Error: The input file is not a valid JSON."
- For any other unexpected errors, a message will be displayed with the error details.

## Documentation

For more detailed documentation, please refer to the source code comments and docstrings within `main.py` and `converter.py`.

We hope this tool helps you efficiently convert your JSON data into CSV format. If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.
```