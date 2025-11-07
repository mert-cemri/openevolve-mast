```markdown
# CLI System Log Monitor

A command-line interface (CLI) application designed to monitor system log files in real-time, highlighting lines that contain user-defined keywords.

## Overview

The CLI System Log Monitor is a Python-based application that allows users to tail a specified log file and highlight lines containing specific keywords. This tool is particularly useful for system administrators and developers who need to monitor log files for specific events or errors.

## Features

- **Real-time Monitoring**: Continuously monitors a specified log file for new entries.
- **Keyword Highlighting**: Highlights user-defined keywords in the log entries for easy identification.
- **Customizable**: Users can specify keywords directly via command-line arguments or through a file.

## Quick Install

To install the necessary dependencies for running the CLI System Log Monitor, ensure you have Python installed and then run:

```bash
pip install -r requirements.txt
```

*Note: The `requirements.txt` file should list any additional dependencies required by the application.*

## How to Use

### Running the Application

To start monitoring a log file, use the following command:

```bash
python main.py <logfile> [--keyword-file <keyword_file>] [keywords...]
```

- `<logfile>`: The path to the log file you wish to monitor (e.g., `/var/log/syslog`).
- `--keyword-file <keyword_file>`: (Optional) Path to a file containing keywords, one per line, to highlight in the log.
- `[keywords...]`: (Optional) List of keywords to highlight directly from the command line.

### Examples

1. **Monitor a log file with keywords specified in a file:**

   ```bash
   python main.py /var/log/syslog --keyword-file keywords.txt
   ```

2. **Monitor a log file with keywords specified directly:**

   ```bash
   python main.py /var/log/syslog error warning critical
   ```

### Stopping the Monitor

To stop the log monitor, simply press `Ctrl+C` in the terminal.

## Documentation

For more detailed documentation, including advanced usage and troubleshooting, please refer to the source code comments and function docstrings within the `main.py`, `log_tailer.py`, and `utils.py` files.

## Support

For any issues or questions, please contact our support team at support@chatdev.com.

```
```