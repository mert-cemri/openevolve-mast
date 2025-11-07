# System Uptime CLI Tool

This CLI tool provides a simple way to display the system uptime, which indicates how long the system has been running. It utilizes the `uptime` command available on Linux systems.

## Quick Install

To use this tool, you need to have Python installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

This tool requires Python 3.x. Ensure you have Python installed by running:

```bash
python --version
```

If Python is not installed, download and install it from the [official Python website](https://www.python.org/downloads/).

### Step 3: Run the Tool

Navigate to the directory where `main.py` is located and execute the script:

```bash
python main.py
```

## 🤔 What is this?

This CLI tool is designed to provide users with a quick and easy way to check the system uptime using the `uptime` command on Linux systems. It is a simple yet effective tool for system administrators and users who need to monitor system performance and availability.

## 📖 Documentation

### Main Functions

- **Get Uptime**: The tool executes the `uptime -p` command to retrieve the system uptime in a human-readable format.
- **Display Uptime**: The tool prints the system uptime to the console.

### How to Use

1. **Execute the Script**: Run the `main.py` script using Python to display the system uptime.
2. **Output**: The tool will output the system uptime in a format like "up 1 hour, 23 minutes".

### Error Handling

If there is an error fetching the uptime, the tool will display an error message indicating the issue.

## Resources

For more information on the `uptime` command, you can refer to the [Linux man pages](https://man7.org/linux/man-pages/man1/uptime.1.html).

If you encounter any issues or have questions, feel free to reach out to our support team.