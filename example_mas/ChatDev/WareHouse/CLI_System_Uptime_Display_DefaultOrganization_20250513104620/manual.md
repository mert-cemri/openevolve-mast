```markdown
# System Uptime CLI Tool

This CLI tool is designed to display the system uptime, i.e., how long the system has been running. It utilizes the `uptime` command available on Linux systems to fetch and display this information.

## Main Functions

- **Display System Uptime**: The primary function of this tool is to execute the `uptime` command and display the system's uptime in a human-readable format.

## Installation

### Prerequisites

- **Python Version**: Ensure that Python 3.6 or higher is installed on your system. You can verify your Python version by running:
  ```bash
  python --version
  ```

- **Uptime Command**: This tool relies on the `uptime` command, which should be available on most Linux distributions by default. You can check if it's installed by running:
  ```bash
  uptime
  ```

### Quick Install

1. **Clone the Repository**: First, clone the repository containing the CLI tool to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Use the following command to install the required dependencies specified in the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

## Usage

Once you have installed the necessary dependencies, you can use the CLI tool to display the system uptime.

1. **Run the Tool**: Execute the `main.py` script to display the system uptime.
   ```bash
   python main.py
   ```

2. **Output**: The tool will output the system uptime in a human-readable format. For example:
   ```
   System Uptime: up 3 hours, 25 minutes
   ```

## Troubleshooting

- **Command Not Found**: If you encounter an error stating that the `uptime` command is not found, ensure that it is installed on your system. You may need to install it using your package manager.

- **Python Errors**: Ensure that you are using Python 3.6 or higher. If you encounter any Python-related errors, verify your Python installation and the installed packages.

## Documentation

For further information and updates, please refer to the official documentation or contact support.

```
```