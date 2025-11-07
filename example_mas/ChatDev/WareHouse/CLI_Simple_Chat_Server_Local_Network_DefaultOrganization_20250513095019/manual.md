```markdown
# ChatDev CLI Chat Server

A simple command-line interface (CLI) chat server for local networks. This server listens for connections from chat clients and broadcasts messages to all connected clients.

## Main Functions

- **Start and Stop Server**: The server can be started and stopped using simple commands.
- **Client Connection Management**: Manages multiple client connections simultaneously.
- **Message Broadcasting**: Broadcasts messages from one client to all other connected clients.
- **Client Disconnection Handling**: Automatically handles client disconnections.

## Quick Install

This project does not require any external dependencies. Ensure you have Python installed on your system.

### Step-by-Step Installation

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Verify Python Installation**:
   Ensure Python is installed on your system. You can verify by running:
   ```bash
   python --version
   ```

3. **Install Python (if not installed)**:
   - For Windows: Download and install from [Python's official website](https://www.python.org/downloads/).
   - For macOS: Use Homebrew to install Python:
     ```bash
     brew install python
     ```
   - For Linux: Use the package manager for your distribution, e.g., for Ubuntu:
     ```bash
     sudo apt-get update
     sudo apt-get install python3
     ```

## How to Use

### Starting the Server

1. **Navigate to the Project Directory**:
   ```bash
   cd <repository-directory>
   ```

2. **Run the Server**:
   Execute the following command to start the server:
   ```bash
   python main.py
   ```
   - The server will start and listen for incoming client connections.
   - You will see a message indicating the server has started.

### Stopping the Server

- To stop the server, type `stop` in the command line where the server is running and press Enter. This will gracefully shut down the server and disconnect all clients.

### Connecting Clients

- Clients can connect to the server using any TCP client tool or a custom client script that connects to the server's IP address and port (default is `localhost:12345`).

### Broadcasting Messages

- Once connected, any message sent by a client will be broadcast to all other connected clients. Clients will receive messages in real-time as they are broadcast by the server.

## Troubleshooting

- **Server Not Starting**: Ensure no other application is using the default port `12345`. You can change the port in `server.py` if needed.
- **Client Disconnection Issues**: If a client disconnects unexpectedly, ensure network stability and check the client-side implementation for errors.

## Documentation

For more detailed documentation, please refer to the code comments in each file (`main.py`, `client_handler.py`, `server.py`) which provide insights into the implementation and functionality of each component.

```
