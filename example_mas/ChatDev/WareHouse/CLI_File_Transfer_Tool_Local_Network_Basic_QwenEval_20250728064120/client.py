'''
Client module to handle file sending over a local network.
'''
import socket
import os
class Client:
    def __init__(self, host='127.0.0.1', port=65432):
        self.host = host
        self.port = port
    def connect_to_server(self):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.host, self.port))
            return s
    def send_file(self, file_path):
        with self.connect_to_server() as s:
            file_name = os.path.basename(file_path)
            s.sendall(file_name.encode())
            with open(file_path, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        break
                    s.sendall(data)
            print(f"File {file_name} sent to {self.host}:{self.port}")
            return f"File {file_name} sent to {self.host}:{self.port}"