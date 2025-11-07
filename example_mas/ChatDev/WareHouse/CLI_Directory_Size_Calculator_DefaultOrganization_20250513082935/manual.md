```markdown
# Directory Size CLI Utility

A command-line interface (CLI) utility for calculating and displaying the total size of a directory and its subdirectories in a human-readable format (e.g., KB, MB, GB).

## Quick Install

To install the necessary environment dependencies, ensure you have Python 3.6 or higher installed. You can install the required packages using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

This CLI utility is designed to help users quickly determine the total size of a directory and all its subdirectories. It is particularly useful for managing disk space and understanding the storage requirements of different directories.

### Main Functions

- **Calculate Directory Size**: Recursively calculates the total size of a specified directory and its subdirectories.
- **Human-Readable Output**: Converts the total size into a human-readable format, such as KB, MB, GB, or TB.

## 📖 How to Use

### Running the Utility

To use the CLI utility, navigate to the directory containing the `main.py` file and run the following command in your terminal:

```bash
python main.py <directory_path>
```

Replace `<directory_path>` with the path to the directory you want to analyze. For example:

```bash
python main.py /path/to/directory
```

### Output

- If the specified path is a valid directory, the utility will output the total size in a human-readable format.
- If the specified path is not a directory, the utility will display an error message indicating that the path is not a directory.

### Example

```bash
$ python main.py /home/user/documents
Total Size: 1.23 GB
```

## 📖 Documentation

For more detailed information on the utility's functionality and implementation, please refer to the source code files:

- `main.py`: Contains the CLI application logic.
- `utils.py`: Contains utility functions for calculating and formatting directory sizes.

This utility is a simple yet powerful tool for managing and understanding directory sizes on your system. Enjoy using it to keep track of your storage needs!
```