'''
Client logic to send files to the server.
'''
import socket
import os
def send_file(file_path, host='localhost', port=5001):
    file_size = os.path.getsize(file_path)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client_socket:
        client_socket.connect((host, port))
        with open(file_path, 'rb') as f:
            while (chunk := f.read(1024)):
                client_socket.sendall(chunk)
    print(f"File {file_path} sent successfully.")