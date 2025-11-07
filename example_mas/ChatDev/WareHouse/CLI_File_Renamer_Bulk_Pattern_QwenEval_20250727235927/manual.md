# File Renamer CLI Tool

## Overview

The File Renamer CLI Tool is a powerful utility designed to rename multiple files in a directory based on a specified pattern. This tool supports adding prefixes, replacing substrings, and adding sequential numbers to filenames. It is built using Python and is designed to be easy to use and extend.

## Quick Install

To use the File Renamer CLI Tool, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

Once Python is installed, you can install the required dependencies using pip. The tool does not have any external dependencies beyond the Python standard library, so no additional packages need to be installed.

## 🤔 What is this?

The File Renamer CLI Tool is a command-line application that allows users to rename files in a directory according to specified patterns. This tool is particularly useful for batch processing of files, such as organizing images, documents, or any other type of files.

## 📖 Documentation

### Main Functions

The File Renamer CLI Tool supports the following main functions:

1. **Add Prefix**: Adds a specified prefix to all filenames in the directory.
2. **Replace Substring**: Replaces a specified substring in all filenames with a new substring.
3. **Add Sequential Numbers**: Adds sequential numbers to all filenames, starting from a specified number.

### How to Use

#### Step 1: Open Command Line Interface

Open your command line interface (CLI) or terminal. This can be Command Prompt on Windows, Terminal on macOS, or any terminal emulator on Linux.

#### Step 2: Navigate to the Directory

Navigate to the directory where the File Renamer CLI Tool is located. You can use the `cd` command to change directories. For example:

```bash
cd path/to/file-renamer
```

#### Step 3: Run the Tool

Run the tool using the following command:

```bash
python main.py <directory> [options]
```

Replace `<directory>` with the path to the directory containing the files you want to rename. The available options are:

- `--prefix <prefix>`: Adds the specified prefix to all filenames.
- `--replace <old> <new>`: Replaces the specified substring in all filenames with a new substring.
- `--sequential <start>`: Adds sequential numbers to all filenames, starting from the specified number.

#### Examples

1. **Add Prefix**

   To add the prefix "new_" to all files in the directory "documents", use the following command:

   ```bash
   python main.py documents --prefix new_
   ```

2. **Replace Substring**

   To replace the substring "old" with "new" in all filenames in the directory "documents", use the following command:

   ```bash
   python main.py documents --replace old new
   ```

3. **Add Sequential Numbers**

   To add sequential numbers starting from 1 to all files in the directory "images", use the following command:

   ```bash
   python main.py images --sequential 1
   ```

4. **Combine Options**

   You can combine multiple options in a single command. For example, to add the prefix "new_" and replace the substring "old" with "new" in all filenames in the directory "documents", use the following command:

   ```bash
   python main.py documents --prefix new_ --replace old new
   ```

### Troubleshooting

If you encounter any issues while using the File Renamer CLI Tool, please check the following:

- Ensure that the specified directory exists and contains files.
- Ensure that you have the necessary permissions to rename files in the specified directory.
- Check the command syntax and ensure that all required arguments are provided.

## 🛠️ Development

The File Renamer CLI Tool is open-source and can be extended or modified to suit your needs. The source code is available on [GitHub](https://github.com/ChatDev/file-renamer-cli).

Feel free to contribute to the project by submitting bug reports, feature requests, or pull requests.

## 📬 Support

For any questions or support, please contact us at [support@chatdev.com](mailto:support@chatdev.com).

---

This manual should provide a comprehensive guide for users to understand and use the File Renamer CLI Tool effectively.