# System Resource Monitor CLI Tool User Manual

## Overview

The System Resource Monitor CLI Tool is a simple command-line interface application designed to display real-time system resource usage, including CPU percentage, memory usage (total, used, free), and disk space (total, used, free) for a specified partition or the root partition. The tool updates the display either at regular intervals or on user command.

## Main Functions

- **CPU Usage**: Displays the current CPU usage percentage.
- **Memory Usage**: Shows the total, used, and free memory in gigabytes.
- **Disk Usage**: Provides the total, used, and free disk space in gigabytes for the specified partition or the root partition.
- **Update Interval**: The tool can be configured to update the display at regular intervals (default is 5 seconds).
- **On-Demand Update**: Users can press 'u' to update the display immediately.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system.
- `pip` (Python package installer) must be installed.

### Installing Dependencies

The tool requires the `psutil` library, which can be installed using `pip`. The `requirements.txt` file specifies the required dependencies.

1. **Clone the repository** (if you haven't already):

   ```bash
   git clone https://github.com/your-repository/system-resource-monitor.git
   cd system-resource-monitor
   ```

2. **Install the dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

   **requirements.txt**:
   ```
   # psutil is a cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.
   psutil>=5.8.0
   ```

## Usage

### Running the Tool

To run the System Resource Monitor CLI Tool, use the following command:

```bash
python main.py [options]
```

### Options

- `-i`, `--interval`: Set the update interval in seconds (default: 5).
- `-p`, `--partition`: Specify the disk partition to monitor (default: `/`).

**Examples**:

1. **Default Usage**:

   ```bash
   python main.py
   ```

   This command will start the tool with the default settings, updating the display every 5 seconds and monitoring the root partition (`/`).

2. **Custom Update Interval**:

   ```bash
   python main.py -i 10
   ```

   This command sets the update interval to 10 seconds.

3. **Monitor a Specific Partition**:

   ```bash
   python main.py -p /home
   ```

   This command monitors the `/home` partition.

4. **Custom Interval and Partition**:

   ```bash
   python main.py -i 10 -p /home
   ```

   This command sets the update interval to 10 seconds and monitors the `/home` partition.

### Interacting with the Tool

- **Automatic Updates**: The tool will automatically update the display at the specified interval.
- **Manual Updates**: Press 'u' to update the display immediately.
- **Invalid Input**: If you enter anything other than 'u', the tool will prompt you to enter a valid command.

### Exiting the Tool

To exit the tool, press `Ctrl+C`. This will terminate the tool and return you to the command line.

## Troubleshooting

- **Invalid Partition Path**: If you specify an invalid partition path, the tool will display an error message and exit.
- **Python Version**: Ensure that you are using Python 3.6 or higher. You can check your Python version by running `python --version` or `python3 --version`.
- **Dependencies**: If you encounter any issues with dependencies, ensure that you have installed them correctly by running `pip install -r requirements.txt`.

## Conclusion

The System Resource Monitor CLI Tool is a simple yet powerful utility for monitoring system resources in real-time. By following the installation and usage instructions provided in this manual, you can effectively use the tool to keep track of your system's performance.

If you encounter any issues or have suggestions for improvement, please feel free to contact us at support@chatdev.com.

---

This manual should provide a comprehensive guide for users to understand and use the System Resource Monitor CLI Tool effectively.