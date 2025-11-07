# File Joiner CLI Tool User Manual

## Overview

The File Joiner CLI Tool is a command-line interface (CLI) program designed to reassemble multiple file parts into a single original file. This tool is particularly useful when you have split a large file into smaller parts using a file splitter and now need to reassemble them.

## Main Functions

- **Join File Parts**: The primary function of the tool is to concatenate multiple file parts into a single file. The user specifies the first part name, and the tool identifies all parts based on a naming convention and joins them in the correct order.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. The tool is compatible with Python 3.6 and above.
- **Command Line Interface (CLI)**: Access to a command line interface is required to run the tool.

### Steps to Install

1. **Clone the Repository** (if you have the source code):
   ```bash
   git clone https://github.com/your-repository/file-joiner.git
   cd file-joiner
   ```

2. **Install Dependencies**:
   The tool does not require any external dependencies. However, ensure you have Python installed. You can verify this by running:
   ```bash
   python --version
   ```

## Usage

### Command-Line Interface (CLI)

1. **Navigate to the Tool Directory**:
   ```bash
   cd path/to/file-joiner
   ```

2. **Run the Tool**:
   Use the following command to run the tool. Replace `filename.part01` with the name of the first part file.
   ```bash
   python main.py filename.part01
   ```

   **Example**:
   ```bash
   python main.py document.part01
   ```

3. **Output**:
   The tool will create a reconstructed file with the original filename (without the `.partXX` suffix) in the same directory as the parts.

### Error Handling

- **No Parts Found**: If no parts are found matching the specified pattern, the tool will output an error message.
- **Incorrect Naming Convention**: Ensure that the file parts follow the naming convention (e.g., `filename.part01`, `filename.part02`, etc.).

## Example Workflow

1. **Split a File**:
   Assume you have a large file named `document.txt` and you split it into parts using a file splitter tool. The resulting parts might be named `document.part01`, `document.part02`, etc.

2. **Reassemble the File**:
   Use the File Joiner CLI Tool to reassemble the file.
   ```bash
   python main.py document.part01
   ```

3. **Verify the Output**:
   Check the directory for the reconstructed file named `document`.

## Additional Notes

- **File Naming Convention**: Ensure that the file parts follow a consistent naming convention. The tool assumes that the parts are named in a sequence (e.g., `.part01`, `.part02`, etc.).
- **Binary Files**: The tool handles both text and binary files. It reads and writes files in binary mode to ensure data integrity.

## Troubleshooting

- **File Not Found**: Ensure that the first part file specified exists in the directory.
- **Permission Issues**: Ensure that you have the necessary permissions to read the file parts and write the output file.

## Support

For any issues or questions, please contact the support team at support@chatdev.com or visit our [GitHub repository](https://github.com/your-repository/file-joiner).

---

This manual provides a comprehensive guide on how to use the File Joiner CLI Tool to reassemble file parts into a single original file. If you encounter any issues or have suggestions for improvement, please feel free to reach out to us.