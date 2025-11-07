```markdown
# File Permission Changer CLI Utility

A simple command-line interface (CLI) utility to change file permissions using numeric (octal) notation, similar to the `chmod` command. This utility allows users to easily modify the permissions of files and directories by specifying the desired permission mode and the target file or directory path.

## Quick Install

To use the File Permission Changer CLI Utility, you need to have Python installed on your system. This utility is compatible with Python version 3.6 and above.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <repository-directory>
   ```

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## 🤔 What is this?

The File Permission Changer CLI Utility is designed to simplify the process of changing file permissions using numeric (octal) notation. This tool is particularly useful for developers and system administrators who need to manage file permissions efficiently.

### Main Features

- **Change File Permissions:** Modify the permissions of files and directories using a simple command-line interface.
- **Error Handling:** Provides user-friendly error messages for invalid input or non-existent paths.
- **Cross-Platform:** Compatible with any operating system that supports Python.

## 📖 How to Use

To change the permissions of a file or directory, use the following command:

```bash
python main.py <mode> <path>
```

- `<mode>`: The permission mode in numeric (octal) notation (e.g., 755, 644).
- `<path>`: The path to the file or directory whose permissions you want to change.

### Example

To change the permissions of a file named `example.txt` to `755`, use the following command:

```bash
python main.py 755 example.txt
```

### Error Messages

- **Invalid Permission Mode:** If the permission mode is not a three-digit octal number, the utility will display an error message: "Error: Invalid permission mode. Please enter a three-digit octal number."
- **Non-Existent Path:** If the specified path does not exist, the utility will raise an `OSError` with the message: "The path '<path>' does not exist."

## Additional Information

For more detailed information on file permissions and octal notation, please refer to the official documentation of your operating system or consult online resources.

Feel free to contribute to the project by submitting issues or pull requests on the repository.

```
