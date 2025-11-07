# CSV Unique Value Extractor

This is a command-line interface (CLI) program designed to read a CSV file, allow the user to specify a column name, and then print all unique values from that column. The program is capable of handling CSV files with headers.

## Main Functions

- **Read CSV File**: The program reads a CSV file and processes its data into a list of dictionaries, where each dictionary represents a row in the CSV file.
- **Extract Unique Values**: It extracts unique values from a specified column in the CSV file.
- **Error Handling**: The program includes error handling for scenarios such as file not found, empty files, and non-existent columns.

## Quick Install

### Prerequisites

- Ensure you have Python 3.6 or higher installed on your system.

### Installation

1. **Clone the Repository**: Clone the repository to your local machine.

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**: Change your directory to the project folder.

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**: Install the required dependencies using pip.

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

1. **Run the Program**: Execute the program from your terminal or command prompt.

   ```bash
   python main.py <file_path> <column_name>
   ```

   - `<file_path>`: The path to the CSV file you want to process.
   - `<column_name>`: The name of the column from which you want to extract unique values.

2. **Example Usage**:

   ```bash
   python main.py data.csv Name
   ```

   This command will read the `data.csv` file and print all unique values from the `Name` column.

## Error Messages

- **File Not Found**: If the specified file path is incorrect, you will see an error message: `Error: The file '<file_path>' was not found.`
- **Empty File or Missing Column**: If the CSV file is empty or the specified column does not exist, you will see: `Error: The CSV file is empty or does not contain the specified column.`
- **Non-existent Column**: If the column name provided does not exist in the CSV file, you will see: `Error: The column '<column_name>' does not exist in the CSV file.`

## Additional Information

For any further assistance or to report issues, please contact our support team or visit our [documentation page](#).

---

This manual provides a comprehensive guide to installing and using the CSV Unique Value Extractor program. Follow the instructions carefully to ensure a smooth setup and operation.