```markdown
# CLI File Renamer

A command-line interface (CLI) application that allows you to rename multiple files in a directory based on a specified pattern. This tool is designed to streamline the process of renaming files by adding prefixes, replacing substrings, and appending sequential numbers.

## Main Functions

The CLI File Renamer provides the following functionalities:

- **Add Prefix**: Add a specified prefix to the beginning of each file name.
- **Replace Substring**: Replace a specified substring within the file names with a new substring.
- **Add Sequential Numbers**: Append sequential numbers to the file names, starting from a specified number.

## Quick Install

This project uses only Python's standard library and does not require any additional packages. Ensure you have Python installed on your system.

## How to Use

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Run the Application**

   Use the following command to run the CLI File Renamer:

   ```bash
   python main.py <directory> [--prefix PREFIX] [--replace SUBSTRING] [--replacement NEW_SUBSTRING] [--start-number NUMBER]
   ```

   - `<directory>`: The path to the directory containing the files you want to rename.
   - `--prefix PREFIX`: (Optional) The prefix to add to each file name.
   - `--replace SUBSTRING`: (Optional) The substring to replace in each file name.
   - `--replacement NEW_SUBSTRING`: (Optional) The new substring to replace the old substring.
   - `--start-number NUMBER`: (Optional) The starting number for sequential numbering (default is 1).

4. **Examples**

   - Add a prefix to all files in a directory:

     ```bash
     python main.py /path/to/directory --prefix "new_"
     ```

   - Replace a substring in all file names:

     ```bash
     python main.py /path/to/directory --replace "old" --replacement "new"
     ```

   - Add sequential numbers to all file names starting from 10:

     ```bash
     python main.py /path/to/directory --start-number 10
     ```

5. **Error Handling**

   - If the directory is invalid, the application will display an error message.
   - If no files are found in the specified directory, an informational message will be displayed.
   - Ensure both `--replace` and `--replacement` are provided when replacing substrings.

## Documentation

For further details and updates, please refer to the project documentation or contact the support team.

```