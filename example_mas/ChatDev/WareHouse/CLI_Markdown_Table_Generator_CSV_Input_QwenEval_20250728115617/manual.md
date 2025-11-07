# ChatDev CLI Tool for Generating Markdown Tables from CSV Files

## Quick Overview

This tool allows users to convert CSV files into Markdown tables via a command-line interface (CLI). The first row of the CSV file is treated as the header of the Markdown table. This tool is particularly useful for developers, data analysts, and anyone who needs to present tabular data in a Markdown format.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/ChatDev/csv-to-markdown.git
   cd csv-to-markdown
   ```

2. **Install Dependencies**:
   This tool has no external dependencies beyond Python's standard library, so no additional installation is required. However, if you have a `requirements.txt` file, you can install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

The primary way to use this tool is through the command line.

1. **Run the Tool**:
   ```bash
   python main.py <path_to_csv_file> <path_to_output_markdown_file>
   ```
   - `<path_to_csv_file>`: The path to your CSV file.
   - `<path_to_output_markdown_file>`: The path where you want the Markdown file to be saved.

2. **Example**:
   ```bash
   python main.py data.csv output.md
   ```
   This command will read `data.csv`, convert it into a Markdown table, and save it as `output.md`.

### Error Handling

- **FileNotFoundError**: If the specified CSV file does not exist, the tool will print an error message.
- **General Exceptions**: Any other errors during processing will be caught and displayed as a message.

### Graphical User Interface (GUI)

While the primary interface is the CLI, a GUI is also provided for users who prefer a graphical approach.

1. **Run the GUI**:
   ```bash
   python gui.py
   ```
2. **Steps in GUI**:
   - Click "Browse" next to "CSV File" to select your CSV file.
   - Click "Browse" next to "Markdown File" to specify where you want the Markdown file to be saved.
   - Click "Generate" to create the Markdown table.

## Main Functions

### CSVParser

- **Purpose**: Reads and parses a CSV file.
- **Method**: `parse_csv(file_path)`
  - **Parameters**: `file_path` (str) - The path to the CSV file.
  - **Returns**: A list of dictionaries, where each dictionary represents a row in the CSV file with keys as column headers.

### MarkdownGenerator

- **Purpose**: Converts parsed CSV data into a Markdown table.
- **Method**: `generate_table(data)`
  - **Parameters**: `data` (list of dicts) - The parsed CSV data.
  - **Returns**: A string representing the Markdown table.

## Troubleshooting

- **CSV File Format**: Ensure your CSV file is properly formatted with a header row.
- **File Paths**: Double-check the paths to your CSV and output Markdown files.
- **Python Version**: Make sure you are using Python 3.6 or higher.

## Contributing

We welcome contributions to this project! If you have any ideas or improvements, feel free to fork the repository and submit a pull request.

## License

This project is licensed under the MIT License. See the `LICENSE` file for details.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev CLI tool effectively.