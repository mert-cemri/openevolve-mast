'''
Handles the connection to the chat server, sending, and receiving messages.
'''
import socket
import threading
class ChatClient:
    def __init__(self, server_ip, server_port):
        self.server_ip = server_ip
        self.server_port = server_port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.connected = False
        self.message_callback = None
    def connect(self):
        try:
            self.client_socket.connect((self.server_ip, self.server_port))
            self.connected = True
            print(f"Connected to {self.server_ip}:{self.server_port}")
        except socket.error as e:
            print(f"Failed to connect to {self.server_ip}:{self.server_port}. Error: {e}")
            self.connected = False
    def send_message(self, message):
        if self.connected:
            try:
                self.client_socket.sendall(message.encode('utf-8'))
            except socket.error as e:
                print(f"Failed to send message. Error: {e}")
                self.disconnect()
    def receive_messages(self):
        while self.connected:
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    if self.message_callback:
                        self.message_callback(message)
                else:
                    # Handle the case where the server sends an empty message (graceful disconnect)
                    print("Server disconnected.")
                    self.disconnect()
                    break
            except socket.error as e:
                print(f"Socket error: {e}")
                self.disconnect()
                break
            except ConnectionResetError:
                print("Connection was reset by the server.")
                self.disconnect()
                break
            except Exception as e:
                print(f"Unexpected error: {e}")
                self.disconnect()
                break
    def disconnect(self):
        if self.connected:
            self.client_socket.close()
            self.connected = False
            print("Disconnected from server")
    def set_message_callback(self, callback):
        self.message_callback = callback