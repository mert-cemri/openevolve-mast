# File Splitter CLI Utility

## Introduction

The File Splitter CLI Utility is a powerful tool designed to split large files into smaller, manageable parts of a specified size. This utility is particularly useful for handling large files that need to be transferred over networks with size limitations or for archiving purposes.

## Main Functions

- **Split File**: The primary function of the utility is to split a large file into smaller chunks of a specified size. The chunks are named sequentially to maintain order.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository** (if not already done):
   ```bash
   git clone https://github.com/ChatDev/file-splitter.git
   cd file-splitter
   ```

2. **Install Dependencies**:
   This utility does not have any external dependencies beyond Python's standard library. However, if you plan to use the GUI, you will need to install `tkinter`, which is usually included with Python.

   For the GUI:
   ```bash
   pip install tk
   ```

## Usage

### Command Line Interface (CLI)

1. **Navigate to the Project Directory**:
   ```bash
   cd path/to/file-splitter
   ```

2. **Run the Utility**:
   Use the following command to split a file:
   ```bash
   python main.py <file_path> <chunk_size_in_mb>
   ```
   - `<file_path>`: The path to the file you want to split.
   - `<chunk_size_in_mb>`: The size of each chunk in megabytes.

   **Example**:
   ```bash
   python main.py largefile.zip 10
   ```
   This command will split `largefile.zip` into chunks of 10MB each.

### Graphical User Interface (GUI)

1. **Run the GUI**:
   ```bash
   python gui.py
   ```

2. **Select File**:
   - Click on the "Browse" button to select the file you want to split.
   - Enter the desired chunk size in megabytes in the "Chunk Size (MB)" field.

3. **Split File**:
   - Click on the "Split File" button to start the splitting process.
   - A success message will be displayed once the file has been split.

## Output

The utility will create multiple files with the original file name appended by `.partX`, where `X` is the sequential number of the chunk.

**Example**:
If you split `largefile.zip` into 10MB chunks, the output files will be:
- `largefile.zip.part1`
- `largefile.zip.part2`
- `largefile.zip.part3`
- ...

## Troubleshooting

- **File Not Found**: Ensure that the file path is correct and the file exists.
- **Invalid Chunk Size**: Make sure the chunk size is a positive integer.
- **Permission Issues**: Ensure you have the necessary permissions to read the file and write to the directory.

## Conclusion

The File Splitter CLI Utility is a simple yet effective tool for splitting large files into smaller parts. Whether you prefer using the command line or the graphical interface, this utility provides a seamless experience for managing large files.

Feel free to contribute to the project or report any issues on the [GitHub repository](https://github.com/ChatDev/file-splitter).

---

This manual should provide a comprehensive guide for users to understand and use the File Splitter CLI Utility effectively.