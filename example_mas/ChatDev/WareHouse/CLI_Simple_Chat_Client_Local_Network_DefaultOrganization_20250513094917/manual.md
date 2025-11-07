manual.md

```
# CLI Chat Client

A simple Command Line Interface (CLI) chat client for local networks, allowing users to connect to a chat server, send, and receive text messages.

## Introduction

The CLI Chat Client is designed to facilitate text-based communication over a local network. It connects to a specified chat server and allows users to send and receive messages in real-time. This application is ideal for environments where a simple, text-based communication tool is needed.

## Main Functions

- **Connect to Server**: Establishes a connection to a chat server running on a specified host and port.
- **Send Messages**: Allows users to send text messages to the server, which can then be broadcast to other connected clients.
- **Receive Messages**: Continuously listens for incoming messages from the server and displays them to the user.
- **Exit**: Users can disconnect from the server by typing 'exit'.

## Quick Install

To run the CLI Chat Client, you need to have Python installed on your system. Follow these steps to set up the environment:

1. **Install Python**: Ensure Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

2. **Clone the Repository**: Download the code files to your local machine.

3. **Navigate to the Project Directory**: Open a terminal and navigate to the directory where the code files are located.

## How to Use

1. **Start the Chat Server**: Ensure that a chat server is running on the local network. The server should be listening on the default port `12345` or any other specified port.

2. **Run the Chat Client**: Execute the following command in your terminal to start the chat client:
   ```bash
   python main.py
   ```

3. **Connect to the Server**: The client will attempt to connect to the server. If the server is not running, the client will retry up to 5 times.

4. **Send Messages**: Once connected, type your message and press Enter to send it. To exit the chat, type `exit` and press Enter.

5. **Receive Messages**: Incoming messages from the server will be displayed in the terminal.

## Troubleshooting

- **Connection Issues**: If the client fails to connect, ensure the server is running and the network connection is stable. The client will retry connecting up to 5 times.

- **Server Disconnection**: If the server disconnects, the client will close the connection and exit.

## Additional Information

For further assistance or to report issues, please contact our support team.

```