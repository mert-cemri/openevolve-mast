```markdown
# Environment Variable Manager

A command-line and graphical user interface application for managing environment variables easily.

## Overview

The Environment Variable Manager is a tool designed to help users manage their environment variables through both a command-line interface (CLI) and a graphical user interface (GUI). It allows users to list, set, and unset environment variables, with the option to make these changes persistent across sessions by updating the user's shell profile.

## Features

- **List Environment Variables**: View all current environment variables and their values.
- **Set Environment Variables**: Add or update environment variables for the current session or persistently.
- **Unset Environment Variables**: Remove environment variables from the current session or persistently.
- **Graphical User Interface**: A user-friendly GUI for managing environment variables without using the command line.

## Installation

### Prerequisites

- **Python 3.x**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/).
- **Tkinter**: This is included with Python installations on Windows and macOS. On some Linux distributions, you might need to install it separately using the package manager. For example, on Ubuntu, you can use:
  ```bash
  sudo apt-get install python3-tk
  ```

### Installation Steps

1. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install any necessary dependencies. Note that `argparse` is part of the Python standard library and does not need to be installed separately.
   ```bash
   # No additional dependencies are required for this project.
   ```

## Usage

### Command-Line Interface (CLI)

1. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the project is located.

2. **Run the CLI Application**: Use the following commands to interact with the environment variables.

   - **List Environment Variables**:
     ```bash
     python main.py --list
     ```

   - **Set an Environment Variable**:
     ```bash
     python main.py --set <NAME> <VALUE>
     ```

   - **Set an Environment Variable Persistently**:
     ```bash
     python main.py --set <NAME> <VALUE> --persistent
     ```

   - **Unset an Environment Variable**:
     ```bash
     python main.py --unset <NAME>
     ```

   - **Unset an Environment Variable Persistently**:
     ```bash
     python main.py --unset <NAME> --persistent
     ```

### Graphical User Interface (GUI)

1. **Run the GUI Application**: Execute the `gui.py` file to launch the GUI.
   ```bash
   python gui.py
   ```

2. **Using the GUI**:
   - Enter the variable name and value in the respective fields.
   - Check the "Persistent" checkbox if you want the change to be persistent.
   - Click "Set Variable" to add or update a variable.
   - Click "Unset Variable" to remove a variable.
   - The list of current environment variables is displayed in the list box.

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the project repository.

```
