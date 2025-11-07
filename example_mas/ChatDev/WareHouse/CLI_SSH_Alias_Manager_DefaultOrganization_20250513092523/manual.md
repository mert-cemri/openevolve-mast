```markdown
# SSH Alias Manager

A command-line and graphical user interface application for managing SSH connection aliases, making it easier to connect to remote servers.

## Introduction

The SSH Alias Manager is a tool designed to simplify the management of SSH connection aliases. It allows users to add, list, and remove SSH connection aliases, which include details such as hostname, user, port, and key file. This tool is available both as a command-line interface (CLI) and a graphical user interface (GUI) using Tkinter.

## Main Functions

- **Add Alias**: Create a new SSH alias with specified details.
- **List Aliases**: Display all stored SSH aliases.
- **Remove Alias**: Delete an existing SSH alias by name.

## Installation

### Prerequisites

- Python 3.6 or higher is required.
- Tkinter library for GUI (usually included with Python, but may need separate installation on some Linux distributions).

### Installing Dependencies

1. **Ensure Python is installed**: Verify that Python 3.6 or higher is installed on your system. You can check this by running:
   ```bash
   python --version
   ```

2. **Install Tkinter** (if not already installed):
   - On Ubuntu or Debian-based systems, run:
     ```bash
     sudo apt-get install python3-tk
     ```
   - On Fedora, run:
     ```bash
     sudo dnf install python3-tkinter
     ```

3. **Clone the Repository**: Clone the project repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

4. **Install Python Dependencies**: Install any additional Python dependencies specified in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

### Command-Line Interface (CLI)

1. **Navigate to the Project Directory**: Ensure you are in the directory containing the `main.py` file.

2. **Run the Application**: Use the following commands to manage your SSH aliases.

   - **Add an Alias**:
     ```bash
     python main.py add --alias <alias_name> --hostname <hostname> --user <user> --port <port> --keyfile <key_file>
     ```
     Example:
     ```bash
     python main.py add --alias myserver --hostname example.com --user admin --port 22 --keyfile ~/.ssh/id_rsa
     ```

   - **List Aliases**:
     ```bash
     python main.py list
     ```

   - **Remove an Alias**:
     ```bash
     python main.py remove --alias <alias_name>
     ```
     Example:
     ```bash
     python main.py remove --alias myserver
     ```

### Graphical User Interface (GUI)

1. **Run the GUI Application**: Execute the following command to launch the GUI.
   ```bash
   python ssh_alias_gui.py
   ```

2. **Using the GUI**:
   - **Add Alias**: Click the "Add Alias" button and fill in the details in the popup window.
   - **List Aliases**: Click the "List Aliases" button to view all stored aliases.
   - **Remove Alias**: Click the "Remove Alias" button and enter the alias name to delete it.

## Conclusion

The SSH Alias Manager provides a convenient way to manage SSH connection details, making it easier to connect to remote servers without remembering complex connection strings. Whether you prefer using the command line or a graphical interface, this tool offers flexibility and ease of use.

For further assistance or to report issues, please contact our support team.

```