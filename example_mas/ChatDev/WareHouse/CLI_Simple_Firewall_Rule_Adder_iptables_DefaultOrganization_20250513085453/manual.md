```markdown
# Firewall Manager CLI Utility

A simple command-line interface (CLI) utility to manage basic firewall rules using `iptables` on Linux systems. This utility allows you to easily allow, block, or remove rules for specific ports with the necessary sudo privileges.

## Main Functions

The Firewall Manager CLI utility provides the following main functions:

- **Allow a Port**: Add a rule to allow traffic on a specified port.
- **Block a Port**: Add a rule to block traffic on a specified port.
- **Remove a Rule**: Remove an existing rule for a specified port.

## Installation

### Prerequisites

- **Python**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).
- **sudo Privileges**: The utility requires sudo privileges to modify firewall rules.

### Quick Install

1. **Clone the Repository**: Clone the repository to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: There are no external dependencies required for this project. However, ensure that `iptables` is installed and accessible on your system.

## Usage

### Command-Line Interface

The CLI utility is executed via the terminal. Use the following commands to manage firewall rules:

- **Allow a Port**:
  ```bash
  sudo python main.py allow <port-number>
  ```

- **Block a Port**:
  ```bash
  sudo python main.py block <port-number>
  ```

- **Remove a Rule**:
  ```bash
  sudo python main.py remove <port-number>
  ```

Replace `<port-number>` with the desired port number you wish to manage.

### Graphical User Interface (Optional)

A simple GUI is also available if you prefer a graphical interface over the command line. To use the GUI:

1. **Run the GUI Application**:
   ```bash
   python firewall_gui.py
   ```

2. **Using the GUI**:
   - Enter the port number in the provided text field.
   - Click "Allow" to allow traffic on the specified port.
   - Click "Block" to block traffic on the specified port.
   - Click "Remove" to remove the rule for the specified port.

## Troubleshooting

- **Permission Denied**: Ensure you are running the commands with `sudo` to have the necessary permissions to modify firewall rules.
- **Command Not Found**: Ensure `iptables` is installed and accessible in your system's PATH.

## Documentation

For further details and advanced usage, please refer to the source code and comments provided within the scripts.

```
