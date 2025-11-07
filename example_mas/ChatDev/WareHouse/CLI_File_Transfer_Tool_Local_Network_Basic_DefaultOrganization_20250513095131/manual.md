```markdown
# CLI File Transfer Tool

A simple command-line interface (CLI) application for transferring files over a local network. This tool allows you to send a file from one machine (client) to another (server) running a corresponding receiver script.

## Quick Install

This project does not require any external dependencies beyond Python's standard library. Ensure you have Python installed on your system.

## 🤔 What is this?

The CLI File Transfer Tool is designed to facilitate the transfer of files between two machines on the same local network. It consists of two main components:

- **Server**: Listens for incoming connections and receives files from clients.
- **Client**: Connects to the server and sends files.

## 📖 Documentation

### Main Functions

- **Server**: Starts a server that listens for incoming file transfers.
- **Client**: Sends a specified file to the server.

### How to Use

1. **Start the Server**

   To start the server, run the following command in your terminal:

   ```bash
   python main.py server --host <host> --port <port>
   ```

   - `--host`: The host address to bind the server (default is `0.0.0.0`).
   - `--port`: The port number to bind the server (default is `5001`).

   Example:

   ```bash
   python main.py server --host 0.0.0.0 --port 5001
   ```

   This will start the server and it will listen for incoming connections on the specified host and port.

2. **Send a File from the Client**

   To send a file from the client, run the following command in your terminal:

   ```bash
   python main.py client <file_path> --host <server_host> --port <server_port>
   ```

   - `<file_path>`: The path of the file you want to send.
   - `--host`: The server host to connect to (default is `localhost`).
   - `--port`: The server port to connect to (default is `5001`).

   Example:

   ```bash
   python main.py client example.txt --host 192.168.1.10 --port 5001
   ```

   This will send the file `example.txt` to the server running on `192.168.1.10` at port `5001`.

### Additional Information

- Ensure both the client and server are on the same local network for successful file transfer.
- The server will save received files with a timestamped filename to avoid overwriting existing files.

For any further assistance or support, please contact our support team.
```