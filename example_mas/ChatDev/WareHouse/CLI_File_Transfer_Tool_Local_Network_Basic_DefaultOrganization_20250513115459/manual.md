```markdown
# CLI File Transfer Tool

A simple command-line interface (CLI) tool for transferring files over a local network. This tool allows you to send a file from one machine (client) to another (server) running a corresponding receiver script.

## Quick Install

This project does not require any external dependencies, making it easy to set up and use. Ensure you have Python installed on your system.

## 🤔 What is this?

This CLI File Transfer Tool is designed to facilitate the transfer of files between two machines on the same local network. It consists of a server-side script that listens for incoming connections and a client-side script that sends files to the server.

## 📖 Documentation

### Main Functions

- **Server-Side (Receiver):** Listens for incoming connections and receives files sent from the client.
- **Client-Side (Sender):** Sends a specified file to the server.

### Setting Up the Environment

1. **Ensure Python is Installed:**
   - Make sure Python is installed on both the client and server machines. You can download it from [python.org](https://www.python.org/downloads/).

2. **No Additional Dependencies:**
   - This project does not require any additional Python packages. The built-in `socket` library is used for network communication.

### How to Use

#### Server-Side (Receiver)

1. **Run the Server Script:**
   - Open a terminal on the server machine.
   - Navigate to the directory containing `main.py`.
   - Run the server script with the following command:
     ```
     python main.py <server_host> <server_port>
     ```
   - Replace `<server_host>` with the server's IP address and `<server_port>` with the desired port number.
   - Example:
     ```
     python main.py 192.168.1.2 65432
     ```
   - The server will start listening for incoming connections.

#### Client-Side (Sender)

1. **Prepare the Client Script:**
   - You will need to create a client script to send files. Below is a basic example of how you might implement this:

   ```python
   import socket
   import sys
   import os

   def send_file(server_host, server_port, file_path):
       try:
           with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
               client_socket.connect((server_host, server_port))
               filename = os.path.basename(file_path)
               filename_bytes = filename.encode()
               client_socket.send(len(filename_bytes).to_bytes(4, 'big'))
               client_socket.send(filename_bytes)
               with open(file_path, 'rb') as f:
                   while (chunk := f.read(1024)):
                       client_socket.send(chunk)
               print(f"File {filename} sent successfully.")
       except Exception as e:
           print(f"An error occurred: {e}")

   if __name__ == "__main__":
       if len(sys.argv) != 4:
           print("Usage: python client.py <server_host> <server_port> <file_path>")
       else:
           _, server_host, server_port, file_path = sys.argv
           send_file(server_host, int(server_port), file_path)
   ```

2. **Run the Client Script:**
   - Open a terminal on the client machine.
   - Navigate to the directory containing your client script.
   - Run the client script with the following command:
     ```
     python client.py <server_host> <server_port> <file_path>
     ```
   - Replace `<server_host>` with the server's IP address, `<server_port>` with the port number, and `<file_path>` with the path to the file you want to send.
   - Example:
     ```
     python client.py 192.168.1.2 65432 /path/to/file.txt
     ```

### Troubleshooting

- **Connection Issues:** Ensure both machines are on the same local network and that the server's IP address and port number are correct.
- **File Not Received:** Check for any errors in the terminal output and ensure the file path is correct on the client-side.

This tool provides a straightforward way to transfer files over a local network using Python's built-in capabilities.
```