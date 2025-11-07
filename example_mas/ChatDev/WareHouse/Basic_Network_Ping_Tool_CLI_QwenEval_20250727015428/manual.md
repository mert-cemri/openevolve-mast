# ChatDev Ping Tool User Manual

## Introduction

The ChatDev Ping Tool is a simple yet powerful Command Line Interface (CLI) application designed to send ICMP echo requests to a specified IP address or hostname. It allows users to configure the number of pings to send and provides detailed round-trip time information for each ping, along with a summary of the average round-trip time.

## Main Functions

- **Ping a Host:** The primary function of the tool is to send ICMP echo requests to a specified host.
- **Configure Ping Count:** Users can specify the number of ICMP echo requests to send.
- **Display Round-Trip Time:** The tool displays the round-trip time for each ping in milliseconds.
- **Summary:** After all pings are sent, the tool provides a summary of the average round-trip time.

## System Requirements

- **Operating System:** Windows, macOS, or Linux.
- **Python Version:** Python 3.6 or higher.

## Installation

The ChatDev Ping Tool is a Python-based application and does not require any external dependencies beyond the standard Python library. You can install it by cloning the repository or downloading the source code.

### Cloning the Repository

1. Open a terminal or command prompt.
2. Clone the repository using the following command:
   ```bash
   git clone https://github.com/ChatDev/ping-tool.git
   ```
3. Navigate to the project directory:
   ```bash
   cd ping-tool
   ```

### Downloading the Source Code

1. Visit the [ChatDev Ping Tool GitHub repository](https://github.com/ChatDev/ping-tool).
2. Click on the "Code" button and select "Download ZIP".
3. Extract the downloaded ZIP file to a directory of your choice.
4. Open a terminal or command prompt and navigate to the extracted directory.

## Usage

### Basic Usage

To use the ChatDev Ping Tool, open a terminal or command prompt and navigate to the directory where the `main.py` file is located. Run the following command:

```bash
python main.py <host> [-c <count>]
```

- `<host>`: The IP address or hostname to ping.
- `-c <count>`: (Optional) The number of pings to send. Default is 4.

### Examples

1. **Ping a Host with Default Count:**

   ```bash
   python main.py example.com
   ```

   This command will ping `example.com` four times and display the round-trip time for each ping along with the average round-trip time.

2. **Ping a Host with Custom Count:**

   ```bash
   python main.py 192.168.1.1 -c 10
   ```

   This command will ping the IP address `192.168.1.1` ten times and display the round-trip time for each ping along with the average round-trip time.

## Troubleshooting

- **No Valid Ping Responses Received:**
  - Ensure that the host is reachable and that there are no network issues.
  - Verify that the host is correctly specified (IP address or hostname).

- **Error: [Error Message]:**
  - Check the error message for more details.
  - Ensure that you have the necessary permissions to send ICMP echo requests.

## Conclusion

The ChatDev Ping Tool is a simple yet effective CLI application for sending ICMP echo requests to a specified host. It provides detailed round-trip time information and a summary of the average round-trip time, making it a valuable tool for network diagnostics and monitoring.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to the ChatDev support team.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev Ping Tool effectively.