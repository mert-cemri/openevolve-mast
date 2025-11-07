```markdown
# Simple CLI Chat Server

A simple command-line interface (CLI) chat server application designed for local network communication. This server listens for connections from chat clients and broadcasts messages to all connected clients.

## Main Functions

- **Connection Handling**: Accepts multiple client connections and manages them concurrently.
- **Message Broadcasting**: Receives messages from clients and broadcasts them to all other connected clients.
- **Client Management**: Handles client disconnections and ensures the server continues to run smoothly.

## Installation

### Prerequisites

- **Python 3.x**: Ensure you have Python installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Environment Setup

1. **Clone the Repository**: Download the source code to your local machine.
   ```bash
   git clone <repository-url>
   cd <repository-directory>
   ```

2. **Install Dependencies**: This project does not require any external dependencies beyond Python's standard library. However, ensure your environment is set up correctly.

   ```bash
   # No external dependencies are required for this project.
   ```

## Usage

### Running the Server

1. **Start the Server**: Execute the `main.py` script to start the chat server.
   ```bash
   python main.py
   ```

2. **Server Output**: Once started, the server will listen for incoming client connections on the default host `127.0.0.1` and port `12345`. You will see output indicating the server is running and any new client connections.

3. **Stopping the Server**: To stop the server, type `exit` in the command line where the server is running.

### Connecting Clients

- Clients can connect to the server using a compatible chat client application that supports socket connections to the specified host and port.

## Additional Information

- **Customization**: You can modify the server's host and port by editing the `Server` class initialization parameters in `main.py`.
- **Thread Management**: The server uses threading to handle multiple clients concurrently, ensuring efficient message broadcasting and client management.

For further assistance or inquiries, please contact our support team.
```
