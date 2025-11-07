```markdown
# Log Rotator CLI

A simple Command Line Interface (CLI) application for log rotation, compression, and deletion of old logs.

## Overview

The Log Rotator CLI is designed to help manage log files efficiently by providing functionalities to:

- Rotate logs: Rename an existing log file and create a new empty log file.
- Compress old logs: Optionally compress rotated log files to save space.
- Delete old logs: Remove log files older than a specified number of days.

## Quick Install

To use the Log Rotator CLI, you need to have Python installed on your system. You can install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

Ensure you have the following dependencies in your `requirements.txt` file:

```
argparse
```

## Main Functions

### 1. Rotate Logs

The primary function of the Log Rotator is to rename an existing log file (e.g., `app.log` to `app.log.1`) and create a new empty `app.log`.

### 2. Compress Logs

Optionally compress rotated log files to save disk space. This feature can be enabled using the `--compress` flag.

### 3. Delete Old Logs

Automatically delete log files older than a specified number of days. This feature can be configured using the `--delete_days` option.

## How to Use

### Command Line Interface

To run the Log Rotator from the command line, use the following command:

```bash
python main.py --log_file <log_file> [--compress] [--delete_days <N>]
```

- `--log_file`: Specify the log file to rotate. Default is `app.log`.
- `--compress`: Add this flag to compress old logs.
- `--delete_days <N>`: Specify the number of days after which logs should be deleted.

**Example Usage:**

Rotate `app.log`, compress old logs, and delete logs older than 7 days:

```bash
python main.py --log_file app.log --compress --delete_days 7
```

### Graphical User Interface

The Log Rotator also provides a simple GUI for users who prefer a graphical interface. To run the GUI, execute:

```bash
python log_rotator_gui.py
```

- Use the "Rotate Logs" button to perform log rotation.
- Check the "Compress Logs" option to enable compression.
- Enter the number of days in the "Delete logs older than (days)" field to set the deletion threshold.

## Documentation

For more detailed documentation, please refer to the source code comments and function docstrings. The code is structured to be self-explanatory and easy to navigate.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the source code.

```