'''
This module implements a simple CLI chat server using Python's socket library.
It listens for connections from chat clients and broadcasts messages to all connected clients.
'''
import socket
import threading
class ClientHandler:
    def __init__(self, client_socket, address, server):
        self.client_socket = client_socket
        self.address = address
        self.server = server
        self.running = True
        self.thread = threading.Thread(target=self.receive_messages)
        self.thread.start()
    def receive_messages(self):
        while self.running:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    self.server.broadcast_message(message, self.client_socket)
                else:
                    self.stop()
            except ConnectionResetError:
                self.stop()
    def send_message(self, message):
        try:
            self.client_socket.sendall(message.encode('utf-8'))
        except ConnectionResetError:
            self.stop()
    def stop(self):
        self.running = False
        self.client_socket.close()
        self.server.remove_client(self)
class Server:
    def __init__(self, host='127.0.0.1', port=12345):
        self.host = host
        self.port = port
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.clients = []
        self.running = True
    def start_server(self):
        self.server_socket.bind((self.host, self.port))
        self.server_socket.listen()
        print(f"Server started on {self.host}:{self.port}")
        self.accept_clients()
    def accept_clients(self):
        while self.running:
            try:
                client_socket, address = self.server_socket.accept()
                print(f"Connection from {address}")
                client_handler = ClientHandler(client_socket, address, self)
                self.clients.append(client_handler)
            except OSError:
                # This exception is raised when the server socket is closed
                break
    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client.client_socket != sender_socket:
                client.send_message(message)
    def remove_client(self, client_handler):
        if client_handler in self.clients:
            self.clients.remove(client_handler)
    def stop_server(self):
        self.running = False
        # Close the server socket to stop accepting new connections
        self.server_socket.close()
        # Stop all client handler threads
        for client in self.clients:
            client.stop()
        # Wait for all client handler threads to finish
        for client in self.clients:
            client.thread.join()
def main():
    server = Server()
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
    print("Type 'exit' to stop the server.")
    while True:
        command = input()
        if command.strip().lower() == 'exit':
            server.stop_server()
            break
    server_thread.join()
if __name__ == "__main__":
    main()