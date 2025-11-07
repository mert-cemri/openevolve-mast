'''
Main entry point for the CLI file transfer application. Handles command-line arguments for server and client operations.
'''
import argparse
from server import start_server
from client import send_file
def main():
    parser = argparse.ArgumentParser(description="CLI File Transfer Tool")
    subparsers = parser.add_subparsers(dest='command')
    server_parser = subparsers.add_parser('server', help='Start the server to receive files')
    server_parser.add_argument('--host', default='0.0.0.0', help='Host to bind the server')
    server_parser.add_argument('--port', type=int, default=5001, help='Port to bind the server')
    client_parser = subparsers.add_parser('client', help='Send a file to the server')
    client_parser.add_argument('file_path', help='Path of the file to send')
    client_parser.add_argument('--host', default='localhost', help='Server host to connect to')
    client_parser.add_argument('--port', type=int, default=5001, help='Server port to connect to')
    args = parser.parse_args()
    if args.command == 'server':
        start_server(host=args.host, port=args.port)
    elif args.command == 'client':
        send_file(args.file_path, host=args.host, port=args.port)
    else:
        parser.print_help()
if __name__ == "__main__":
    main()