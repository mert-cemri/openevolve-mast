'''
Server logic to receive files from the client.
'''
import socket
import time
def start_server(host='0.0.0.0', port=5001):
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((host, port))
    server_socket.listen(1)
    print(f"Server listening on {host}:{port}")
    while True:
        conn, addr = server_socket.accept()
        print(f"Connection from {addr}")
        receive_file(conn)
        conn.close()
def receive_file(conn):
    filename = f"received_file_{int(time.time())}"
    with open(filename, 'wb') as f:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            f.write(data)
    print(f"File received successfully and saved as {filename}.")