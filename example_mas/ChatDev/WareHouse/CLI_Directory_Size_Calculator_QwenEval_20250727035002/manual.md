# Directory Size Calculator CLI Utility

## Description

This utility calculates and displays the total size of a directory and its subdirectories in a human-readable format (e.g., KB, MB, GB). It is designed to be simple, efficient, and easy to use, making it perfect for developers and system administrators who need to quickly assess the size of directories.

## Main Functions

- **Calculate Directory Size**: The utility traverses the specified directory and all its subdirectories, summing up the sizes of all files.
- **Human-Readable Output**: The total size is displayed in a human-readable format, making it easy to understand the size without needing to convert bytes manually.
- **Command-Line Interface (CLI)**: The utility can be run from the command line, making it accessible and convenient for use in scripts and automation workflows.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. The utility is compatible with Python 3.6 and above.

### Installing Dependencies

The utility is written in Python and uses standard libraries, so no additional dependencies need to be installed. However, you can ensure your Python environment is up-to-date by running:

```bash
pip install --upgrade pip
```

## Usage

### Running the Utility

1. **Open a Terminal or Command Prompt**: Navigate to the directory containing `main.py`.
2. **Run the Utility**: Use the following command to calculate the size of a directory:

```bash
python main.py /path/to/directory
```

Replace `/path/to/directory` with the path to the directory you want to analyze.

### Example

```bash
python main.py /home/user/Documents
```

**Output:**

```
Total size of /home/user/Documents: 1.2 GB
```

### Error Handling

- **Invalid Path**: If the specified path does not exist or is not a directory, the utility will display an error message.
- **Permissions**: If the utility does not have permission to access a file or directory, it will skip that file or directory and continue processing the rest.

## Additional Features

### Graphical User Interface (GUI)

In addition to the CLI, the utility includes a graphical user interface (GUI) for users who prefer a more visual approach.

#### Running the GUI

1. **Open a Terminal or Command Prompt**: Navigate to the directory containing `gui.py`.
2. **Run the GUI**: Use the following command to start the GUI:

```bash
python gui.py
```

3. **Select a Directory**: Use the "Browse" button to select the directory you want to analyze. The total size will be displayed in the GUI.

### Example

1. **Run the GUI**:

```bash
python gui.py
```

2. **Select a Directory**: Click "Browse" and choose `/home/user/Documents`.

3. **View the Result**: The total size of the directory will be displayed in the GUI.

## Troubleshooting

### Common Issues

- **File Not Found**: Ensure the specified path is correct and the directory exists.
- **Permission Denied**: Run the utility with appropriate permissions or as an administrator if necessary.

### Contact Support

If you encounter any issues or have questions, please contact our support team at [support@chatdev.com](mailto:support@chatdev.com).

## Conclusion

The Directory Size Calculator CLI Utility is a powerful tool for quickly assessing the size of directories and their subdirectories. Whether you prefer the command line or a graphical interface, this utility provides a convenient and efficient way to manage your files and directories.

---

This manual should provide a comprehensive guide for users to understand and utilize the Directory Size Calculator CLI Utility effectively.