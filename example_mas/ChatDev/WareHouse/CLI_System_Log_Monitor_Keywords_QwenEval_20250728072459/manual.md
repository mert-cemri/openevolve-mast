# Log Monitor CLI Tool

## Overview

The Log Monitor CLI Tool is a utility designed to monitor specified log files in real-time and highlight lines containing user-defined keywords. This tool is particularly useful for system administrators and developers who need to monitor logs for specific events or errors.

## Features

- **Real-time Monitoring**: Continuously tails the specified log file.
- **Keyword Highlighting**: Highlights lines containing user-defined keywords in red.
- **Cross-Platform Compatibility**: Works on most systems where Python is installed.
- **Ease of Use**: Simple command-line interface.

## Installation

### Prerequisites

- Python 3.6 or higher must be installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Steps

1. **Clone the Repository** (if you haven't already):

   ```bash
   git clone https://github.com/ChatDev/log-monitor.git
   cd log-monitor
   ```

2. **Install Dependencies**:

   This tool does not require any external dependencies. However, ensure that Python is installed correctly by running:

   ```bash
   python --version
   ```

   You should see the Python version number printed.

## Usage

### Command-Line Interface

The tool is executed via the command line. The basic syntax is as follows:

```bash
python main.py <log_file_path> <keyword1,keyword2,...>
```

#### Example

To monitor the `/var/log/syslog` file and highlight lines containing the keywords "error" and "warning", you would run:

```bash
python main.py /var/log/syslog error,warning
```

### Stopping the Monitor

To stop the log monitoring process, press `Ctrl+C` in the terminal where the tool is running.

## Troubleshooting

### Permission Issues

If you encounter permission issues when trying to access the log file, you may need to run the tool with elevated privileges. For example, on Unix-based systems, you can use `sudo`:

```bash
sudo python main.py /var/log/syslog error,warning
```

### Python Version

Ensure that you are using Python 3.6 or higher. You can check your Python version by running:

```bash
python --version
```

### Missing Dependencies

This tool does not require any external dependencies. If you encounter any issues related to missing modules, ensure that you have followed the installation steps correctly.

## Contributing

Contributions to this project are welcome! If you have any ideas for improvements or bug fixes, please feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/ChatDev/log-monitor).

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.

---

This manual should provide a comprehensive guide for users to understand and use the Log Monitor CLI Tool effectively. If you have any specific questions or need further assistance, feel free to reach out!