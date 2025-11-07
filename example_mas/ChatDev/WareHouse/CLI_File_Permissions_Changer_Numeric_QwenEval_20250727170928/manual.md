# File Permissions CLI Utility

## Quick Install

To install the File Permissions CLI Utility, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can clone the repository or download the source code. Navigate to the directory containing the `main.py` file and install the required dependencies:

```bash
pip install -r requirements.txt
```

Note: In this case, there are no external dependencies other than Python's standard library, so the `requirements.txt` file is not necessary. However, it's a good practice to include it for future scalability.

## 🤔 What is this?

The File Permissions CLI Utility is a command-line tool that allows you to change file or directory permissions using numeric (octal) notation, similar to the `chmod` command in Unix-like operating systems. This utility is particularly useful for users who prefer a command-line interface or need to automate permission changes in scripts.

## 📖 Documentation

### Main Functions

The utility provides a single command-line interface to change file or directory permissions. The main function is `change_permissions`, which takes two arguments:

- `mode`: The permission mode in numeric (octal) notation (e.g., 755, 644).
- `path`: The file or directory path for which you want to change permissions.

### How to Use

1. **Open a Terminal or Command Prompt**: Navigate to the directory containing the `main.py` file.

2. **Run the Utility**: Use the following command to change file or directory permissions:

   ```bash
   python main.py <mode> <path>
   ```

   Replace `<mode>` with the desired permission mode (e.g., 755, 644) and `<path>` with the file or directory path.

   **Example:**

   ```bash
   python main.py 755 /path/to/your/file_or_directory
   ```

3. **Output**: If the operation is successful, you will see a confirmation message:

   ```
   Permissions changed for /path/to/your/file_or_directory to 755
   ```

   If an error occurs, you will see an error message indicating the issue.

### Error Handling

The utility includes basic error handling for common issues:

- **Invalid Mode**: If you provide an invalid permission mode (e.g., not a 3 or 4-digit octal number), you will see an error message:

  ```
  Error: Invalid mode: 899. Please provide a valid octal number (3 or 4 digits, only 0-7).
  ```

- **File Not Found**: If the specified file or directory does not exist, you will see an error message:

  ```
  Error: File or directory not found: /path/to/nonexistent/file_or_directory
  ```

- **Permission Denied**: If you do not have the necessary permissions to change the file or directory permissions, you will see an error message:

  ```
  Error: Permission denied: /path/to/your/file_or_directory
  ```

### Additional Notes

- **Administrative Privileges**: Changing file or directory permissions may require administrative privileges. If you encounter a permission denied error, try running the command with elevated privileges (e.g., using `sudo` on Unix-like systems or running the command prompt as an administrator on Windows).

- **Compatibility**: This utility is compatible with any operating system that supports Python and the `os.chmod` function, including Unix-like systems (Linux, macOS) and Windows.

## Conclusion

The File Permissions CLI Utility is a simple yet powerful tool for managing file and directory permissions from the command line. By following the instructions in this manual, you can easily change permissions using numeric (octal) notation, similar to the `chmod` command in Unix-like operating systems. If you have any questions or encounter issues, please refer to the error messages or contact the support team for assistance.