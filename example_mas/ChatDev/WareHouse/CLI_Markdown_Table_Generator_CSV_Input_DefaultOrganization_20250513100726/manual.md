# CSV to Markdown Converter CLI Tool

This tool is designed to convert CSV files into Markdown table format through a simple command-line interface (CLI). It is ideal for users who need to quickly transform CSV data into a format suitable for Markdown documentation.

## Main Functions

- **CSV to Markdown Conversion**: The tool reads a CSV file and converts its contents into a Markdown table. The first row of the CSV is treated as the header of the table.
- **Error Handling**: The tool provides error messages if the CSV file is empty or if any other issue occurs during the conversion process.

## Quick Install

To use this tool, you need to have Python installed on your system. The tool requires Python version 3.6 or higher.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

Ensure you have the required Python version and install any necessary dependencies. You can create a virtual environment to manage dependencies:

```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
pip install -r requirements.txt
```

## How to Use

Once the environment is set up, you can use the tool to convert CSV files to Markdown tables.

### Command-Line Usage

To convert a CSV file to a Markdown table, run the following command:

```bash
python main.py <path-to-your-csv-file>
```

Replace `<path-to-your-csv-file>` with the actual path to your CSV file. The tool will output the Markdown table to the console.

### Example

Suppose you have a CSV file named `data.csv` in the current directory. You can convert it to a Markdown table by running:

```bash
python main.py data.csv
```

The output will be a Markdown table printed to the console, which you can then copy and paste into your Markdown documents.

## Troubleshooting

- **Empty CSV File**: If the CSV file is empty, the tool will raise an error indicating that the file is empty.
- **File Not Found**: Ensure the file path is correct if you encounter a file not found error.

## Documentation

For further details on the implementation and additional examples, please refer to the source code comments and docstrings within the `main.py` and `converter.py` files.

---

This manual provides a comprehensive guide to installing and using the CSV to Markdown Converter CLI Tool. For any issues or further assistance, please contact our support team.