# CLI Text File Sorter

## Quick Overview

The CLI Text File Sorter is a command-line application written in Python that sorts the lines of a text file either alphabetically or in reverse alphabetical order. The sorted lines can be output to a new file or printed to the standard output.

## 📦 Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the repository** (if you haven't already):
   ```bash
   git clone https://github.com/your-repo/cli-text-file-sorter.git
   cd cli-text-file-sorter
   ```

2. **Install dependencies**:
   This project does not require any external Python packages. However, ensure that Python is correctly installed by running:
   ```bash
   python --version
   ```

## 📖 Usage

### Basic Command Structure

```bash
python main.py <file_path> <asc|desc> [output_file]
```

- `<file_path>`: Path to the input text file.
- `<asc|desc>`: Sort order. Use `asc` for ascending (alphabetical) order or `desc` for descending (reverse alphabetical) order.
- `[output_file]` (optional): Path to the output text file. If not provided, the sorted lines will be printed to the standard output.

### Examples

1. **Sorting a file in ascending order and printing to standard output:**
   ```bash
   python main.py input.txt asc
   ```

2. **Sorting a file in descending order and writing to a new file:**
   ```bash
   python main.py input.txt desc output.txt
   ```

3. **Handling errors:**
   - If the input file does not exist, the program will print an error message and exit.
   - If an invalid sort order is provided, the program will print an error message and exit.

## 🛠️ Main Functions

### `sort_lines(lines, order="asc")`

- **Purpose**: Sorts a list of lines alphabetically or in reverse alphabetical order.
- **Parameters**:
  - `lines`: List of strings to be sorted.
  - `order`: Sort order, either `"asc"` for ascending or `"desc"` for descending.
- **Returns**: A new list of sorted lines.

### `read_file(file_path)`

- **Purpose**: Reads lines from a text file.
- **Parameters**:
  - `file_path`: Path to the input text file.
- **Returns**: A list of lines read from the file.

### `write_file(file_path, lines)`

- **Purpose**: Writes a list of lines to a text file.
- **Parameters**:
  - `file_path`: Path to the output text file.
  - `lines`: List of strings to be written to the file.

## 🙋‍♂️ Need Help?

If you encounter any issues or have questions, feel free to reach out to our support team at support@chatdev.com. We're here to help!

## 📝 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This manual should provide a comprehensive guide for users to understand and use the CLI Text File Sorter effectively.