# System Uptime CLI Tool

## Overview

The System Uptime CLI Tool is a simple command-line interface application designed to display the system uptime (how long the system has been running) on a Linux-based system. This tool utilizes the `uptime` command to fetch and display the system's uptime in a user-friendly format.

## Main Functions

- **Display System Uptime**: The primary function of the tool is to display the system uptime using the `uptime -p` command, which provides a human-readable format of the uptime.

## Prerequisites

- **Operating System**: Linux (The tool is designed to work on Linux-based systems, as it relies on the `uptime` command, which is native to Linux.)
- **Python**: Python 3.6 or higher (The tool is written in Python and requires Python to be installed on your system.)

## Installation

### Step 1: Install Python

Ensure that Python is installed on your system. You can check if Python is installed by running the following command in your terminal:

```bash
python3 --version
```

If Python is not installed, you can install it by following the instructions for your Linux distribution:

- **Debian/Ubuntu**:
  ```bash
  sudo apt update
  sudo apt install python3
  ```

- **Fedora**:
  ```bash
  sudo dnf install python3
  ```

- **Arch Linux**:
  ```bash
  sudo pacman -S python
  ```

### Step 2: Clone the Repository

Clone the repository containing the System Uptime CLI Tool to your local machine:

```bash
git clone https://github.com/ChatDev/system-uptime-cli.git
cd system-uptime-cli
```

### Step 3: Install Dependencies

The System Uptime CLI Tool does not have any external dependencies beyond Python itself. However, if you have a `requirements.txt` file, you can install any dependencies listed there using pip:

```bash
pip3 install -r requirements.txt
```

## Usage

### Display System Uptime

To display the system uptime, run the following command in your terminal:

```bash
python3 main.py
```

This command will execute the `main.py` script, which in turn calls the `display_uptime` function in the `uptime.py` module. The `display_uptime` function uses the `subprocess` module to execute the `uptime -p` command and prints the system uptime to the terminal.

### Example Output

```bash
System Uptime: up 2 days, 5 hours, 30 minutes
```

## GUI Mode (Optional)

The tool also includes a graphical user interface (GUI) mode, which can be used to display the system uptime in a window. To use the GUI mode, run the following command:

```bash
python3 gui.py
```

This command will execute the `gui.py` script, which creates a simple GUI window using the `tkinter` library. The GUI window will display the system uptime in a label widget.

### Example GUI Output

![System Uptime GUI](path/to/screenshot.png)

## Troubleshooting

If you encounter any issues while using the System Uptime CLI Tool, please check the following:

- **Python Installation**: Ensure that Python is installed and properly configured on your system.
- **Permissions**: Ensure that you have the necessary permissions to execute the `uptime` command.
- **Dependencies**: Ensure that all dependencies are installed and up-to-date.

If you are unable to resolve the issue, please contact the support team at support@chatdev.com for assistance.

## Contributing

We welcome contributions to the System Uptime CLI Tool. If you have any ideas for improvements or bug fixes, please feel free to submit a pull request on the [GitHub repository](https://github.com/ChatDev/system-uptime-cli).

## License

The System Uptime CLI Tool is released under the MIT License. Please see the [LICENSE](LICENSE) file for more information.

---

This manual should provide users with a comprehensive guide on how to install, use, and troubleshoot the System Uptime CLI Tool. If you have any further questions or need additional assistance, please don't hesitate to reach out.