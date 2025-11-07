# CLI Log Rotator User Manual

## Overview

The CLI Log Rotator is a simple command-line tool designed to manage log files by renaming, compressing, and deleting old logs based on user-defined criteria. This tool is particularly useful for maintaining clean and manageable log directories in applications that generate a large volume of log data.

## Features

- **Log Renaming**: Renames the current log file (e.g., `app.log` to `app.log.1`).
- **Log Compression**: Optionally compresses old log files using gzip.
- **Log Deletion**: Deletes log files older than a specified number of days.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- No additional third-party packages are required for this project.

### Steps to Install

1. **Clone the Repository**: If you haven't already, clone the repository containing the CLI Log Rotator code.
   ```bash
   git clone https://github.com/your-repo/cli-log-rotator.git
   cd cli-log-rotator
   ```

2. **Install Dependencies**: Since no third-party packages are required, you can skip this step. However, ensure that Python is correctly installed and accessible from your command line.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

The CLI Log Rotator can be executed from the command line using the `main.py` script. Below are the available options and their usage.

#### Basic Usage

To rotate a log file without compression or deletion, use the following command:
```bash
python main.py path/to/app.log
```

#### Optional Features

- **Compress Old Logs**: Use the `--compress` flag to compress the renamed log file using gzip.
  ```bash
  python main.py path/to/app.log --compress
  ```

- **Delete Logs Older Than N Days**: Use the `--delete-older-than` flag followed by the number of days to delete log files older than the specified number of days.
  ```bash
  python main.py path/to/app.log --delete-older-than 7
  ```

- **Combine Options**: You can combine both optional features in a single command.
  ```bash
  python main.py path/to/app.log --compress --delete-older-than 7
  ```

### Graphical User Interface (GUI)

The CLI Log Rotator also provides a graphical user interface (GUI) for users who prefer a more visual approach. To use the GUI, run the `gui.py` script:
```bash
python gui.py
```

#### GUI Features

- **Log File Path**: Enter the path to the log file you wish to rotate.
- **Compress Old Logs**: Check the box to compress the renamed log file using gzip.
- **Delete Logs Older Than**: Check the box and enter the number of days to delete log files older than the specified number of days.
- **Rotate Logs**: Click the "Rotate Logs" button to perform the log rotation.

## Troubleshooting

### Common Issues

- **Log File Not Found**: Ensure that the specified log file path is correct and that the file exists.
- **Permission Denied**: Ensure that you have the necessary permissions to read, write, and delete files in the specified directory.
- **Invalid Input**: Ensure that the `--delete-older-than` value is a non-negative integer.

### Error Messages

- **FileNotFoundError**: The specified log file was not found.
- **PermissionError**: You do not have the necessary permissions to perform the requested operation.
- **ValueError**: The `--delete-older-than` value is invalid.

## Conclusion

The CLI Log Rotator is a powerful tool for managing log files in your applications. By using the provided CLI or GUI, you can easily rotate, compress, and delete old log files according to your specific needs. If you encounter any issues or have suggestions for improvement, please feel free to contact the support team.

---

This manual should provide a comprehensive guide for users to understand and utilize the CLI Log Rotator effectively.