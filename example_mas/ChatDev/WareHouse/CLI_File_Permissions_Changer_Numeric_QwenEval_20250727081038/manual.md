# File Permission Changer CLI Utility

## Introduction

The File Permission Changer CLI Utility is a Python-based command-line interface (CLI) tool designed to change file or directory permissions using numeric (octal) notation, similar to the Unix `chmod` command. This utility allows users to specify the desired permission mode (e.g., 755, 644) and the path to the target file or directory.

## Key Features

- **Numeric (Octal) Notation Support:** Users can specify file permissions using three-digit octal numbers.
- **Error Handling:** The utility provides informative error messages for common issues such as invalid permission modes, non-existent files, and permission errors.
- **Cross-Platform:** The utility is written in Python and should work on any platform that supports Python, including Windows, macOS, and Linux.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/file-permission-changer.git
   cd file-permission-changer
   ```

2. **Install Dependencies:**
   This utility does not require any external dependencies. However, ensure you have Python installed as mentioned above.

   ```bash
   pip install -r requirements.txt
   ```

   *(Note: The `requirements.txt` file is empty in this case as no external libraries are needed.)*

## Usage

### Basic Command Structure

```bash
python main.py <permission_mode> <file_path>
```

- **`<permission_mode>`:** The desired permission mode in numeric (octal) notation (e.g., 755, 644).
- **`<file_path>`:** The path to the file or directory whose permissions you want to change.

### Examples

1. **Change Permissions of a File:**

   ```bash
   python main.py 644 /path/to/your/file.txt
   ```

   This command sets the permissions of `file.txt` to `644`, which means:
   - Owner: Read and Write (6)
   - Group: Read (4)
   - Others: Read (4)

2. **Change Permissions of a Directory:**

   ```bash
   python main.py 755 /path/to/your/directory
   ```

   This command sets the permissions of `directory` to `755`, which means:
   - Owner: Read, Write, and Execute (7)
   - Group: Read and Execute (5)
   - Others: Read and Execute (5)

### Error Handling

- **Invalid Permission Mode:**
  ```bash
  python main.py 1234 /path/to/your/file.txt
  ```
  Output:
  ```
  Value Error: Invalid permission mode. Please use a three-digit numeric (octal) notation (e.g., 755, 644).
  ```

- **File Not Found:**
  ```bash
  python main.py 644 /nonexistent/file.txt
  ```
  Output:
  ```
  File Not Found Error: The file or directory '/nonexistent/file.txt' does not exist.
  ```

- **Permission Denied:**
  ```bash
  python main.py 755 /protected/directory
  ```
  Output:
  ```
  Permission Error: Permission denied to change permissions for '/protected/directory'.
  ```

## Troubleshooting

- **Python Not Found:**
  Ensure that Python is installed and added to your system's PATH. You can verify this by running `python --version` in your terminal or command prompt.

- **Incorrect File Path:**
  Double-check the file or directory path provided to ensure it is correct and accessible.

- **Insufficient Permissions:**
  If you encounter a permission error, you may need to run the command with elevated privileges (e.g., using `sudo` on Unix-based systems).

## Contributing

We welcome contributions to improve the File Permission Changer CLI Utility. If you have any ideas, bug fixes, or feature requests, feel free to open an issue or submit a pull request on our [GitHub repository](https://github.com/ChatDev/file-permission-changer).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual provides a comprehensive guide on how to use the File Permission Changer CLI Utility, including installation, usage, and troubleshooting tips. If you encounter any issues or have suggestions for improvement, please don't hesitate to reach out to our support team or contribute to the project.