```markdown
# File Searcher CLI

A command-line interface (CLI) application to search for a given string or pattern within all text files in a specified directory and its subdirectories, similar to the functionality of `grep -r`.

## Overview

The File Searcher CLI is designed to help users quickly locate specific patterns within text files across directories. It recursively searches through all `.txt` files in the specified directory and its subdirectories, displaying the filenames and lines where the pattern is found.

## Quick Install

To get started with the File Searcher CLI, ensure you have Python installed on your system. The application requires Python version 3.6 or higher.

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies:**

   Install the required dependencies using pip:

   ```bash
   pip install -r requirements.txt
   ```

## How to Use

Once the environment is set up, you can use the File Searcher CLI to search for patterns in text files.

### Running the Application

To run the application, use the following command:

```bash
python main.py <directory> <pattern>
```

- `<directory>`: The path to the directory you want to search in.
- `<pattern>`: The string or pattern you want to search for within the text files.

### Example

Suppose you want to search for the pattern "error" in all text files within the directory `/home/user/documents`. You would run:

```bash
python main.py /home/user/documents error
```

### Output

The application will output the filenames and lines where the pattern is found. For example:

```
File: /home/user/documents/file1.txt
  Line 1: This is an error line.
  Line 3: Another error found here.

File: /home/user/documents/subdir/file2.txt
  Line 2: Error detected in this line.
```

## Documentation

For more detailed documentation, please refer to the source code comments and docstrings within the `main.py` and `filesearcher.py` files. These provide insights into the application's architecture and functionality.

## Support

For any issues or questions, please contact our support team or open an issue in the repository.

```

This manual provides a comprehensive guide for users to install, set up, and use the File Searcher CLI application effectively. It includes installation instructions, usage examples, and output expectations to ensure a smooth user experience.
```