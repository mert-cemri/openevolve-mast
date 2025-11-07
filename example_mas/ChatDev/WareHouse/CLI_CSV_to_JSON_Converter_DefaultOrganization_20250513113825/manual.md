```markdown
# CSV to JSON Converter CLI

A command-line utility to convert CSV files into JSON format, where each row in the CSV becomes a JSON object. This tool is designed for ease of use and efficiency, allowing users to quickly transform their data files with minimal effort.

## Quick Install

To use the CSV to JSON Converter CLI, you need to have Python installed on your system. The required Python version is 3.6 or higher.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Ensure you have the necessary dependencies installed. You can do this using the `requirements.txt` file provided:

```bash
pip install -r requirements.txt
```

This will install any necessary packages specified in the `requirements.txt` file.

## 🤔 What is this?

This utility is a simple yet powerful tool for converting CSV files to JSON format. It is particularly useful for developers, data analysts, and anyone who needs to transform CSV data into a more flexible and widely-used JSON format.

### Main Features

- **CSV to JSON Conversion**: Convert any CSV file into a JSON file, where each row in the CSV is represented as a JSON object.
- **Command-Line Interface**: Easy-to-use CLI for quick conversions without the need for a graphical interface.
- **Error Handling**: Provides informative error messages for common issues like file not found or IO errors.

## 📖 How to Use

### Running the Converter

To convert a CSV file to a JSON file, use the following command in your terminal:

```bash
python main.py <input_csv_path> <output_json_path>
```

- `<input_csv_path>`: The path to the input CSV file you wish to convert.
- `<output_json_path>`: The path where you want the output JSON file to be saved.

### Example

Suppose you have a CSV file named `data.csv` and you want to convert it to `data.json`. You would run:

```bash
python main.py data.csv data.json
```

### Error Handling

- If the input file does not exist, you will receive an error message: `Error: The file <input_csv_path> does not exist.`
- For any IO errors, the program will output: `IO error occurred: <error_message>`
- For unexpected errors, you will see: `An unexpected error occurred: <error_message>`

## 📖 Documentation

For further details and documentation, please refer to the source code comments and docstrings within the `main.py` and `converter.py` files. These provide additional insights into the implementation and usage of the utility.

Feel free to reach out for support or contribute to the project by submitting issues or pull requests on the repository.

```
```