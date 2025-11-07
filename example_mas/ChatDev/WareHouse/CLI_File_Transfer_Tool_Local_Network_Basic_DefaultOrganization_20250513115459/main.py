'''
This module implements the server-side of the file transfer tool. It listens for incoming connections and receives a file.
'''
import socket
def receive_file(server_host, server_port):
    """
    Listens for incoming connections and receives a file.
    """
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server_socket:
            server_socket.bind((server_host, server_port))
            server_socket.listen(1)
            print(f"Server listening on {server_host}:{server_port}")
            conn, addr = server_socket.accept()
            with conn:
                print(f"Connected by {addr}")
                # Receive the length of the filename
                filename_length = int.from_bytes(conn.recv(4), 'big')
                # Receive the filename
                filename = conn.recv(filename_length).decode()
                with open(filename, 'wb') as f:
                    while (chunk := conn.recv(1024)):
                        f.write(chunk)
                print(f"File {filename} received successfully.")
    except Exception as e:
        print(f"An error occurred: {e}")
if __name__ == "__main__":
    import sys
    if len(sys.argv) != 3:
        print("Usage: python main.py <server_host> <server_port>")
    else:
        _, server_host, server_port = sys.argv
        receive_file(server_host, int(server_port))