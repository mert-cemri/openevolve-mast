```markdown
# Simple CLI Chat Client

A simple command-line interface (CLI) chat client for connecting to a chat server over a local network. This application allows users to send and receive text messages in real-time.

## Main Functions

- **Connect to Server**: Establishes a connection to a chat server running on a specified host and port.
- **Send Messages**: Allows users to send text messages to the connected chat server.
- **Receive Messages**: Continuously listens for incoming messages from the server and displays them to the user.
- **Exit Chat**: Users can exit the chat session by typing 'exit'.

## Installation and Setup

### Prerequisites

- **Python 3.x**: Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/).

### Quick Install

1. **Clone the Repository**: Download the source code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Python**: Make sure Python is installed. You can verify the installation by running:
   ```bash
   python --version
   ```

3. **Install Dependencies**: This project does not require any external dependencies as it uses Python's standard library. However, ensure your Python environment is set up correctly.

## How to Use

1. **Start the Chat Server**: Before running the client, ensure that a chat server is running on the network. The server should be listening on the same host and port specified in the `client.py` file (default is `localhost:12345`).

2. **Run the Chat Client**: Execute the `main.py` script to start the chat client.
   ```bash
   python main.py
   ```

3. **Send and Receive Messages**: Once connected, you can start typing messages. Press `Enter` to send a message. Incoming messages from other users will be displayed in real-time.

4. **Exit the Chat**: To leave the chat session, type `exit` and press `Enter`. This will close the connection and terminate the client.

## Troubleshooting

- **Connection Issues**: If you encounter a "Failed to connect to server" error, ensure that the server is running and accessible on the specified host and port.
- **Message Sending/Receiving Issues**: If messages are not being sent or received, check your network connection and ensure the server is functioning correctly.

## Additional Information

This chat client is designed for educational purposes and local network use. For production use, consider implementing additional features such as authentication, encryption, and error handling.

For further assistance or to report issues, please contact our support team.

```