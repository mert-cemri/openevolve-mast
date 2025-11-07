```markdown
# System Info CLI Tool

A simple command-line interface (CLI) tool to display basic system information on Linux systems. This tool provides details about the OS version, kernel version, CPU model, and total RAM using system files and commands.

## Quick Install

This tool is written in Python and does not require any external dependencies. Ensure you have Python installed on your system.

### Installation Steps

1. **Clone the Repository:**

   Clone the repository to your local machine using the following command:

   ```bash
   git clone <repository-url>
   ```

   Replace `<repository-url>` with the actual URL of the repository.

2. **Navigate to the Project Directory:**

   Change into the project directory:

   ```bash
   cd <project-directory>
   ```

   Replace `<project-directory>` with the name of the cloned directory.

3. **Run the Tool:**

   Execute the main Python script to display the system information:

   ```bash
   python main.py
   ```

## 🤔 What is this?

This CLI tool is designed to provide essential system information for Linux users. It retrieves data directly from system files and commands, ensuring accurate and up-to-date information. The tool is lightweight and does not require any additional libraries or dependencies.

### Main Functions

- **OS Version:** Retrieves the operating system version from the `/etc/os-release` file.
- **Kernel Version:** Uses the `uname` command to get the kernel version.
- **CPU Model:** Extracts the CPU model information from the `/proc/cpuinfo` file.
- **Total RAM:** Reads the total RAM available from the `/proc/meminfo` file and converts it to megabytes for readability.

## 📖 Usage

After following the installation steps, you can run the tool to display the system information. The output will be displayed in the terminal, showing:

- OS Version
- Kernel Version
- CPU Model
- Total RAM

This tool is useful for system administrators, developers, and users who need quick access to system information without navigating through multiple files or commands.

## Troubleshooting

If you encounter any issues while running the tool, ensure that:

- Python is installed and added to your system's PATH.
- You have the necessary permissions to read system files like `/etc/os-release`, `/proc/cpuinfo`, and `/proc/meminfo`.

For further assistance, please refer to the documentation or contact support.

```
