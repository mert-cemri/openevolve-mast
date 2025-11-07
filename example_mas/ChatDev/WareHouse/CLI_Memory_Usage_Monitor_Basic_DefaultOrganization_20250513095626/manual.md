```markdown
# Memory Usage Monitor

A Command-Line Interface (CLI) and Graphical User Interface (GUI) application to monitor system memory usage and list top memory-consuming processes.

## Overview

The Memory Usage Monitor is a Python-based application designed to help users track their system's memory usage. It provides both a CLI and an optional GUI for displaying overall memory usage and the top memory-consuming processes. The application reads data from the `/proc/meminfo` and `/proc/[pid]/status` files to gather the necessary information.

## Features

- **Overall Memory Usage**: Displays detailed information about the system's memory usage.
- **Top Memory-Consuming Processes**: Lists the top processes consuming the most memory.
- **CLI and GUI Options**: Users can choose to run the application in a command-line interface or a graphical user interface.

## Installation

### Prerequisites

- Python 3.x
- Tkinter (for GUI functionality)

### Quick Install

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**:
   Ensure you have Python and Tkinter installed. Tkinter is usually included with Python installations, but you can install it using your package manager if needed.

3. **Run the Application**:
   - For CLI:
     ```bash
     python main.py
     ```
   - For GUI:
     ```bash
     python main.py --gui
     ```

## Usage

### Command-Line Interface (CLI)

- **Display Overall Memory Usage**:
  Run the application without any arguments to see the overall memory usage.
  ```bash
  python main.py
  ```

- **Display Top Memory-Consuming Processes**:
  The CLI will automatically display the top 5 memory-consuming processes.

### Graphical User Interface (GUI)

- **Launch GUI**:
  Run the application with the `--gui` flag to launch the graphical interface.
  ```bash
  python main.py --gui
  ```

- **Features in GUI**:
  - The main window displays overall memory usage and top memory-consuming processes.
  - The display updates every 5 seconds to provide real-time monitoring.

## Documentation

For more detailed documentation and examples, please refer to the source code comments and docstrings within the Python files. The code is structured into separate modules for memory monitoring (`memory_monitor.py`), command-line interface (`cli.py`), and graphical user interface (`gui.py`).

## Support

For any issues or questions, please contact our support team or open an issue in the repository.

```
```