'''
This file provides a command line interface for the chat server. It allows the user to start and stop the server.
'''
from server import ChatServer
import threading
def main():
    server = ChatServer()
    server_thread = threading.Thread(target=server.start_server)
    server_thread.start()
    print("Server started. Type 'stop' to stop the server.")
    while True:
        command = input()
        if command.lower() == 'stop':
            server.stop_server()  # Use the new stop_server method
            print("Server stopped.")
            break
if __name__ == "__main__":
    main()