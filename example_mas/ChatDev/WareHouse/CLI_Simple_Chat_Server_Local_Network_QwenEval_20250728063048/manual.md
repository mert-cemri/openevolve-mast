# ChatDev CLI Chat Server Manual

## Introduction

Welcome to the ChatDev CLI Chat Server! This manual will guide you through the installation, setup, and usage of the chat server and client. The server listens for connections from chat clients and broadcasts messages to all connected clients, making it perfect for local network communication.

## Main Functions

### Chat Server
- **Listen for Connections:** The server listens on a specified host and port for incoming client connections.
- **Broadcast Messages:** When a client sends a message, the server broadcasts it to all other connected clients.
- **Handle Multiple Clients:** The server can handle multiple clients simultaneously using asynchronous programming.

### Chat Client
- **Connect to Server:** The client connects to the server using a specified host and port.
- **Send Messages:** The client can send messages to the server.
- **Receive Messages:** The client receives messages broadcasted by the server from other clients.

## Installation

### Prerequisites
- Python 3.7 or higher

### Steps
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/your-repo/chatdev-cli-chat-server.git
   cd chatdev-cli-chat-server
   ```

2. **Install Dependencies:**
   This project does not require any external dependencies. However, ensure you have Python installed:
   ```bash
   python --version
   ```

## Usage

### Running the Chat Server
1. **Start the Server:**
   ```bash
   python main.py server
   ```
   - By default, the server listens on `127.0.0.1` (localhost) and port `65432`.
   - You can specify a different host and port by modifying the `ChatServer` initialization in `main.py`.

### Running the Chat Client
1. **Start the Client:**
   ```bash
   python main.py
   ```
   - By default, the client connects to `127.0.0.1` (localhost) and port `65432`.
   - You can specify a different host and port by modifying the `ChatClient` initialization in `main.py`.

2. **Interact with the Server:**
   - Once connected, you can type messages and press Enter to send them.
   - The client will display messages received from the server.

### Example Workflow
1. **Start the Server:**
   ```bash
   python main.py server
   ```
   - Output: `Serving on ('127.0.0.1', 65432)`

2. **Start Multiple Clients:**
   ```bash
   python main.py
   ```
   - Output: `Connected to 127.0.0.1:65432`
   - Type messages in each client window to see them broadcasted to all connected clients.

## Troubleshooting

### Connection Issues
- **Server Not Running:** Ensure the server is running before starting clients.
- **Incorrect Host/Port:** Verify that the host and port specified in the client match those used by the server.

### Error Messages
- **ConnectionRefusedError:** The server might not be running or the specified host/port is incorrect.
- **KeyboardInterrupt:** Use `Ctrl+C` to gracefully exit the client.

## Conclusion

Thank you for using ChatDev CLI Chat Server! We hope this manual has been helpful. If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team.

---

This manual provides a comprehensive guide for users to understand and utilize the ChatDev CLI Chat Server effectively.