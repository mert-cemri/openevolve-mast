# Duplicate File Finder CLI

## Overview

The Duplicate File Finder CLI is a command-line tool designed to identify duplicate files within a specified directory based on their content. It uses cryptographic hashes (such as SHA256) to compare file contents and lists the paths of any duplicate files it finds.

## Quick Install

To use the Duplicate File Finder CLI, you need to have Python installed on your system. The software does not require any third-party packages, so no additional installations are necessary.

1. **Clone the repository:**

   ```bash
   git clone https://github.com/ChatDev/duplicate-file-finder.git
   cd duplicate-file-finder
   ```

2. **Ensure Python is installed:**

   You can verify your Python installation by running:

   ```bash
   python --version
   ```

   If Python is not installed, you can download it from the [official Python website](https://www.python.org/downloads/).

## 🤔 What is this?

The Duplicate File Finder CLI is a simple yet powerful tool for managing files on your system. It helps you identify and remove duplicate files, freeing up disk space and ensuring that your files are organized efficiently.

## 📖 Documentation

### Main Functions

The Duplicate File Finder CLI has the following main functions:

- **Hashing Files:** The tool computes the hash of each file in the specified directory using a cryptographic hash function (SHA256 by default).
- **Finding Duplicates:** It compares the hashes of all files and groups files with identical hashes together.
- **Listing Duplicates:** The tool lists the paths of any duplicate files it finds.

### How to Use

1. **Navigate to the project directory:**

   ```bash
   cd path/to/duplicate-file-finder
   ```

2. **Run the CLI tool:**

   Use the following command to find duplicate files in a specified directory:

   ```bash
   python main.py /path/to/directory
   ```

   Replace `/path/to/directory` with the path to the directory you want to scan.

3. **Interpreting the Output:**

   The tool will output a list of duplicate files, grouped by their hash values. Each group will contain the paths of files with identical content.

   Example output:

   ```
   Duplicate files found:
   Hash: 3e25960a79dbc69b674cd4ec67a72c62
     /path/to/directory/file1.txt
     /path/to/directory/file2.txt
   ```

### Troubleshooting

- **Invalid Directory:** If you provide an invalid directory path, the tool will display an error message and exit.

  ```
  Error: /path/to/directory is not a valid directory.
  ```

- **No Duplicates Found:** If no duplicate files are found, the tool will display a message indicating this.

  ```
  No duplicate files found.
  ```

### Additional Features

- **Hash Type:** The tool uses SHA256 by default, but you can modify the `FileHasher` class in `file_hasher.py` to use a different hash type if needed.

## Conclusion

The Duplicate File Finder CLI is a simple yet effective tool for identifying and managing duplicate files on your system. By using cryptographic hashes to compare file contents, it ensures that only truly identical files are grouped together. We hope you find it useful!

If you have any questions or encounter any issues, please feel free to reach out to our support team.