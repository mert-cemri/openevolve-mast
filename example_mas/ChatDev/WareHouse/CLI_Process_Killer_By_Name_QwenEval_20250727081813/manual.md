# Process Tool User Manual

## Overview

The Process Tool is a Command Line Interface (CLI) application designed to find and kill processes by their name. It lists all matching processes and asks for user confirmation before killing any of them. This tool is particularly useful for system administrators and developers who need to manage processes on their machines.

## Main Functions

1. **Find Processes:** The tool searches for processes that match the user-provided name.
2. **List Processes:** It displays all found processes with their Process IDs (PID) and names.
3. **Kill Processes:** After listing, the tool asks for confirmation to kill each process. It ensures that the user does not accidentally terminate any processes.

## Installation

### Prerequisites

- Python 3.6 or higher
- `pip` package manager

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/process-tool.git
   cd process-tool
   ```

2. **Install Dependencies:**
   The tool requires the `psutil` library to interact with system processes.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Running the Tool

To start the tool, simply run the `main.py` script from the command line:
```bash
python main.py
```

### Step-by-Step Guide

1. **Enter Process Name:**
   When prompted, enter the name of the process you want to find and kill. The tool will search for all processes that match this name.
   ```
   Enter the name of the process to find and kill: example_process
   ```

2. **Review Matching Processes:**
   The tool will list all matching processes along with their PIDs and names.
   ```
   Found the following processes:
   PID: 1234, Name: example_process
   PID: 5678, Name: example_process
   ```

3. **Confirm Process Termination:**
   For each process, the tool will ask for confirmation before killing it. Enter `y` to kill the process or `n` to skip.
   ```
   Are you sure you want to kill process 1234? (y/n): y
   Process 1234 killed successfully.
   ```

### Handling Invalid Inputs

If you enter an invalid response (anything other than `y` or `n`), the tool will prompt you again. After three invalid attempts, it will skip the confirmation for that process.
```
Invalid input. Please enter 'y' or 'n'.
Are you sure you want to kill process 5678? (y/n): a
Invalid input. Please enter 'y' or 'n'.
Are you sure you want to kill process 5678? (y/n): b
Invalid input. Please enter 'y' or 'n'.
Too many invalid attempts. Exiting confirmation for process 5678.
```

## Logging

The tool logs all its activities to a file named `process_tool.log`. This log file can be useful for debugging and tracking the tool's behavior.
- **Location:** The log file is created in the same directory as the `main.py` script.
- **Format:** Each log entry includes a timestamp, log level, and message.

## Troubleshooting

- **No Processes Found:**
  If no processes match the provided name, the tool will inform you.
  ```
  No processes found with that name.
  ```

- **Access Denied:**
  If the tool cannot access a process (e.g., due to insufficient permissions), it will log a warning and skip that process.
  ```
  Process 1234 could not be accessed or is no longer running.
  ```

## Conclusion

The Process Tool is a simple yet powerful utility for managing system processes via the command line. By following the steps outlined in this manual, you can effectively use the tool to find and terminate processes on your system.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.

---

This manual provides a comprehensive guide for users to understand and utilize the Process Tool effectively.