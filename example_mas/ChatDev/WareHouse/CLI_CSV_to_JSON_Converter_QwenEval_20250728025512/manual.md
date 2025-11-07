# CSV to JSON Converter CLI Utility

## Quick Overview

The CSV to JSON Converter CLI Utility is a simple yet powerful tool designed to convert CSV files into JSON format. Each row in the CSV file is transformed into a JSON object, making it easy to work with structured data in a format that is widely used in web applications and APIs.

## Installation

To use the CSV to JSON Converter, you need to have Python installed on your system. The utility is built using Python 3.6 and above.

### Step 1: Install Python

If you don't have Python installed, you can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Install Required Dependencies

The utility uses the `csv` and `json` modules, which are part of Python's standard library, so no additional dependencies need to be installed.

## Usage

### Step 1: Download the Utility

You can download the utility by cloning the repository or downloading the zip file from the [GitHub repository](https://github.com/ChatDev/csv-to-json-converter).

### Step 2: Run the Utility

Navigate to the directory where the utility is located and run the following command in your terminal:

```bash
python main.py <input_csv_path> <output_json_path>
```

Replace `<input_csv_path>` with the path to your input CSV file and `<output_json_path>` with the path where you want to save the output JSON file.

#### Example

```bash
python main.py data.csv output.json
```

This command will read the `data.csv` file and write the converted JSON data to `output.json`.

### Step 3: Verify the Output

After running the command, you should see a message indicating that the conversion was successful. You can open the output JSON file to verify the contents.

## Error Handling

The utility includes basic error handling to manage common issues:

- **File Not Found:** If the input CSV file does not exist, the utility will print an error message.
- **Permission Denied:** If the utility cannot read the input CSV file or write to the output JSON file, it will print an error message.
- **Unexpected Errors:** Any other exceptions will be caught and an error message will be printed.

## Additional Notes

- **CSV Format:** The utility assumes that the CSV file has a header row. The header row will be used as the keys for the JSON objects.
- **JSON Formatting:** The output JSON file is formatted with an indentation of 4 spaces for readability.

## Contributing

We welcome contributions to the CSV to JSON Converter CLI Utility. If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/csv-to-json-converter).

## License

The CSV to JSON Converter CLI Utility is released under the MIT License. See the [LICENSE](https://github.com/ChatDev/csv-to-json-converter/blob/main/LICENSE) file for more information.

---

This manual should provide a comprehensive guide for users to understand and use the CSV to JSON Converter CLI Utility effectively.