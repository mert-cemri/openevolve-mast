# Memory Usage Monitor CLI Tool

## Overview

The Memory Usage Monitor CLI Tool is a command-line interface application designed to display overall system memory usage and optionally list the top memory-consuming processes. This tool is particularly useful for system administrators and developers who need to monitor memory usage in real-time on Linux systems.

## Features

- **System Memory Usage**: Displays total, available, and percentage of system memory usage.
- **Top Memory-Consuming Processes**: Optionally lists the top N memory-consuming processes, where N can be specified by the user.

## Installation

### Prerequisites

- **Python**: Ensure you have Python 3.6 or higher installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps to Install

1. **Clone the Repository**: If you haven't already, clone the repository containing the Memory Usage Monitor CLI Tool.
   ```bash
   git clone https://github.com/your-repo/memory-usage-monitor.git
   cd memory-usage-monitor
   ```

2. **Install Dependencies**: This tool does not require any external packages. However, if you decide to use `psutil` for simplified access to system and process memory usage information, you can install it using pip.
   ```bash
   pip install psutil
   ```

## Usage

### Basic Usage

To run the Memory Usage Monitor CLI Tool, use the following command:
```bash
python main.py
```

This will display the total, available, and percentage of system memory usage, along with the top 5 memory-consuming processes.

### Advanced Usage

You can specify the number of top memory-consuming processes to display using the `--top` argument. For example, to display the top 10 memory-consuming processes, use:
```bash
python main.py --top 10
```

## Command-Line Arguments

- `--top`: Specifies the number of top memory-consuming processes to display. Default is 5.

## Example Output

```
Total Memory: 15.55 GB
Available Memory: 2.34 GB
Memory Usage: 85.02%

Top Memory-Consuming Processes:
PID       Name                          Memory (MB)
1234      chrome                        1234.56
5678      firefox                       876.54
9101      python                        543.21
2345      systemd                       234.56
6789      Xorg                          123.45
```

## Troubleshooting

- **Permission Denied**: If you encounter a `Permission Denied` error while accessing `/proc/[pid]/status`, it might be due to insufficient permissions. You can run the tool with `sudo` to resolve this issue.
  ```bash
  sudo python main.py
  ```

- **File Not Found**: If you encounter a `File Not Found` error, ensure that the tool is being run on a Linux system where the `/proc` filesystem is available.

## Contributing

We welcome contributions to the Memory Usage Monitor CLI Tool. If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-repo/memory-usage-monitor).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

This manual provides a comprehensive guide on how to install, use, and troubleshoot the Memory Usage Monitor CLI Tool. If you have any further questions or need additional assistance, please don't hesitate to reach out.