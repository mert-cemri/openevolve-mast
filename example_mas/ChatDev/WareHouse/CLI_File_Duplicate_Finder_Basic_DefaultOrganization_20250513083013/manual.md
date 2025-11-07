```markdown
# Duplicate File Finder CLI

A command-line interface (CLI) application to find duplicate files within a specified directory based on their content using MD5 hashes.

## Overview

The Duplicate File Finder CLI is a tool designed to help users identify duplicate files in a directory by comparing the content of files using MD5 hashing. This can be particularly useful for cleaning up storage space and organizing files more efficiently.

## Quick Install

To use the Duplicate File Finder CLI, you need to have Python installed on your system. The application is compatible with Python version 3.6 and above.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

   Ensure that you have Python 3.6 or higher installed on your system.

## How to Use

Once you have installed the dependencies, you can use the Duplicate File Finder CLI to search for duplicate files in a specified directory.

### Running the Application

1. **Open a Terminal:**

   Open a terminal or command prompt on your system.

2. **Execute the Command:**

   Run the following command to find duplicate files in a directory:

   ```bash
   python main.py <directory-path>
   ```

   Replace `<directory-path>` with the path to the directory you want to search for duplicate files.

### Example

To find duplicate files in a directory named `my_files`, you would run:

```bash
python main.py my_files
```

### Output

- If duplicate files are found, the application will list the paths of the duplicate files.
- If no duplicate files are found, it will display a message indicating that no duplicates were found.

## Main Functions

- **calculate_md5(file_path):** Calculates the MD5 hash of a file to uniquely identify its content.
- **find_duplicate_files(directory):** Searches the specified directory for duplicate files based on their MD5 hash and returns a list of duplicate file paths.

## Documentation

For more detailed information on the implementation and usage of the Duplicate File Finder CLI, please refer to the source code files `main.py` and `file_utils.py`.

## Support

If you encounter any issues or have questions, please reach out to our support team or check the project's repository for updates and additional documentation.

```
