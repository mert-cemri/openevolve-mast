# System Resource Monitor CLI Tool

This user manual provides detailed instructions on how to install, configure, and use the System Resource Monitor CLI Tool. This tool is designed to help users monitor their system's CPU, memory, and disk usage through a simple command-line interface.

## Main Functions

The System Resource Monitor CLI Tool offers the following functionalities:

- **CPU Usage Monitoring**: Displays the current CPU usage percentage.
- **Memory Usage Monitoring**: Shows the total, used, and free memory in gigabytes.
- **Disk Usage Monitoring**: Provides information on total, used, and free disk space for a specified partition or root.
- **Automatic Updates**: Automatically updates the display every few seconds.
- **Manual Refresh**: Allows users to manually refresh the display on command.

## Installation

### Prerequisites

- Python 3.x
- pip (Python package installer)

### Quick Install

1. **Clone the Repository**: Clone the repository containing the CLI tool to your local machine.

   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: Install the required Python packages using pip.

   ```bash
   pip install -r requirements.txt
   ```

   The `requirements.txt` file includes the following dependency:
   - `psutil`: A cross-platform library for retrieving information on running processes and system utilization (CPU, memory, disks, network, sensors) in Python.

## Usage

### Running the CLI Tool

1. **Navigate to the Project Directory**: Ensure you are in the directory where the project files are located.

   ```bash
   cd <repository-directory>
   ```

2. **Execute the Main Script**: Run the `main.py` script to start the CLI tool.

   ```bash
   python main.py
   ```

3. **Monitor System Resources**: Once the tool is running, it will automatically update the display every few seconds. You can also press "Enter" to refresh the display manually.

### Example Output

```
CPU Usage: 15%
Memory Usage: 3.20 GB used / 8.00 GB total
Disk Usage: 120.00 GB used / 250.00 GB total
----------------------------------------
```

## Additional Information

- **Customizing Disk Partition**: By default, the tool monitors the root partition. To monitor a different partition, modify the `get_disk_usage` method in the `system_monitor.py` file to specify the desired partition.

- **Graphical User Interface (GUI)**: Although the primary focus is on the CLI tool, a basic GUI version is available using `tkinter`. To use the GUI, execute the `app_gui.py` script.

  ```bash
  python app_gui.py
  ```

## Support

For any issues or questions, please contact our support team or refer to the documentation provided in the repository.

---

This manual provides all necessary information to effectively use the System Resource Monitor CLI Tool. Enjoy monitoring your system resources with ease!