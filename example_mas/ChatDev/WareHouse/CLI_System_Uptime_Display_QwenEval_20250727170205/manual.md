# Uptime Display Tool

## Overview

The Uptime Display Tool is a command-line interface (CLI) application designed to display the system uptime, i.e., how long the system has been running. This tool utilizes the `uptime` command available on Linux systems to fetch and display the uptime information.

## Main Functions

- **Fetch System Uptime:** The tool fetches the system uptime using the `uptime` command with the `-p` option, which provides a human-readable format.
- **Display Uptime:** The fetched uptime is displayed in the command line interface.

## Installation

### Prerequisites

- Python 3.6 or higher installed on your system.
- Access to a Linux-based system where the `uptime` command is available.

### Steps to Install

1. **Clone the Repository:**
   Clone the repository containing the Uptime Display Tool from GitHub or any other source.

   ```bash
   git clone https://github.com/ChatDev/uptime-display-tool.git
   cd uptime-display-tool
   ```

2. **Install Dependencies:**
   This tool does not require any external Python packages. However, ensure you have Python installed on your system. You can verify this by running:

   ```bash
   python --version
   ```

   If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

3. **Run the Tool:**
   Navigate to the directory containing the `main.py` file and run the tool using Python.

   ```bash
   python main.py
   ```

## Usage

### Command-Line Interface (CLI)

The Uptime Display Tool is designed to be used via the command line. Here’s how you can use it:

1. **Run the Tool:**
   Execute the following command in your terminal:

   ```bash
   python main.py
   ```

2. **View Uptime:**
   The tool will fetch the system uptime and display it in the terminal. The output will look something like this:

   ```
   System Uptime: up 2 days, 5 hours, 30 minutes
   ```

### Graphical User Interface (GUI) [Optional]

Although the primary interface for this tool is the CLI, a GUI interface is also provided for users who prefer a graphical approach. To use the GUI:

1. **Run the GUI:**
   Execute the following command in your terminal:

   ```bash
   python gui_interface.py
   ```

2. **View Uptime:**
   A window will appear displaying the system uptime. The uptime will be updated every second.

## Troubleshooting

- **Command Not Found:**
  If you encounter an error stating that the `uptime` command is not found, ensure that you are running the tool on a Linux-based system where the `uptime` command is available.

- **Permission Issues:**
  If you encounter permission issues, ensure that you have the necessary permissions to execute the `uptime` command.

## Contributing

We welcome contributions to the Uptime Display Tool. If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/uptime-display-tool).

## License

The Uptime Display Tool is released under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Uptime Display Tool effectively. If you have any further questions or need additional assistance, please don't hesitate to reach out.