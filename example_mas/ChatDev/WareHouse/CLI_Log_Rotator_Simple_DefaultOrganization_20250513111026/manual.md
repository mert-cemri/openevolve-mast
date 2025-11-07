```markdown
# Simple CLI Log Rotator

A command-line and GUI-based application for rotating, compressing, and managing log files.

## Overview

The Simple CLI Log Rotator is a versatile tool designed to help manage log files efficiently. It provides both a command-line interface (CLI) and a graphical user interface (GUI) for ease of use. The main functions include:

- Rotating log files by renaming the existing log file and creating a new empty one.
- Optionally compressing old log files to save disk space.
- Deleting log files older than a specified number of days.

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).

### Environment Setup

1. **Clone the Repository**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

2. **Navigate to the Project Directory**

   ```bash
   cd <project-directory>
   ```

3. **Install Dependencies**

   Install the required Python packages using pip:

   ```bash
   pip install -r requirements.txt
   ```

   If `requirements.txt` is not provided, you can manually install the necessary packages:

   ```bash
   pip install argparse tkinter
   ```

## Usage

### Command-Line Interface (CLI)

To use the CLI version of the log rotator, open your terminal and run the following command:

```bash
python main.py --file <log-file-path> [--compress] [--delete <days>]
```

- `--file`: Specify the path to the log file you want to rotate.
- `--compress`: (Optional) Add this flag to compress old log files.
- `--delete <days>`: (Optional) Specify the number of days to delete logs older than this value.

#### Example

Rotate a log file, compress old logs, and delete logs older than 7 days:

```bash
python main.py --file app.log --compress --delete 7
```

### Graphical User Interface (GUI)

To launch the GUI version, use the following command:

```bash
python main.py --gui
```

#### Using the GUI

1. **Select Log File**: Click on "Browse" to select the log file you want to rotate.
2. **Compress Logs**: Check the "Compress Logs" option if you want to compress old logs.
3. **Delete Logs Older Than N Days**: Check this option and enter the number of days to delete logs older than this value.
4. **Rotate Logs**: Click on "Rotate Logs" to execute the operation.

## Documentation

For further details and documentation, please refer to the source code comments and function docstrings within the project files.

## Support

For any issues or support, please contact our support team or open an issue in the repository.

```
