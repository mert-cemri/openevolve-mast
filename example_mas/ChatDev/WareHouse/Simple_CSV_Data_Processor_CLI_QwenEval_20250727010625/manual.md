# CSV Unique Values Finder CLI Program

## Overview

The CSV Unique Values Finder is a command-line interface (CLI) program designed to read a CSV file, allow the user to specify a column name, and then print all unique values from that column. The program is built using Python and handles CSV files with headers.

## Main Functions

- **Read CSV File:** The program reads a CSV file specified by the user.
- **Specify Column Name:** The user can specify the column name from which to extract unique values.
- **Print Unique Values:** The program prints all unique values from the specified column.

## Installation

### Prerequisites

- Python 3.6 or higher
- `csv` module (comes pre-installed with Python)

### Steps to Install

1. **Clone the Repository:**

   ```bash
   git clone https://github.com/ChatDev/csv-unique-values-finder.git
   cd csv-unique-values-finder
   ```

2. **Install Dependencies:**

   This project does not require any external dependencies beyond the standard library. However, if you want to run the GUI version, you will need to install `tkinter`:

   ```bash
   pip install tk
   ```

## Usage

### Command-Line Interface (CLI)

1. **Run the Program:**

   ```bash
   python main.py <csv_file_path> <column_name>
   ```

   - `<csv_file_path>`: The path to the CSV file you want to process.
   - `<column_name>`: The name of the column from which you want to extract unique values.

2. **Example:**

   ```bash
   python main.py data.csv Name
   ```

   This command will read `data.csv`, extract unique values from the `Name` column, and print them.

### Graphical User Interface (GUI)

1. **Run the GUI:**

   ```bash
   python gui.py
   ```

2. **Steps:**

   - Click on the "Select File" button to choose a CSV file.
   - Enter the column name in the "Column Name" field.
   - Click on the "Process CSV" button to see the unique values from the specified column.

## Error Handling

- **FileNotFoundError:** If the specified CSV file does not exist, the program will print an error message and exit.
- **KeyError:** If the specified column name does not exist in the CSV file, the program will print an error message and exit.
- **Unexpected Errors:** Any other unexpected errors will be caught and an error message will be printed.

## Contributing

We welcome contributions to the CSV Unique Values Finder project. If you have any ideas, bug fixes, or improvements, feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Contact

For any questions or support, please contact us at support@chatdev.com.

---

This manual should provide a comprehensive guide for users to understand and use the CSV Unique Values Finder CLI program effectively.