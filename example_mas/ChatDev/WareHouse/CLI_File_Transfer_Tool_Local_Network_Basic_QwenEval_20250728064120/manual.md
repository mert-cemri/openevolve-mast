# ChatDev File Transfer Tool User Manual

## Introduction

Welcome to the ChatDev File Transfer Tool, a simple yet powerful command-line interface (CLI) tool designed for transferring files over a local network. This tool is ideal for users who need to share files between two machines without the need for complex setup or additional software.

## Key Features

- **Local Network Transfer:** Efficiently transfer files between two machines on the same local network.
- **Command-Line Interface:** Easy to use with minimal setup.
- **Cross-Platform:** Works on Windows, macOS, and Linux.

## Prerequisites

- **Python 3.6+** installed on both the client and server machines.
- **Basic understanding of command-line operations.**

## Installation

### Step 1: Install Python

Ensure Python 3.6 or higher is installed on both machines. You can download Python from the [official website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the ChatDev File Transfer Tool repository from GitHub:

```bash
git clone https://github.com/ChatDev/file-transfer-tool.git
cd file-transfer-tool
```

### Step 3: Install Dependencies

This tool does not require any external dependencies beyond Python's standard library. However, if you have a `requirements.txt` file, you can install any additional dependencies using:

```bash
pip install -r requirements.txt
```

## Usage

### Starting the Server

1. **Navigate to the Project Directory:**

   ```bash
   cd path/to/file-transfer-tool
   ```

2. **Run the Server Script:**

   ```bash
   python main.py server <host> <port> [save_directory]
   ```

   - `<host>`: The IP address of the server machine (e.g., `192.168.1.100`).
   - `<port>`: The port number to listen on (e.g., `65432`).
   - `[save_directory]` (optional): The directory where received files will be saved (default is `received_files`).

   **Example:**

   ```bash
   python main.py server 192.168.1.100 65432
   ```

### Sending a File

1. **Navigate to the Project Directory:**

   ```bash
   cd path/to/file-transfer-tool
   ```

2. **Run the Client Script:**

   ```bash
   python main.py client <host> <port> <file_path>
   ```

   - `<host>`: The IP address of the server machine (e.g., `192.168.1.100`).
   - `<port>`: The port number the server is listening on (e.g., `65432`).
   - `<file_path>`: The path to the file you want to send.

   **Example:**

   ```bash
   python main.py client 192.168.1.100 65432 /path/to/example.txt
   ```

## Example Workflow

1. **Start the Server:**

   On the machine that will receive the file, run:

   ```bash
   python main.py server 192.168.1.100 65432
   ```

2. **Send a File:**

   On the machine that will send the file, run:

   ```bash
   python main.py client 192.168.1.100 65432 /path/to/example.txt
   ```

3. **Verify File Transfer:**

   Check the `received_files` directory on the server machine to ensure the file has been received.

## Troubleshooting

- **Connection Issues:** Ensure both machines are on the same local network and the server is running before starting the client.
- **File Not Found:** Double-check the file path provided to the client script.
- **Permission Errors:** Ensure the server has write permissions to the specified save directory.

## Conclusion

The ChatDev File Transfer Tool is a simple yet effective solution for transferring files over a local network. By following the steps outlined in this manual, you should be able to set up and use the tool without any issues. If you encounter any problems, please refer to the troubleshooting section or contact our support team for assistance.

---

Feel free to reach out if you have any questions or need further assistance!

Best regards,

[Your Name]  
Chief Product Officer  
ChatDev

---

This manual should provide a comprehensive guide for users to install, configure, and use the ChatDev File Transfer Tool effectively.