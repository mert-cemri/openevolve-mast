```markdown
# File Splitter CLI Utility

A command-line interface (CLI) utility to split a large file into smaller parts of a specified size, naming the output parts sequentially.

## Introduction

The File Splitter CLI Utility is designed to help users efficiently manage large files by splitting them into smaller, more manageable chunks. This can be particularly useful for transferring large files over networks, storing them on devices with limited storage capacity, or simply organizing data into smaller segments.

## Main Functions

- **File Splitting**: The utility splits a large file into smaller parts based on a specified chunk size in megabytes (MB).
- **Sequential Naming**: The output parts are named sequentially, ensuring easy identification and reassembly.
- **Custom Output Directory**: Users can specify the directory where the output parts will be saved.

## Installation

### Environment Setup

This project does not require any external Python packages beyond the standard library. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Quick Install

Clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

## Usage

The utility is executed via the command line. Below is the syntax for using the File Splitter CLI Utility:

```bash
python main.py <file_path> <output_dir> <chunk_size>
```

- `<file_path>`: Path to the input file you wish to split.
- `<output_dir>`: Directory where the output parts will be saved.
- `<chunk_size>`: Size of each chunk in megabytes (MB).

### Example

To split a file named `largefile.txt` into 10MB chunks and save the parts in a directory named `output_parts`, use the following command:

```bash
python main.py largefile.txt output_parts 10
```

### Output

Upon successful execution, the utility will create multiple files in the specified output directory. Each file will be named sequentially, e.g., `largefile.txt_part00`, `largefile.txt_part01`, etc.

## Error Handling

If an error occurs during execution, the utility will print an error message to the console. Common issues include:

- Incorrect file path or file does not exist.
- Insufficient permissions to read the input file or write to the output directory.
- Invalid chunk size (e.g., non-integer or negative values).

Ensure that the input parameters are correct and that you have the necessary permissions to access the specified files and directories.

## Support

For further assistance, please contact our support team at support@chatdev.com.

```
