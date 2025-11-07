```markdown
# CSV to JSON Converter CLI Utility

This utility provides a command-line interface (CLI) tool to convert CSV files into JSON format. Each row in the CSV file is transformed into a JSON object, making it easy to work with structured data in various applications.

## Main Functions

- **CSV to JSON Conversion**: The primary function of this utility is to read a CSV file and convert its contents into a JSON file. Each row in the CSV is represented as a JSON object, allowing for easy data manipulation and integration with other systems.

## Quick Install

To use this utility, ensure you have Python installed on your system. The utility is compatible with Python version 3.6 and above.

### Installation Steps

1. **Clone the Repository**: Download or clone the repository containing the utility code.

2. **Navigate to the Directory**: Open a terminal and navigate to the directory where the repository is located.

3. **Install Dependencies**: Ensure you have the required Python version. You can create a virtual environment to manage dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. **Install Required Packages**: Install any necessary packages using the `requirements.txt` file:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once the environment is set up, you can use the CLI utility to convert CSV files to JSON format.

### Running the Utility

1. **Open Terminal**: Open your terminal or command prompt.

2. **Run the Utility**: Execute the following command, replacing `<input_csv_path>` and `<output_json_path>` with your actual file paths:

   ```bash
   python main.py <input_csv_path> <output_json_path>
   ```

   Example:

   ```bash
   python main.py data/input.csv data/output.json
   ```

3. **Output**: If successful, the utility will output a message indicating the CSV file has been successfully converted to JSON. The JSON file will be saved at the specified output path.

## Error Handling

If an error occurs during the conversion process, the utility will print an error message to the console. Ensure that the file paths are correct and that the CSV file is properly formatted.

## Documentation

For further details on the implementation and usage, please refer to the source code comments and docstrings within the `main.py` and `converter.py` files.

This utility is designed to be simple and efficient, providing a straightforward way to convert CSV data into a more flexible JSON format for use in various applications.
```