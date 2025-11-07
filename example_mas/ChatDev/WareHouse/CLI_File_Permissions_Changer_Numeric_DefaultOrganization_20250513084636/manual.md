# File Permission Changer CLI Utility

This utility is a command-line interface (CLI) application designed to change file permissions using numeric (octal) notation, similar to the `chmod` command. Users can specify the permission mode and the file or directory path to modify permissions accordingly.

## Main Functions

- **Change File Permissions**: The utility allows users to change the permissions of a specified file or directory by providing the desired permission mode in octal notation (e.g., 755, 644).

## Quick Install

### Prerequisites

- **Python Version**: Ensure you have Python 3.6 or higher installed on your system.

### Installation

1. **Clone the Repository**: Clone the repository containing the CLI utility to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required dependencies using `pip`.

   ```bash
   pip install -r requirements.txt
   ```

   This will ensure that your environment is set up with the necessary Python version.

## How to Use

1. **Navigate to the Directory**: Open your terminal and navigate to the directory where the `main.py` file is located.

2. **Run the Utility**: Execute the utility by running the following command:

   ```bash
   python main.py <path> <mode>
   ```

   - `<path>`: The file or directory path for which you want to change permissions.
   - `<mode>`: The permission mode in octal notation (e.g., 755).

   Example:

   ```bash
   python main.py /path/to/file 755
   ```

3. **Output**: The utility will output a message indicating whether the permissions were successfully changed or if an error occurred.

## Error Handling

- **ValueError**: If the permission mode is not within the valid range (000 to 777), an error message will be displayed.
- **FileNotFoundError**: If the specified file or directory does not exist, an error message will be shown.
- **PermissionError**: If the user does not have the necessary permissions to change the file or directory permissions, an error message will be displayed.
- **General Exception**: Any unexpected errors will be caught and displayed to the user.

## Documentation

For further information and detailed documentation, please refer to the source code comments and docstrings within the `main.py` file. These provide additional insights into the functionality and error handling mechanisms of the utility.

By following this manual, users can effectively utilize the CLI utility to manage file permissions on their systems.