'''
Server module to handle file reception over a local network.
'''
import socket
import os
class Server:
    def __init__(self, host='127.0.0.1', port=65432, save_directory='received_files'):
        self.host = host
        self.port = port
        self.save_directory = save_directory
    def start_server(self):
        os.makedirs(self.save_directory, exist_ok=True)
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((self.host, self.port))
            s.listen()
            print(f"Server listening on {self.host}:{self.port}")
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                file_name = conn.recv(1024).decode()
                file_path = os.path.join(self.save_directory, file_name)
                with open(file_path, 'wb') as f:
                    while True:
                        data = conn.recv(1024)
                        if not data:
                            break
                        f.write(data)
                print(f"File {file_name} received and saved to {file_path}")
                return f"File {file_name} received and saved to {file_path}"
    def receive_file(self):
        return self.start_server()