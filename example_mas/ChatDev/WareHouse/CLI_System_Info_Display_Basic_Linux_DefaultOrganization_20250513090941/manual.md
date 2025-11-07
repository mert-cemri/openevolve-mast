# System Information CLI Tool

A simple command-line interface (CLI) tool to display basic system information on Linux systems, such as OS version, kernel version, CPU model, and total RAM.

## Quick Install

This tool is developed using Python 3.8 and does not require any external dependencies. Ensure you have Python 3.8 installed on your system.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change your current directory to the project directory:

   ```bash
   cd <repository-directory>
   ```

   Replace `<repository-directory>` with the actual directory name.

3. **Run the Tool:**

   Execute the main application file to display system information:

   ```bash
   python main.py
   ```

## 🤔 What is this?

This CLI tool is designed to provide users with essential system information directly from the command line. It retrieves data from system files and commands available on Linux systems, ensuring accurate and up-to-date information.

### Main Functions

- **OS Version:** Displays the operating system version by reading the `/etc/os-release` file.
- **Kernel Version:** Retrieves the kernel version using the `uname` command.
- **CPU Model:** Provides the CPU model information by parsing the `/proc/cpuinfo` file.
- **Total RAM:** Shows the total RAM available on the system by reading the `/proc/meminfo` file.

## 📖 Usage

To use the tool, simply run the `main.py` file as described in the installation steps. The tool will output the following information:

- **OS Version:** The version of the operating system.
- **Kernel Version:** The version of the Linux kernel.
- **CPU Model:** The model name of the CPU.
- **Total RAM:** The total amount of RAM available on the system, displayed in MB.

Example output:

```
OS Version: Ubuntu 20.04.3 LTS
Kernel Version: 5.11.0-37-generic
CPU Model: Intel(R) Core(TM) i7-8565U CPU @ 1.80GHz
Total RAM: 16384 MB
```

## Troubleshooting

If you encounter any issues while running the tool, ensure that:

- You have Python 3.8 installed on your system.
- You have the necessary permissions to read system files like `/etc/os-release`, `/proc/cpuinfo`, and `/proc/meminfo`.
- The `uname` command is available and executable on your system.

For further assistance, please contact our support team.