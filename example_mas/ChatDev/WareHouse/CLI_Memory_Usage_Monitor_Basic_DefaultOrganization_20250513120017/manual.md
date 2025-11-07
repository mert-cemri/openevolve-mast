```markdown
# Memory Usage Monitor

A simple and efficient CLI and GUI application to monitor system memory usage and identify top memory-consuming processes.

## Overview

The Memory Usage Monitor is a Python-based application designed to provide users with insights into their system's memory usage. It offers both a command-line interface (CLI) and a graphical user interface (GUI) to cater to different user preferences. The application fetches data from the `/proc/meminfo` and `/proc/[pid]/status` files to display overall memory usage and list the top memory-consuming processes.

## Features

- **Overall Memory Usage**: Displays detailed information about the system's memory usage.
- **Top Memory-Consuming Processes**: Lists the processes consuming the most memory, helping users identify potential resource hogs.
- **Dual Interface**: Offers both CLI and GUI options for flexibility in usage.

## Installation

### Prerequisites

- Python 3.x installed on your system.
- No external dependencies are required for this project.

### Quick Install

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd memory-usage-monitor
   ```

2. **Run the Application**:
   - For the CLI version:
     ```bash
     python main.py --cli
     ```
   - For the GUI version:
     ```bash
     python main.py
     ```

## Usage

### Command-Line Interface (CLI)

To use the CLI version, execute the following command in your terminal:

```bash
python main.py --cli
```

This will display the overall memory usage and list the top memory-consuming processes directly in your terminal.

### Graphical User Interface (GUI)

To use the GUI version, simply run:

```bash
python main.py
```

This will open a window displaying the overall memory usage and the top memory-consuming processes in a user-friendly interface.

## Troubleshooting

- **GUI Errors**: If you encounter errors while launching the GUI, ensure that you are running the application in a GUI-enabled environment. The application uses Tkinter, which requires a graphical interface to function properly.

## Documentation

For further details and updates, please refer to the project's documentation or contact support.

```
```