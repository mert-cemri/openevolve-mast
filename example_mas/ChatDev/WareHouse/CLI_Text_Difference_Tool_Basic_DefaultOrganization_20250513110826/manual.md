```markdown
# CLI Text Difference Tool

A simple command-line interface (CLI) tool to compare two text files and highlight the lines that are different.

## Introduction

The CLI Text Difference Tool is designed to help users quickly identify differences between two text files. It reads the contents of both files, compares them line by line, and outputs the lines that differ. This tool is useful for developers, writers, and anyone who needs to compare text files for changes or discrepancies.

## Quick Install

This project does not require any external dependencies, making it easy to set up and use. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the directory where the repository was cloned.

3. **Run the Tool**

   You can run the tool directly using Python. No additional installation steps are required.

## How to Use

The CLI Text Difference Tool is straightforward to use. Follow these steps to compare two text files:

1. **Prepare Your Text Files**

   Ensure you have two text files that you want to compare. Note the paths to these files.

2. **Run the Tool**

   Use the following command to run the tool:

   ```bash
   python main.py <file1> <file2>
   ```

   Replace `<file1>` and `<file2>` with the paths to your text files.

3. **View the Output**

   The tool will output the differences line by line. If there are no differences, it will indicate that no differences were found.

   Example output:

   ```
   Differences found:
   Line 3:
   File 1: This is a line in file 1.
   File 2: This is a different line in file 2.
   ```

## Features

- **Line-by-Line Comparison**: Compares two files line by line and highlights differences.
- **Simple Output**: Provides a clear and concise output of differences.
- **No External Dependencies**: The tool is lightweight and easy to use without needing additional libraries.

## Conclusion

The CLI Text Difference Tool is a simple yet effective solution for comparing text files. Whether you're a developer checking code changes or a writer reviewing document edits, this tool provides a quick way to identify differences.

For any questions or support, please contact our team at ChatDev.

```