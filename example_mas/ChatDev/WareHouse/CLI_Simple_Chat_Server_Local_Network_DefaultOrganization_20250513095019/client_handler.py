'''
This file manages individual client connections. It handles receiving and sending messages to and from the client.
'''
class ClientHandler:
    def __init__(self, client_socket, server):
        self.client_socket = client_socket
        self.server = server
    def receive_messages(self):
        while self.server.running:  # Check the server's running flag
            try:
                message = self.client_socket.recv(1024).decode('utf-8')
                if message:
                    print(f"Received message: {message}")
                    self.server.broadcast_message(message, self.client_socket)
                else:
                    break
            except:
                break
        self.client_socket.close()
        self.server.remove_client(self)
    def send_message(self, message):
        try:
            self.client_socket.send(message.encode('utf-8'))
        except:
            self.client_socket.close()
            self.server.remove_client(self)