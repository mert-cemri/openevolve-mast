```markdown
# File Joiner CLI Program

Welcome to the File Joiner CLI Program! This tool is designed to help you seamlessly join multiple file parts, which have been split using a file splitter, back into a single original file. This user manual will guide you through the installation, usage, and main functions of the software.

## Quick Install

This project does not require any external Python packages, making it simple to set up and use. Ensure you have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

## 🤔 What is this?

The File Joiner CLI Program is a command-line tool that allows users to merge file parts into a single file. This is particularly useful when dealing with large files that have been split into smaller parts for easier storage or transfer. By specifying the first part of the file, the program automatically identifies and joins all related parts in the correct order.

## 📖 Main Functions

- **Join File Parts**: The primary function of this program is to join multiple file parts into a single file. It reads the parts from the specified directory, sorts them, and writes them into a new file named `joined_file`.

## 🚀 How to Use

### Step 1: Prepare Your Environment

1. Ensure Python is installed on your system. You can verify this by running `python --version` in your command line interface.
2. Clone or download the project files to your local machine.

### Step 2: Run the Program

1. Open your command line interface.
2. Navigate to the directory where the project files are located.
3. Execute the program by running the following command:

   ```bash
   python main.py <first_part_path>
   ```

   Replace `<first_part_path>` with the path to the first part of the file you wish to join.

### Example

If your file parts are named `example.part1`, `example.part2`, etc., and are located in the directory `/path/to/files/`, you would run:

```bash
python main.py /path/to/files/example.part1
```

### Output

Once the program completes, you will see a message indicating that the files have been joined successfully. The resulting file will be named `joined_file` and located in the same directory as the file parts.

## Troubleshooting

- **Incorrect Usage**: If you do not provide the correct number of arguments, the program will display a usage message and exit.
- **File Not Found**: Ensure that the path to the first part is correct and that all parts are in the same directory.

Thank you for using the File Joiner CLI Program! If you encounter any issues or have questions, please feel free to reach out for support.
```