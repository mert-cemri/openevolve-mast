# CSV Unique Values Finder

## Quick Overview

The CSV Unique Values Finder is a command-line interface (CLI) tool designed to read a CSV file, allow the user to specify a column name, and print all unique values from that column. This tool is particularly useful for data analysis and preprocessing tasks where understanding the distinct entries in a dataset is crucial.

## 🚀 Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository**

   First, clone the repository from GitHub or download the source code.

   ```bash
   git clone https://github.com/ChatDev/csv-unique-values-finder.git
   cd csv-unique-values-finder
   ```

2. **Install Dependencies**

   The project does not require any external dependencies beyond the standard Python library. However, if you have a `requirements.txt` file, you can install any dependencies listed there using pip.

   ```bash
   pip install -r requirements.txt
   ```

   In this case, the `requirements.txt` file is empty, so no additional packages need to be installed.

## 📖 Documentation

### Main Functions

- **Reading CSV Files:** The tool reads CSV files with headers and stores the data internally.
- **Specifying Column Names:** Users can specify the column name from which they want to extract unique values.
- **Finding Unique Values:** The tool identifies and prints all unique values from the specified column.

### How to Use

1. **Run the Program**

   Use the following command to run the program from the command line:

   ```bash
   python main.py <filename> <column_name>
   ```

   Replace `<filename>` with the path to your CSV file and `<column_name>` with the name of the column you want to analyze.

   **Example:**

   ```bash
   python main.py data.csv Name
   ```

   This command will read `data.csv`, find all unique values in the `Name` column, and print them.

2. **Handling Errors**

   - **File Not Found:** If the specified file does not exist, the program will print an error message and exit.
   - **Column Not Found:** If the specified column name does not exist in the CSV file, the program will print an error message and exit.
   - **No Data Available:** If the CSV file is empty or cannot be read, the program will print an error message and exit.

### Example Usage

Assume you have a CSV file named `employees.csv` with the following content:

```csv
Name,Department,Salary
Alice,HR,50000
Bob,Engineering,75000
Charlie,HR,50000
David,Engineering,80000
Eve,Marketing,60000
```

To find all unique departments, you would run:

```bash
python main.py employees.csv Department
```

The output would be:

```
Unique values in column 'Department':
HR
Engineering
Marketing
```

## 🛠️ Development

### Contributing

We welcome contributions to the CSV Unique Values Finder project. If you have ideas for new features, bug fixes, or improvements, please feel free to open an issue or submit a pull request on GitHub.

### License

This project is licensed under the MIT License. See the `LICENSE` file for more details.

---

This manual should provide a comprehensive guide for users to understand and utilize the CSV Unique Values Finder tool effectively.