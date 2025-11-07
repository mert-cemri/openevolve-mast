'''
This file contains the ChatServer class, which handles client connections, manages broadcasting messages, and maintains the list of connected clients.
'''
import socket
import threading
from client_handler import ClientHandler
class ChatServer:
    def __init__(self, host='localhost', port=12345):
        self.server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_socket.bind((host, port))
        self.server_socket.listen()
        self.clients = []
        self.running = True  # Add a running flag
    def start_server(self):
        print("Server started, waiting for connections...")
        while self.running:
            try:
                client_socket, addr = self.server_socket.accept()
                print(f"Connection from {addr} has been established.")
                client_handler = ClientHandler(client_socket, self)
                self.clients.append(client_handler)
                threading.Thread(target=client_handler.receive_messages).start()
            except OSError:
                break  # Exit loop if server socket is closed
    def stop_server(self):
        self.running = False
        self.server_socket.close()
        for client in self.clients:
            client.client_socket.close()  # Ensure all client sockets are closed
    def broadcast_message(self, message, sender_socket):
        for client in self.clients:
            if client.client_socket != sender_socket:
                client.send_message(message)
    def remove_client(self, client_handler):
        if client_handler in self.clients:
            self.clients.remove(client_handler)