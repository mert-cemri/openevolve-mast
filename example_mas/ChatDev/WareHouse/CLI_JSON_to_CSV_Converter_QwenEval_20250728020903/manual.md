# JSON to CSV Converter

## Quick Overview

The JSON to CSV Converter is a command-line interface (CLI) tool designed to convert JSON files into CSV format. It supports handling nested JSON structures by either flattening them or allowing users to specify which fields to include in the output CSV. This tool is particularly useful for data processing and analysis tasks where JSON data needs to be transformed into a more accessible format.

## Quick Install

To use the JSON to CSV Converter, you need to have Python installed on your system. You can download and install Python from the [official website](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository containing the tool or download the source code. Navigate to the directory containing the source code and install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Note: The `requirements.txt` file should list all the necessary dependencies. In this case, the only dependency is `tkinter`, which is included with Python by default.

## 🤔 What is this?

The JSON to CSV Converter is a tool that facilitates the conversion of JSON data into CSV format. It is designed to handle nested JSON structures, which can be challenging to work with in CSV format. The tool provides two main functionalities:

1. **Flattening Nested JSON**: The tool can automatically flatten nested JSON structures into a flat dictionary, making it easier to convert them into CSV format.
2. **Specifying Fields**: Users can specify which fields to include in the output CSV, allowing for more customized conversions.

## 📖 Documentation

### Main Functions

#### Flattening Nested JSON

The tool automatically flattens nested JSON structures by appending a unique identifier to keys with the same name in nested lists and dictionaries. This ensures that all data is included in the output CSV.

#### Specifying Fields

Users can specify which fields to include in the output CSV by providing a comma-separated list of field names. This allows for more customized conversions and can be particularly useful when dealing with large or complex JSON structures.

### How to Use

#### Command-Line Interface (CLI)

1. **Open a Terminal or Command Prompt**: Navigate to the directory containing the `main.py` file.
2. **Run the Tool**: Use the following command to run the tool:

   ```bash
   python main.py --input <input_json_path> --output <output_csv_path> --fields <fields>
   ```

   - `<input_json_path>`: The path to the input JSON file.
   - `<output_csv_path>`: The path to the output CSV file.
   - `<fields>` (optional): A comma-separated list of fields to include in the output CSV.

   **Example**:

   ```bash
   python main.py --input data.json --output output.csv --fields name,age,address_city
   ```

#### Graphical User Interface (GUI)

1. **Run the GUI**: Use the following command to run the GUI:

   ```bash
   python gui.py
   ```

2. **Select Input and Output Files**: Use the "Browse" buttons to select the input JSON file and the output CSV file.
3. **Specify Fields (Optional)**: Enter a comma-separated list of fields to include in the output CSV in the "Fields" field.
4. **Convert**: Click the "Convert" button to start the conversion process.

### Troubleshooting

- **FileNotFoundError**: If the input JSON file does not exist, the tool will display an error message.
- **JSONDecodeError**: If the input file is not a valid JSON file, the tool will display an error message.
- **Other Errors**: If any other error occurs during the conversion process, the tool will display an error message.

### Example

Suppose you have a JSON file named `data.json` with the following content:

```json
[
    {
        "name": "John Doe",
        "age": 30,
        "address": {
            "city": "New York",
            "state": "NY"
        }
    },
    {
        "name": "Jane Smith",
        "age": 25,
        "address": {
            "city": "Los Angeles",
            "state": "CA"
        }
    }
]
```

To convert this JSON file to a CSV file named `output.csv` and include only the `name`, `age`, and `address_city` fields, you can use the following command:

```bash
python main.py --input data.json --output output.csv --fields name,age,address_city
```

The resulting `output.csv` file will contain the following content:

```csv
name,age,address_city
John Doe,30,New York
Jane Smith,25,Los Angeles
```

## Conclusion

The JSON to CSV Converter is a powerful tool for converting JSON data into CSV format. It supports handling nested JSON structures and allows users to specify which fields to include in the output CSV. Whether you prefer using the command-line interface or the graphical user interface, this tool provides a convenient and efficient way to perform JSON to CSV conversions.

If you encounter any issues or have any questions, please feel free to reach out to our support team.