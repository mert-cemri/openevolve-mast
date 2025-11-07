# File Watcher CLI Tool

## Introduction

The File Watcher CLI Tool is a utility designed to monitor specified files or directories for changes such as creation, modification, and deletion. It notifies the user via the console whenever a change is detected. This tool is particularly useful for developers, system administrators, and anyone who needs to keep track of file system changes in real-time.

## Main Functions

- **Monitor File or Directory:** The tool can monitor a single file or an entire directory for changes.
- **Detect Changes:** It detects file creation, modification, and deletion events.
- **Console Notifications:** It prints notifications to the console whenever a change is detected.

## Installation

### Prerequisites

- Python 3.6 or higher
- pip (Python package installer)

### Steps to Install

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/ChatDev/file-watcher-cli.git
   cd file-watcher-cli
   ```

2. **Install Dependencies:**
   The tool requires the `watchdog` library to monitor file system events. Install it using pip:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

The tool supports both CLI and GUI interfaces. This section covers the CLI usage.

#### Basic Usage

To start monitoring a file or directory using the CLI, run the following command:
```bash
python main.py cli /path/to/file_or_directory
```

#### Example

To monitor a directory named `documents` located in your home directory, use:
```bash
python main.py cli ~/documents
```

### Graphical User Interface (GUI)

The tool also provides a GUI for users who prefer a graphical interface.

#### Starting the GUI

To start the GUI, run the following command:
```bash
python main.py gui /path/to/file_or_directory
```

#### Example

To start the GUI and monitor a directory named `projects` located in your home directory, use:
```bash
python main.py gui ~/projects
```

### Notifications

- **File Created:** The tool will print a message to the console when a new file is created.
- **File Modified:** The tool will print a message to the console when an existing file is modified.
- **File Deleted:** The tool will print a message to the console when a file is deleted.

## Troubleshooting

### Common Issues

- **Permission Denied:** Ensure you have the necessary permissions to access the specified file or directory.
- **File Not Found:** Verify that the specified path is correct and the file or directory exists.

### Solutions

- **Check Permissions:** Use `chmod` to modify file permissions if necessary.
- **Verify Path:** Double-check the path provided to the tool.

## Conclusion

The File Watcher CLI Tool is a powerful utility for monitoring file system changes. Whether you prefer the command line or a graphical interface, this tool provides a simple and effective way to stay informed about changes in your files and directories.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.

---

This manual should provide a comprehensive guide for users to understand and utilize the File Watcher CLI Tool effectively.