'''
This is the main file for the CLI chat client. It initializes the ChatClient and starts the chat application.
'''
import socket
import threading
import time
class ChatClient:
    def __init__(self, host='localhost', port=12345):
        '''
        Initializes the ChatClient with the server's host and port.
        '''
        self.server_host = host
        self.server_port = port
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    def connect_to_server(self):
        '''
        Connects to the chat server.
        '''
        retry_count = 0
        max_retries = 5
        while retry_count < max_retries:
            try:
                self.client_socket.connect((self.server_host, self.server_port))
                print(f"Connected to chat server at {self.server_host}:{self.server_port}")
                break
            except ConnectionRefusedError:
                print("Failed to connect to the server. Make sure the server is running.")
                retry_count += 1
                if retry_count < max_retries:
                    print(f"Retrying in 5 seconds... ({retry_count}/{max_retries})")
                    time.sleep(5)
                else:
                    print("Max retries reached. Exiting the chat client.")
                    exit()
    def send_message(self):
        '''
        Sends messages to the server.
        '''
        while True:
            message = input()
            if message.lower() == 'exit':
                self.client_socket.sendall(message.encode())
                print("Disconnected from chat server.")
                self.client_socket.close()
                break
            self.client_socket.sendall(message.encode())
    def receive_messages(self):
        '''
        Receives messages from the server.
        '''
        while True:
            try:
                message = self.client_socket.recv(1024).decode()
                if message:
                    print(f"Server: {message}")
                else:
                    print("Disconnected from server.")
                    self.client_socket.close()
                    break
            except ConnectionResetError:
                print("Connection lost. Closing the connection.")
                self.client_socket.close()
                exit()
    def start_chat(self):
        '''
        Starts the chat client.
        '''
        self.connect_to_server()
        threading.Thread(target=self.receive_messages, daemon=True).start()
        self.send_message()
def main():
    '''
    Entry point of the chat client application.
    '''
    client = ChatClient()
    client.start_chat()
if __name__ == "__main__":
    main()