```markdown
# CLI Network Ping Tool

A simple command-line interface (CLI) tool to send ICMP echo requests to a specified IP address or hostname, displaying the round-trip time for each request and providing a summary.

## Quick Install

To use the CLI Network Ping Tool, you need to have Python installed on your system. The tool is compatible with Python version 3.6 and above.

### Step 1: Clone the Repository

Clone the repository to your local machine using the following command:

```bash
git clone <repository-url>
```

### Step 2: Navigate to the Project Directory

Change your directory to the project folder:

```bash
cd <repository-folder>
```

### Step 3: Install Dependencies

Install the required dependencies using pip:

```bash
pip install -r requirements.txt
```

## 🤔 What is this?

The CLI Network Ping Tool is designed to help users test the reachability of a host on an IP network. It sends a configurable number of ICMP echo requests to the specified address and displays the round-trip time for each request. Additionally, it provides a summary of the ping statistics.

## 📖 How to Use

### Running the Tool

To run the tool, use the following command:

```bash
python main.py <address> <count>
```

- `<address>`: The IP address or hostname you want to ping.
- `<count>`: The number of ICMP echo requests to send.

### Example

To ping `google.com` with 4 echo requests, use:

```bash
python main.py google.com 4
```

### Output

The tool will display the round-trip time for each request and a summary of the ping statistics, which includes the average round-trip time.

## 📖 Documentation

For more detailed information on the tool's functionality and usage, please refer to the source code comments and function docstrings in `main.py`.

## Troubleshooting

- Ensure that Python is installed and the version is 3.6 or above.
- Make sure you have the necessary permissions to run ping commands on your system.
- If you encounter any errors, check the output for specific error messages and verify your network connection.

## Support

For further assistance or to report issues, please contact our support team or open an issue in the repository.

```
```