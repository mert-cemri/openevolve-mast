```markdown
# CLI File Archiver

A simple command-line interface (CLI) application for creating and extracting ZIP archives. This tool allows users to easily compress files and directories into a ZIP archive and extract contents from a ZIP archive to a specified directory.

## Quick Install

This project uses only Python standard libraries and does not require additional packages. Ensure you have Python installed on your system.

## 🤔 What is this?

The CLI File Archiver is a utility tool designed to simplify the process of managing ZIP archives directly from the command line. It supports two main functions:

- **Creating a ZIP Archive**: Compress files and directories into a single ZIP file.
- **Extracting a ZIP Archive**: Decompress a ZIP file to retrieve its contents.

## 📖 Documentation

### Main Functions

1. **Create a ZIP Archive**
   - Command: `create`
   - Description: Compress specified files and directories into a ZIP archive.
   - Usage: 
     ```
     python main.py create <archive_name> <files...>
     ```
   - Example:
     ```
     python main.py create my_archive.zip file1.txt folder1
     ```
   - This command will create a ZIP archive named `my_archive.zip` containing `file1.txt` and all contents of `folder1`.

2. **Extract a ZIP Archive**
   - Command: `extract`
   - Description: Extract the contents of a ZIP archive to a specified directory.
   - Usage:
     ```
     python main.py extract <archive_name> <extract_to>
     ```
   - Example:
     ```
     python main.py extract my_archive.zip ./extracted_files
     ```
   - This command will extract all contents of `my_archive.zip` into the `./extracted_files` directory.

### Installation and Setup

1. **Ensure Python is Installed**: 
   - This application requires Python to be installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**:
   - Clone the project repository to your local machine.

3. **Run the Application**:
   - Navigate to the directory containing the `main.py` file.
   - Use the command line to execute the application using the examples provided above.

### Additional Information

- The application does not require any external dependencies beyond the Python standard library.
- Ensure that the paths provided for files and directories are correct and accessible by the application.

For any issues or further assistance, please contact our support team.

```