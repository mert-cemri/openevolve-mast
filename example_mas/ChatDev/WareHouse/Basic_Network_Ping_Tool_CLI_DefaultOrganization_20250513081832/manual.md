# CLI Network Ping Tool

A simple command-line interface (CLI) tool for sending ICMP echo requests (pings) to a specified IP address or hostname. The tool allows users to configure the number of pings to send and provides a summary of the round-trip times.

## Quick Install

To get started with the CLI Network Ping Tool, you'll need to have Python installed on your system. The tool is compatible with Python version 3.6 and above.

### Step 1: Clone the Repository

First, clone the repository to your local machine:

```bash
git clone <repository-url>
cd <repository-directory>
```

### Step 2: Install Dependencies

The tool requires Python 3.6 or newer. You can install the necessary dependencies using the following command:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The CLI Network Ping Tool is designed to help users test the reachability of a host on an IP network. It sends a series of ICMP echo requests to the specified address and measures the time it takes for each request to receive a response. This is useful for diagnosing network connectivity issues and measuring network performance.

## 📖 How to Use

### Running the Tool

To use the CLI Network Ping Tool, run the following command in your terminal:

```bash
python main.py <address> <count>
```

- `<address>`: The IP address or hostname you want to ping.
- `<count>`: The number of ICMP echo requests to send.

### Example

To ping `google.com` with 5 echo requests, use the following command:

```bash
python main.py google.com 5
```

### Output

The tool will display the round-trip time for each ping and provide a summary of the results. If the ping command fails, an error message will be displayed.

## Troubleshooting

- Ensure that you have a stable internet connection.
- Verify that the IP address or hostname is correct.
- Check your firewall settings to ensure that ICMP packets are not being blocked.

## 📖 Documentation

For more detailed information on the tool's functionality and troubleshooting, please refer to the source code comments and logging outputs.

## Support

If you encounter any issues or have questions about the CLI Network Ping Tool, please contact our support team for assistance.