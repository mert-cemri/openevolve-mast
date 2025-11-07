# ChatDev CLI Chat Client

## Introduction

Welcome to the ChatDev CLI Chat Client, a simple yet powerful tool designed to facilitate text-based communication within a local network. This application connects to a corresponding chat server, enabling users to send and receive messages seamlessly via the command line interface (CLI).

## Main Functions

- **Connect to Chat Server:** Establishes a connection to the chat server using the specified IP address and port.
- **Send Messages:** Allows users to input and send text messages to the connected chat server.
- **Receive Messages:** Continuously listens for incoming messages from the chat server and displays them in real-time.
- **Graceful Disconnection:** Handles server disconnections gracefully, ensuring a smooth user experience.

## Quick Install

To use the ChatDev CLI Chat Client, you need to have Python installed on your system. Follow the steps below to install the necessary dependencies and set up the environment.

### Step 1: Install Python

Ensure that Python is installed on your system. You can download it from the [official Python website](https://www.python.org/downloads/).

### Step 2: Clone the Repository

Clone the ChatDev CLI Chat Client repository from GitHub to your local machine:

```bash
git clone https://github.com/ChatDev/cli-chat-client.git
cd cli-chat-client
```

### Step 3: Install Dependencies

The ChatDev CLI Chat Client requires a few Python packages to function correctly. These dependencies are listed in the `requirements.txt` file. Install them using pip:

```bash
pip install -r requirements.txt
```

**Note:** The `requirements.txt` file should be located in the root directory of the project. If it is missing, you can create it with the following content:

```
# requirements.txt
```

Since our application uses only standard Python libraries (`socket` and `threading`), no additional third-party packages are required.

## How to Use

### Step 1: Start the Chat Server

Before running the ChatDev CLI Chat Client, ensure that the corresponding chat server is up and running. The server should be configured to listen on the IP address and port specified in the client configuration.

### Step 2: Run the Chat Client

Navigate to the root directory of the ChatDev CLI Chat Client project and run the `main.py` script:

```bash
python main.py
```

### Step 3: Connect to the Server

Upon running the script, the ChatDev CLI Chat Client will attempt to connect to the chat server using the default IP address (`127.0.0.1`) and port (`12345`). If the server is running and accessible, you will see a confirmation message indicating a successful connection.

### Step 4: Send and Receive Messages

Once connected, you can start sending messages by typing them into the CLI. Press `Enter` to send the message. Incoming messages from other users will be displayed in real-time.

### Step 5: Exit the Chat Client

To exit the ChatDev CLI Chat Client, type `exit` and press `Enter`. The client will disconnect from the server and terminate the application.

## Troubleshooting

### Connection Issues

- **Server Not Running:** Ensure that the chat server is running and listening on the specified IP address and port.
- **Incorrect IP Address or Port:** Verify that the IP address and port specified in the `main.py` script match those of the running chat server.

### Message Delivery Issues

- **Server Disconnected:** If the server disconnects unexpectedly, the ChatDev CLI Chat Client will handle the disconnection gracefully and terminate the application.

## Conclusion

The ChatDev CLI Chat Client is a simple yet effective tool for real-time text communication within a local network. By following the installation and usage instructions provided in this manual, you can quickly set up and start using the client to send and receive messages.

If you encounter any issues or have suggestions for improvement, please feel free to reach out to our support team or contribute to the project on GitHub.

---

This manual should provide a comprehensive guide for users to understand and use the ChatDev CLI Chat Client effectively.