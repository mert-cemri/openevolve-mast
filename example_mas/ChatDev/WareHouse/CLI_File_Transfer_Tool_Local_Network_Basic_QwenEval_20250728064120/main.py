'''
Main file to run the File Transfer Application.
It initializes the server or client based on user input.
'''
import sys
from server import Server
from client import Client
def main():
    if len(sys.argv) < 3:
        print("Usage: python main.py <mode> <host> <port> [file_path]")
        print("Mode: server or client")
        sys.exit(1)
    mode = sys.argv[1]
    host = sys.argv[2]
    port = int(sys.argv[3])
    if mode == 'server':
        server = Server(host, port)
        server.receive_file()
    elif mode == 'client':
        if len(sys.argv) < 5:
            print("Usage: python main.py client <host> <port> <file_path>")
            sys.exit(1)
        file_path = sys.argv[4]
        client = Client(host, port)
        client.send_file(file_path)
    else:
        print("Invalid mode. Use 'server' or 'client'.")
        sys.exit(1)
if __name__ == "__main__":
    main()