# User Manual for ChatDev System Info CLI Tool

## Overview

The ChatDev System Info CLI Tool is a command-line interface designed to display basic system information on Linux systems. It provides details such as the OS version, kernel version, CPU model, and total RAM. This tool is built using Python and utilizes system files in `/proc` and commands like `uname` to gather the necessary information.

## Main Functions

- **OS Version**: Retrieves the operating system version using `lsb_release` or by parsing `/etc/os-release`.
- **Kernel Version**: Fetches the kernel version using the `uname` command.
- **CPU Model**: Extracts the CPU model from `/proc/cpuinfo`.
- **Total RAM**: Reads the total RAM from `/proc/meminfo` and converts it to gigabytes.

## Installation

### Prerequisites

- **Python**: Ensure Python 3.6 or higher is installed on your system. You can check your Python version by running:
  ```bash
  python3 --version
  ```
- **Git**: Optional, but recommended for cloning the repository.

### Steps to Install

1. **Clone the Repository** (if you haven't already):
   ```bash
   git clone https://github.com/ChatDev/system-info-cli.git
   cd system-info-cli
   ```

2. **Install Dependencies**:
   Since this project relies only on built-in Python modules, no additional dependencies are required. However, you can create a virtual environment to manage dependencies:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Run the Tool**:
   You can run the tool directly from the command line:
   ```bash
   python3 main.py
   ```

## Usage

### Command-Line Interface

To use the ChatDev System Info CLI Tool, simply run the `main.py` script from the command line:
```bash
python3 main.py
```

### Example Output

When you run the tool, it will display the system information in a formatted manner:
```
System Information:
OS Version: Ubuntu 20.04.5 LTS
Kernel Version: 5.4.0-126-generic
CPU Model: Intel(R) Core(TM) i7-8550U CPU @ 1.80GHz
Total RAM: 15.55 GB
```

## Troubleshooting

### Common Issues

- **Missing `lsb_release` Command**:
  If the `lsb_release` command is not available, the tool will fall back to parsing `/etc/os-release`. Ensure that this file exists and is readable.

- **File Not Found Errors**:
  Ensure that the `/proc/cpuinfo` and `/proc/meminfo` files are accessible. These files are typically available on all Linux systems.

### Solutions

- **Install `lsb_release`**:
  You can install the `lsb_release` command using your package manager. For example, on Ubuntu:
  ```bash
  sudo apt-get install lsb-release
  ```

- **Check File Permissions**:
  Ensure that the `/proc` directory and its contents are readable. You can check the permissions using:
  ```bash
  ls -ld /proc
  ls -l /proc/cpuinfo
  ls -l /proc/meminfo
  ```

## Conclusion

The ChatDev System Info CLI Tool is a simple yet powerful utility for retrieving essential system information on Linux systems. By following the installation and usage instructions provided in this manual, you should be able to use the tool effectively to monitor your system's configuration.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team or contribute to the project on GitHub.

---

This manual provides a comprehensive guide for users to understand, install, and use the ChatDev System Info CLI Tool. It covers the main functions, installation steps, usage instructions, and troubleshooting tips to ensure a smooth user experience.