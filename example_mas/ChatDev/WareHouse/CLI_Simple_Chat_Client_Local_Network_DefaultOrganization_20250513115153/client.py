'''
A simple CLI chat client for connecting to a chat server.
'''
import socket
import threading
class ChatClient:
    '''
    A simple CLI chat client for connecting to a chat server.
    '''
    def __init__(self, host='localhost', port=12345):
        '''
        Initializes the chat client with server host and port.
        '''
        self.server_host = host
        self.server_port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect_to_server(self):
        '''
        Connects to the chat server.
        '''
        try:
            self.client_socket.connect((self.server_host, self.server_port))
            print(f"Connected to chat server at {self.server_host}:{self.server_port}")
        except ConnectionRefusedError:
            print("Failed to connect to server. Make sure the server is running.")
            exit(1)
    def send_message(self, message):
        '''
        Sends a message to the chat server.
        '''
        try:
            if self.client_socket:
                self.client_socket.sendall(message.encode('utf-8'))
            else:
                print("Cannot send message. Connection is closed.")
        except Exception as e:
            print(f"Error sending message: {e}")
    def receive_messages(self):
        '''
        Listens for incoming messages from the server.
        '''
        try:
            while True:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"\n{message}")
                else:
                    print("Disconnected from server.")
                    break
        except Exception as e:
            print(f"Error receiving message: {e}")
        finally:
            print("Closing connection...")
            self.client_socket.close()
            print("Client terminated. Please restart to reconnect.")
    def run(self):
        '''
        Main loop to handle user input and display messages.
        '''
        self.connect_to_server()
        threading.Thread(target=self.receive_messages, daemon=True).start()
        while True:
            message = input("You: ")
            if message.lower() == 'exit':
                print("Exiting chat...")
                self.client_socket.close()
                break
            try:
                self.send_message(message)
            except Exception as e:
                print("Cannot send message. Connection might be lost.")
                break